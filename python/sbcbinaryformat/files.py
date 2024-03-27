"""
Contains two classes:

* Streamer: which reads a file and either creates a streamer
  or saved everything to RAM. No multiprocessing features.
* Writer: which creates SBC binary files given the passed parameters.
Very simplistic and does not have any multiprocessing features.
"""
import sys
import os

import numpy as np


class Streamer:
    """
        This class specializes in opening and managing a sbc-binary file.
        If a file is too  big to save into RAM, this code will manage the
        reading into a more tolerable internal buffer.
    """
    def __init__(self, file, block_size=65536, max_size=1000):
        """
        :param file: File location and name
        :param blocksize: Size in lines of the internal buffer
        :param max_size: Max size of the file that will be directly loaded
                         into RAM. Beyond this value the streamer will default
                         to a block style of reading.
        :raises OSError: if Endianess is not supported, if the header is
                         not consistent or contents do not match the header.
        """
        self.__data = None
        self.__binary_data = None
        self.system_edianess = sys.byteorder
        self.file_size = os.path.getsize(file) / 1e6
        self.is_all_in_ram = self.file_size < max_size

        # This will throw if the file is not found
        self.file_resource = open(file, "rb")

        # Read the constants from the file
        # First its Endianess
        file_endianess = np.fromfile(self.file_resource,
                                     dtype=np.uint32, count=1)

        if file_endianess == 0x01020304:
            self.file_endianess = "little"
        elif file_endianess == 0x04030201:
            self.file_endianess = "big"
        else:
            raise OSError(f"Endianess not supported: {file_endianess}")

        # Now the length of the header
        self.header_length = np.fromfile(self.file_resource,
                                         dtype=np.uint16, count=1)[0]

        header = self.file_resource.read(self.header_length).decode('ascii')
        header = header.split(';')

        if (len(header) - 1) % 3 != 0:
            raise OSError(f"The number of items found in the header should \
                always come in multiples of 3. It is {len(header) - 1}")

        self.num_columns = int(len(header) / 3)
        header = np.resize(header, (self.num_columns, 3))

        self.columns = header[:, 0]
        self.dtypes = [sbcstring_to_type(type_s, self.file_endianess)
                       for type_s in header[:, 1]]
        self.sizes = [[int(lenght) for lenght in length.split(',')]
                      for length in header[:, 2]]

        self.expected_num_elems = np.fromfile(self.file_resource,
                                              dtype=np.int32, count=1)[0]

        # 4 for endianess, 2 for header length and 4 for num elems
        self.header_size_in_bytes = self.header_length + 10
        # Address in the file where the data starts
        self.__start_data = self.header_size_in_bytes
        # Address in the file where data ends
        self.__end_data = self.file_size

        header_size_in_megbytes = self.header_size_in_bytes*1e-6
        # We need to calculate how many elements are in the file
        bytes_each = [dtype.itemsize*np.prod(sizes) for i, (dtype, sizes)
                      in enumerate(zip(self.dtypes, self.sizes))]

        self.line_size_in_bytes = np.sum(bytes_each)
        line_size_in_megbytes = self.line_size_in_bytes*1.0e-6

        self.num_elems = self.file_size - header_size_in_megbytes
        # TODO(Any): this check has a lot of flaws... float rounding errors
        # mess this up. Solution: check to integers and deal with bytes
        if self.num_elems % line_size_in_megbytes > 1e-3:
            raise OSError(f"""After doing the math, the remaining file is
not evenly distributed by the given parameters.
Header or data written incorrectly.
- Header size = {header_size_in_megbytes} MB.
- File size = {self.file_size } MB.
- Expected line size = {line_size_in_megbytes} MB""")

        self.num_elems = int(self.num_elems / line_size_in_megbytes)

        if self.expected_num_elems != 0:
            if self.num_elems != self.expected_num_elems:
                raise OSError(f"Expected number of elements in file, \
                                {self.expected_num_elems}, does not match \
                                the calculated number of element in file: \
                                {self.num_elems}")

        if (block_size * line_size_in_megbytes) > max_size:
            print(f"Warning: Block size  \
({block_size * line_size_in_megbytes}MB) is bigger than the amount of memory \
this streamer can allocate which is equal to {max_size}MB. \
Reducing until reasonable.")

        if self.is_all_in_ram:
            self.block_size = self.num_elems
        else:
            self.block_size = block_size
            while (self.block_size * line_size_in_megbytes) > max_size:
                self.block_size = int(0.5*self.block_size)

            print(f"Final block size = {self.block_size}")

        self.__create_df()

        self.__start_line_in_memory = 0
        self.__end_line_in_memory = 0
        self.__current_line = 0
        self.__load_data()

        for column in self.columns:
            setattr(self, column, self.__data[column])

    def __enter__(self):
        """
        This allows the use of with()
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        This allows the use of with() and properly closes the resources
        """
        self.file_resource.close()

    def __process_line_data(self, i):
        """
        Helper function to process the data and save it to the
        allocated memory
        """
        position_in_array = 0
        for name, dtype, sizes in zip(self.columns, self.dtypes, self.sizes):
            length = dtype.itemsize*np.prod(sizes)
            s_index = position_in_array + i*self.line_size_in_bytes
            e_index = length + s_index
            if len(sizes) > 1:
                self.__data[name][i] \
                    = self.__binary_data[s_index:e_index].view(dtype).reshape(sizes)
            elif len(sizes) == 1:
                self.__data[name][i] \
                    = self.__binary_data[s_index:e_index].view(dtype)

            position_in_array += length

    def __create_df(self):
        """
        Here is where we allocate the memory for this streamer
        """
        df_dtypes = {}
        if self.__binary_data is None:
            self.__binary_data = np.zeros(
                self.line_size_in_bytes*self.block_size, dtype=np.uint8)

        if self.__data is None:
            self.__data = dict.fromkeys(self.columns)
            # self.__data = pd.DataFrame()
            for name, dtype, sizes in zip(self.columns, self.dtypes, self.sizes):
                self.__data[name] = ()
                if len(sizes) > 1:
                    df_dtypes[name] = list
                    sizes = np.append(self.block_size, sizes)
                    self.__data[name] = np.zeros(sizes, dtype=dtype)
                elif len(sizes) == 1:
                    df_dtypes[name] = dtype
                    self.__data[name] = np.zeros((self.block_size, sizes[0]),
                                                 dtype=dtype)

    def __get_row(self, i):
        return i*self.line_size_in_bytes + self.header_size_in_bytes

    def __set_line_file(self, i):
        self.file_resource.seek(self.__get_row(i))

    def __load_data(self):
        """
            Loads data at self.__current_line
        """
        self.__set_line_file(self.__current_line)
        start_in_bytes = self.file_resource.tell()

        self.__binary_data = np.fromfile(self.file_resource, dtype=np.uint8,
                                         count=self.line_size_in_bytes
                                         * self.block_size)

        end_in_bytes = self.file_resource.tell()

        lines_moved = end_in_bytes - start_in_bytes
        lines_moved = lines_moved / self.line_size_in_bytes

        if int(lines_moved) != lines_moved:
            raise ValueError(f'File did not moved an integer value of \
{self.line_size_in_bytes}')

        lines_moved = int(lines_moved)

        self.__start_line_in_memory = self.__current_line
        self.__end_line_in_memory += lines_moved
        for i in range(lines_moved):
            self.__process_line_data(i)

    def __len__(self):
        return self.num_elems

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_line == self.num_elems:
            self.__current_line = 0
            raise StopIteration

        return self.__getitem__(self.__current_line)

    def __getitem(self, i):
        self.__current_line = i
        if self.__current_line >= self.__end_line_in_memory or \
           self.__current_line < self.__start_line_in_memory:
            # if outside these limits, we dont have that data in memory
            # we need to load it from the file
            print("Loading data...")
            self.__load_data()

        # now, we load the data
        out = dict.fromkeys(self.columns)
        internal_index = self.__current_line - self.__start_line_in_memory

        for column in self.columns:
            out[column] = self.__data[column][internal_index]

        self.__current_line += 1
        return out

    def __getitem__(self, indexes):
        if isinstance(indexes, (int, np.integer)):
            return self.__getitem(indexes)
        if isinstance(indexes, str):
            return self.__data[indexes]

        return np.array([self.__getitem(i) for i in indexes])


