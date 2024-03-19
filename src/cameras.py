import paramiko as pm

class Cameras:
    def __init__(self, main_window):
        self.main_window = main_window
        self.config = main_window.config_class.config
        self.logger = logging.getLogger(__name__)
        self.logger.addHandler(logging.StreamHandler())
        os.putenv("PATH", "/home/sbc/packages")
        self.client = pm.client.SSHClient()
        self.client.set_missing_host_key_policy(pm.AutoAddPolicy())

        self.logger.debug("Cameras class initialized.")

    def connect_camera(self, host, command):
        self.client.connect(host, username=username)
        _stdin, _stdout, _stderr = client.exec_command(command)
        print(_stdout.read().decode())
        client.close()
