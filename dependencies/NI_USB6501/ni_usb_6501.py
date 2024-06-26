#!/usr/bin/python
## coding=utf-8
"""
The ni_usb_6501 is a digital IO module for USB from National Instruments.
Unfortunately their Linux driver is excessively large (>60MB), difficult to install
and doesn't offer off-the-shelf support for python.

This python driver is based on Marc Schutz's pioneer work on c driver
(https://github.com/schuetzm/ni-usb-6501)

INSTALLATION
1. Install the latest PyUSB (at least version 1.0.a3) from http://sourcceforge.net/projects/pyusb/

2. Change the permissions of the USB device node by creating a udev rule.
   e.g. add the following line (and file) to a file in /etc/udev/rules.d/usb.rules
   SUBSYSTEM=="usb", ENV{DEVTYPE}=="usb_device", MODE="0664", GROUP="usbusers"

   This will set the owner of the device node to root:usbusers rather than root:root
   After that add user to the usbusers group for enabling access to the device.
   adduser _<user>_ usbusers
  (Make sure you have group usbusers)

...and you are good to go.

TODO
 - Counter operations
"""
import usb.core
import usb.util

ID_VENDOR = 0x3923
ID_PRODUCT = 0x718a

def get_adapter(**kwargs):
    """
    Returns NiUsb6501 handler if only single adapter is connected to PC.
    Forwards all parameters to pyusb (http://pyusb.sourceforge.net/docs/1.0/tutorial.html)
    """
    device = usb.core.find(idVendor=ID_VENDOR, idProduct=ID_PRODUCT, **kwargs)
    if not device:
        raise ValueError('Device not found')

    return NiUsb6501(device)


def find_adapters(**kwargs):
    """
    Returns NiUsb6501 handle for every adapter that is connected to PC.
    Forwards all parameters to pyusb (http://pyusb.sourceforge.net/docs/1.0/tutorial.html)
    """
    devices = usb.core.find(find_all=True, idVendor=ID_VENDOR, idProduct=ID_PRODUCT, **kwargs)
    if not devices:
        raise ValueError('Device not found')

    return [NiUsb6501(dev) for dev in devices]