class Writer:
    """
    SBC Binary Header description:
     * Header of a binary format is divided in 4 parts:
     * 1.- Edianess            - always 4 bits long (uint32_t)
     * 2.- Data Header size    - always 2 bits long (uint16_t)
     * and is the length of the next bit of data
     * 3.- Data Header         - is data header long.
     * Contains the structure of each line. It is always found as a raw
     * string in the form "{name_col};{type_col};{size1},{size2}...;...;
     * Cannot be longer than 65536 bytes.
     * 4.- Number of lines     - always 4 bits long (int32_t)
     * Number of lines in the file. If 0, it is indefinitely long.
    """

    def __init__(self, file_name, columns_names, dtypes, sizes):
        self.file_name = file_name
        self.num_elems_saved = 0
        self.system_endianess = sys.byteorder

        if len(columns_names) != len(dtypes):
            raise ValueError("columns names and dtypes should be of the \
same length")

        # if does not exist OR its size is 0, we create the header
        if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
            self.__create_header(file_name, columns_names, dtypes, sizes)
        # Otherwise, we read the header and check whenever is compatible with
        # current parameters
        else:
            if not self.__has_compatible_header(file_name, columns_names,
                                                dtypes, sizes):
                raise ValueError(f"Header of already existing file must match \
columns_names ({columns_names}), dtypes ({dtypes}), \
and sizes ({sizes})")

            self.file_resource = open(file_name, 'ab')

    def __len__(self):
        return self.num_elems_saved

    def __enter__(self):
        """
            This allows the use of with()
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
            This allows the use of with() and properly closes the resources
        """
        self.file_resource.close()

    def write(self, data_line):
        """
        Write data_line to the file.

        :raises ValueError: if data_line is not a dictionary, the keys or
        lengths do not match the columns of the file.
        """
        if not isinstance(data_line, dict):
            raise ValueError("data must be a dictionary")

        if (list(data_line) != self.columns).all():
            raise ValueError(f'Data keys must match the column types. This  \
                file columns names : {self.columns}, the data provided keys : \
                {list(data_line)}')

        sizes = [list(np.array(value).shape) for _, value in data_line.items()]
        if not self.__check_sizes(sizes):
            raise ValueError("Data passed is not the length of the \
expected sizes")

        for column_name, dtype, _ in zip(self.columns, self.dtypes, self.sizes):
            np.array(data_line[column_name],
                     dtype=dtype).tofile(self.file_resource)

    def __create_header(self, file_name, columns_names, dtypes, sizes):
        self.file_resource = open(file_name, 'wb')
        # first endianess
        np.array(0x01020304, dtype='u4').tofile(self.file_resource)

        # then we need two things: the header and its length
        self.header = ""
        for column_name, dtype, size in zip(columns_names, dtypes, sizes):
            header_str = ""
            if isinstance(size, int):
                header_str = f"{size}"
            else:
                for i, size_i in enumerate(size):
                    if i == 0:
                        header_str += f"{size_i}"
                    else:
                        header_str += f",{size_i}"

            self.header += f"{column_name};{type_to_sbcstring(dtype)};{header_str};"

        self.header_length = len(self.header)
        np.array(self.header_length, dtype='u2').tofile(self.file_resource)

        self.file_resource.write(self.header.encode('ascii'))

        np.array(0, dtype='i4').tofile(self.file_resource)

        self.columns = np.array(columns_names)
        self.dtypes = np.array(dtypes)
        self.sizes = sizes

    def __has_compatible_header(self, file_name, columns_names, dtypes, sizes):
        # open the file for read only
        with open(file_name, "rb") as file:
            file_endianess = np.fromfile(file,
                                         dtype=np.uint32, count=1)[0]

            if file_endianess not in (0x1020304, 0x4030201):
                raise OSError(f"Endianess not supported: 0x{file_endianess:X}")

            self.correct_for_endian = False
            if (file_endianess == 0x04030201
                and self.system_endianess == 'little') \
               or (file_endianess == 0x01020304
                   and self.system_endianess == 'big'):
                self.correct_for_endian = True

            # Now the length of the header
            self.header_length = np.fromfile(file,
                                             dtype=np.uint16,
                                             count=1)[0]

            print(self.header_length)

            header = file.read(self.header_length).decode('ascii')
            header = header.split(';')

            if (len(header) - 1) % 3 != 0:
                raise OSError(f"The number of items found in the header \
                    should always come in multiples of 3. It is \
                    {len(header) - 1}")

            self.num_columns = int(len(header) / 3)
            header = np.resize(header, (self.num_columns, 3))

            self.columns = header[:, 0]

            if not (self.columns == columns_names).all():
                print(f"SBCWriter: columns did not match {self.columns} and \
                    {columns_names}")
                return False

            self.dtypes = np.array([sbcstring_to_type(type_s, file)
                           for type_s in header[:, 1]])

            np_dtypes = [np.dtype(dtype) for dtype in dtypes]
            if not (self.dtypes == np_dtypes).all():
                print("SBCWriter: dtypes did not match")
                return False

            self.sizes = [[int(lenght) for lenght in length.split(',')]
                          for length in header[:, 2]]

            if not self.__check_sizes(sizes):
                print("SBCWriter: sizes did not match")
                return False

            self.num_elems = np.fromfile(file,
                                         dtype=np.int32,
                                         count=1)[0]
        # If it passed all the test, then they match!
        return True

    def __check_sizes(self, sizes):
        return np.array([(np.array(x) == y).all() \
                         for x, y in zip(self.sizes, sizes)]).all()


def sbcstring_to_type(type_str, endianess):
    out_type_str = ""
    if endianess == 'little':
        out_type_str += '<'
    elif endianess == 'big':
        out_type_str += '>'

    string_to_type = {'char': 'i1',
                      'int8': 'i1',
                      'int16': 'i2',
                      'int32': 'i4',
                      'int64': 'i8',
                      'uint8': 'u1',
                      'uint16': 'u2',
                      'uint32': 'u4',
                      'uint64': 'u8',
                      'single': 'f',
                      'float32': 'f',
                      'double': 'd',
                      'float64': 'd',
                      'float128': 'f16'}

    return np.dtype(out_type_str+string_to_type[type_str])


def type_to_sbcstring(sbc_type_str):
    string_to_type = {'i1': 'int8',
                      'i2': 'int16',
                      'i4': 'int32',
                      'i8': 'int64',
                      'u1': 'uint8',
                      'u2': 'uint16',
                      'u4': 'uint32',
                      'u8': 'uint64',
                      'f': 'float32',
                      'd': 'double',
                      'f16': 'float128'}

    return string_to_type[sbc_type_str]

# with SBCWriteBinary("test.bin", ("a", "b"), ('i1', 'i2'), [[1], [1]]) as out:
#     print(out.columns, out.dtypes, out.sizes)
#     out.write({'a': [0], 'b': [2]})

# with SBCReadBinaryStreamer('test.bin') as data:
#     print(data.columns, data.dtypes, data.sizes)