class NiUsb6501:
    """
    Typical usage:
      adapter = get_adapter()
      adapter.set_io_mode(0b00000000, 0x11111111, 0x01010101) # one bit per port 1=write, 0=read
      # start calling adapter.read_port(port) and adapter.write_port(port, values)
    """
    def __init__(self, device):
        """ used only internally via get_adapter() and find_adapters() """
        self.device = device
        cfg = self.device.get_active_configuration()
        self.interface_number = cfg[(0, 0)].bInterfaceNumber
        self.io_mask = [0, 0, 0]  # All pins initialize to inputs

        if self.device.is_kernel_driver_active(self.interface_number):
            self.device.detach_kernel_driver(self.interface_number)
        # set the active configuration. With no arguments, the first
        # configuration will be the active one
        self.device.set_configuration()
        # This is needed to release interface, otherwise attach_kernel_driver fails 
        # due to "Resource busy"
        usb.util.dispose_resources(self.device)

    def set_io_mode(self, port0=None, port1=None, port2=None):
        """
        Set mode for every IO pin. PIN modes are given in three groups (bitmasks represented by integers)
        bit = 0: read
        bit = 1: write
        """
        # check if mask is a valid 8 bit number
        self.check_valid_mask(port0)
        self.check_valid_mask(port1)
        self.check_valid_mask(port2)
        # if no arguments, use saved io mask
        port0 = self.io_mask[0] if port0 is None else port0
        port1 = self.io_mask[1] if port1 is None else port1
        port2 = self.io_mask[2] if port2 is None else port2

        buf = bytearray(b"\x02\x10\x00\x00\x00\x05\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00")
        buf[6] = port0
        buf[7] = port1
        buf[8] = port2
        self.io_mask = [port0, port1, port2]

        return self.send_request(0x12, buf)

    def change_port_io(self, port, mode_mask):
        """
        Set IO mode of one port. mode_mask is an 8 bit integer
        """
        self.check_valid_port_pin(port)
        self.check_valid_mask(mode_mask)
        self.io_mask[port] = mode_mask
        self.set_io_mode(*self.io_mask)

    def change_pin_io(self, port, pin, mode):
        """
        Set the IO mode of one pin. If self.set_io_mode not called, the default for all pins is low
        Mode parameter is treated as a boolean
        """
        self.check_valid_port_pin(port, pin)
        port_mask = self.io_mask[port]
        port_mask = port_mask | (1 << pin) if mode else port_mask & ~(1 << pin)
        self.change_port_io(port, port_mask)

    def read_port(self, port):
        """
        Read the value from all read-mode pins from one of the 8 PIN ports
        port is 0, 1 or 2
        """
        self.check_valid_port_pin(port)
        buf = bytearray(b"\x02\x10\x00\x00\x00\x03\x00\x00")
        buf[6] = port

        response = bytearray(self.send_request(0x0e, buf))

        self.packet_matches(response,
                            b"\x00\x0c\x01\x00\x00\x00\x00\x02\x00\x03\x00\x00",
                            b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00\xff")

        return response[10]

    def write_port(self, port, value):
        """
        Write value to all write-mode pins in one of the 8 PIN ports
        port is 0, 1 or 2
        value is 8 bits represented by integer
        """
        self.check_valid_port_pin(port)
        self.check_valid_mask(value)
        buf = bytearray(b"\x02\x10\x00\x00\x00\x03\x00\x00\x03\x00\x00\x00")
        buf[6] = port
        buf[9] = value

        response = bytearray(self.send_request(0x0f, buf))
        self.packet_matches(response,
                            b"\x00\x08\x01\x00\x00\x00\x00\x02",
                            b"\xff\xff\xff\xff\xff\xff\xff\xff")

        return response

    def read_pin(self, port, pin):
        """
        Read one pin from a port. This does not make sure that the IO mode is correct
        """
        self.check_valid_port_pin(port, pin)
        port_response = self.read_port(port)

        # bit operation to get the bit at pin
        return (port_response & (1 << pin)) >> pin

    def write_pin(self, port, pin, bit):
        """
        Write one pin in a port. This should perserve all other output pins in the port
        Bit will be interpereted as a boolean
        """
        self.check_valid_port_pin(port, pin)
        write_mask = self.read_port(port)
        # update write_mask with bit
        write_mask = write_mask | (1 << pin) if bit else write_mask & ~(1 << pin)
        write_response = int.from_bytes(self.write_port(port, write_mask))

        return (write_response & (1 << pin)) >> pin

    def send_pulse(self, port, pin):
        """
        Write high to the pin then immediately write low.
        """
        self.write_pin(port, pin, 1)
        self.write_pin(port, pin, 0)

    ##########################################################
    # TODO: COUNTERS ARE NOT YET IMPLEMENTED
    ##########################################################
    def read_counter(self):
        pass

    def write_counter(self):
        pass

    def start_counter(self):
        pass

    def stop_counter(self):
        pass

    ##########################################################
    # INTERNAL UTILITY FUNCTIONS
    ##########################################################
    EP_IN, EP_OUT = 0x81, 0x01
    HEADER_PACKET, HEADER_DATA = 4, 4
    INTERFACE = 0

    def send_request(self, cmd, request):
        if len(request) + self.HEADER_PACKET + self.HEADER_DATA > 255:
            raise ValueError('Request too long (%d bytes)' % (len(request) + self.HEADER_PACKET + self.HEADER_DATA))

        buf = bytearray(b"\x00\x01\x00\x00\x00\x00\x01\x00")
        buf[3] = self.HEADER_PACKET + self.HEADER_DATA + len(request)
        buf[5] = self.HEADER_DATA + len(request)
        buf[7] = cmd
        buf += request

        assert self.device.write(self.EP_OUT, buf, self.INTERFACE) == len(buf)

        ret = bytearray(self.device.read(self.EP_IN, len(buf), self.INTERFACE))

        return ret[self.HEADER_PACKET:]


    def packet_matches(self, actual, expected, mask):
        if len(actual) != len(expected):
            print(actual.hex(" "))
            print(expected.hex(" "))
            print(mask.hex(" "))
            raise ValueError('Protocol error - invalid response length %d' % len(actual))

        for b, e, m in zip(actual, expected, mask):
            if (b & m) != (e & m):
                raise ValueError("""Protocol error - invalid response
                actual:   %s
                expected: %s
                mask:     %s
                """ % (repr(actual), repr(expected), repr(mask)))


    def check_valid_port_pin(self, port=None, pin=None):
        if port is not None and port not in range(3):
            raise IndexError("Port number is not valid!")
        if pin is not None and port not in range(8):
            raise IndexError("Pin number is not valid!")


    def check_valid_mask(self, mask):
        if mask is not None and mask not in range(256):
            raise ValueError("Mask is not valid!")


    def release_interface(self):
        """
        Free all resources, then the device can be used once again
        """
        if self.device.is_kernel_driver_active(self.interface_number):
            self.device.detach_kernel_driver(self.interface_number)
        usb.util.release_interface(self.device, self.INTERFACE)
        usb.util.dispose_resources(self.device)
        self.device.reset()
        self.device = None


#USAGE EXAMPLE
if __name__ == "__main__":
    dev = get_adapter()

    if not dev:
        raise Exception("No device found")

    dev.set_io_mode(0b11111111, 0b11111111, 0b00000000)

    dev.write_port(0, 0b11001100)
    dev.write_port(1, 0b10101010)

    print(bin(dev.read_port(2)))

    ret = dev.set_io_mode(0, 255, 0)      # set all pins between 3-6 & 27-30 as output pins
    # example has special focus on port 3 & 30, the values ot the others are all set to high
    # bitmask: 247: 1111 0111
    # 27: 1     low byte
    # 28: 1     
    # 29: 1     
    # 30: 0
    #  6: 1    
    #  5: 1     
    #  4: 1     
    #  3: 1     high byte

    ret = dev.write_port(1, 0)  # both zero
    print(dev.read_port(1))

    ret = dev.write_port(1, 247)  # 30 low
    print(dev.read_port(1))

    ret = dev.write_port(1, 127)  # 3 low
    print(dev.read_port(1))

    ret = dev.write_port(1, 247)  # 30 low
    print(dev.read_port(1))

    ret = dev.write_port(1, 127)  # 3 low
    print(dev.read_port(1))

    ret = dev.write_port(1, 0)  # both zero
    print(dev.read_port(1))

    ret = dev.write_port(1, 255)  # both high
    print(dev.read_port(1))

    dev.release_interface()     # clean exit, allows direct reuse without to replug the ni6501
    del dev
