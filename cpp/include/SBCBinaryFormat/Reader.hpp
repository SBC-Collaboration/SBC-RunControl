#ifndef SBC_BINARYFORMAT_READER_H
#define SBC_BINARYFORMAT_READER_H
#pragma once

// C STD includes
// C 3rd party includes
// C++ STD includes
#include <fstream>
#include <cinttypes>
#include <functional>
#include <type_traits>
#include <filesystem>
#include <stdexcept>
#include <ranges>
#include <cstring>
#include <string>
#include <iostream>
#include <bit>
#include <numeric>
#include <span>

// C++ 3rd party includes
// my includes
#include "SBCBinaryFormat/Utilities.hpp"

namespace SBC::BinaryFormat {

struct StreamerTraits {
    using index_type = std::size_t;
    // The max size of any dimension read from DynamicStreamer
    constexpr static uint32_t MAX_BUFFER_SIZE = 32000;

    constexpr static uint64_t MAX_FILE_SIZE_RAM_MB = 8000; // MB

    constexpr static double FILE_TOLERANCE = 1e-3;
};

template<typename Types,
         typename ColumnNames,
         typename Traits = StreamerTraits>
class DynamicStreamer {
    using index_type = Traits::index_type;

    // These guys are defined by their types
    static Types _types;
    static ColumnNames _column_names;

    using data_type = Types::data_type;

    // Checks Types and Columns names have the same size
    static_assert(_types.size == _column_names.size);

    std::string _file_name;
    std::fstream _stream;
    bool _swap_buffer = false;

    bool _is_all_in_ram = false;
    // This should be a tuple of vectors<T>...
    // where all our dynamically allocated memory should be.
    // Note: this data is UNROLLED. In other words: only 1 dimensionality to
    // the arrays. The sizes and dimensions are stored in the vectors below
    data_type _data;
    std::vector<char> _data_buffer;

    // Sizes of each dimension of the data vector: read from the file.
    std::vector<index_type> _type_sizes;
    // Pseudo-Dimensions of each data vector: read directly from the file.
    std::vector<index_type> _type_dims;

    std::vector<index_type> _type_total_size;
    // Product of all size times the type sizeof in bytes
    std::vector<index_type> _type_total_sizes_in_B;
    // Positions in bytes of each parameter in the line
    std::vector<index_type> _type_offset_in_B;

    std::uintmax_t _file_size_in_B;
    index_type _line_size_in_B = 0;
    index_type _header_size_in_B = 0;
    index_type _num_elements;
    index_type _block_size_in_lines;
    index_type _block_size_in_B;
    index_type _num_blocks;
    index_type _current_block;

    // Helper for the bellow function
    template<std::size_t... I>
    void _allocate_memory_helper(std::index_sequence<I...>) {
        (std::get<I>(_data).resize(_block_size_in_lines * _type_total_size[I]),...);
    }

    // Allocates the data buffers to sizes found in _type_total_sizes_in_B times
    // block size which should be all the memory we need.
    void _allocate_memory() {
        _allocate_memory_helper(std::make_index_sequence<num_columns>{});
    }

    template<size_t I, typename T>
    void _decode_to_vector(T& column, const std::size_t& lines,
                           std::span<const char> data_buffer_span) {
        const auto& offset_in_line_in_B = _type_offset_in_B[I];
        const auto& length = _type_total_sizes_in_B[I];
        const auto& column_size = _type_total_size[I];

        for (std::size_t i = 0; i < lines; i++) {
//            auto curr_data = data_buffer_span.subspan(i*_line_size_in_B + offset_in_line_in_B, length);
            std::memcpy(&column[i*column_size],
                        &data_buffer_span[i*_line_size_in_B+offset_in_line_in_B],
                        length);
        }
    }

    template<std::size_t... I>
    void _decode_buffer_helper(const std::size_t& lines,
                               std::index_sequence<I...>) {
        (_decode_to_vector<I>(std::get<I>(_data), lines, _data_buffer),...);
    }

    void _decode_buffer(const std::size_t& lines) {
        _decode_buffer_helper(lines, std::make_index_sequence<num_columns>{});
    }

    // Helper function to get type T from file
    template<typename T>
    T _get_type() {
        constexpr std::size_t size = sizeof(T);
        std::array<char, size> buff;
        _stream.read(buff.begin(), size);

        if (_swap_buffer) {
            std::reverse(buff.begin(), buff.end());
        }

        T out;
        std::memcpy(&out, buff.begin(), size);
        return out;
    }
 public:
    constexpr static auto sbc_type_strings = Types::type_str;
    constexpr static auto column_names = _column_names.names;
    constexpr static auto type_sizes = Types::type_sizes;
    constexpr static std::size_t num_columns = _types.size;
    constexpr static std::endian system_endian = std::endian::native;
    constexpr static uint32_t system_sbc_endian = 0x01020304;

    explicit DynamicStreamer(std::string_view file_name,
                             const std::size_t& max_size = 1000,
                             const std::size_t& block_size = 65536) :
            _file_name{file_name},
            _block_size_in_lines{block_size}
    {
        // Reads header and verifies it is compatible with the template
        if (not std::filesystem::exists(file_name)) {
            throw std::invalid_argument("File does not exist.");
        }

        if (std::filesystem::is_empty(file_name)) {
            throw std::invalid_argument("File exists but it is empty.");
        }

        _stream.open(_file_name, std::ios::in | std::ofstream::binary);

        if (not _stream.is_open()) {
            throw std::runtime_error("File was not open.");
        }

        _file_size_in_B = std::filesystem::file_size(_file_name);

        std::uintmax_t actual_max_size_in_B =
                max_size > Traits::MAX_FILE_SIZE_RAM_MB ?
                Traits::MAX_FILE_SIZE_RAM_MB : max_size;

        // We transform to Bytes and divide by 2 because memory
        // is split in two buffers: one, the real data. Two, the raw buffer
        // which is the same size of the real data.
        actual_max_size_in_B *= 0.5e6;
        _is_all_in_ram = _file_size_in_B < actual_max_size_in_B;

        uint32_t sbc_file_endian = _get_type<uint32_t>();
        uint16_t header_length = _get_type<uint16_t>();

        _swap_buffer = sbc_file_endian != system_sbc_endian;

        std::vector<char> buff(header_length);
        _stream.read(buff.data(), header_length);
        std::string_view header(buff.data(), header_length);

        auto header_split = _split(header, ";");
        if ((header_split.size() - 1) % 3 != 0) {
            throw std::runtime_error("The number of items found in the header"
                                     "should always come in multiples of 3.");
        }

        if (static_cast<std::size_t>(header_split.size() / 3) != num_columns) {
            throw std::runtime_error("Incompatible number of elements in the "
                                     "header: " + std::string(header));
        }

        for (std::size_t i = 0; i < header_split.size() - 1; i += 3) {
            auto j = static_cast<std::size_t>(i / 3);
            auto column_name = header_split[i];
            auto type = header_split[i + 1];
            auto raw_sizes_str = header_split[i + 2];

            // Checks to see if the header is compatible with what
            // was provided
            if (column_name != column_names[j]) {
                throw std::runtime_error("Incompatible column name: " +
                                         column_name + " with " +
                                         column_names[j] + " at position " +
                                         std::to_string(j));
            }

            auto type_str = std::string(sbc_type_strings[j]);
            if (type != type_str) {
                throw std::runtime_error("Incompatible type: " +
                                         type + " with " +
                                         type_str +
                                         " at position " + std::to_string(j));
            }

            auto sizes_str = _split(raw_sizes_str, ",");
            for(const auto& size_str : sizes_str) {
                index_type size = std::atoi(size_str.c_str());

                if (size == 0) {
                    throw std::runtime_error("Header indicated a size of 0. "
                                             "That is not allowed by the "
                                             "format.");
                }

                if (size > Traits::MAX_BUFFER_SIZE) {
                    throw std::runtime_error("Size of column " + column_name +
                                             " is too big.");
                }

                _type_sizes.emplace_back(size);
            }

            _type_dims.emplace_back(sizes_str.size());
        }

        // Last info to read from the header is the number of lines
        // the file has inside. If its 0, it can be any size
        auto file_num_elements = static_cast<index_type>(_get_type<uint32_t>());

        // Done with header! Time to deal with the data...
        // But first, let's check the file size is a multiple
        // of what we estimated in the header.
        _header_size_in_B = header_length + 10;

        // Routine to find the size of a line in the file.
        index_type offset = 0;
        _line_size_in_B = 0;
        for (index_type i = 0; i < column_names.size(); i++) {
            _type_offset_in_B.emplace_back(_line_size_in_B);

            index_type prod = 1;
            for (index_type dim_j = 0; dim_j < _type_dims[i]; dim_j++) {
                prod *= _type_sizes[dim_j + offset];
            }

            offset += _type_dims[i];
            _line_size_in_B += type_sizes[i]*prod;
            _type_total_size.emplace_back(prod);
            _type_total_sizes_in_B.emplace_back(type_sizes[i]*prod);
        }

        auto data_size = _file_size_in_B - _header_size_in_B;
        if ((data_size % _line_size_in_B) != 0) {
            throw std::runtime_error("After doing the math, the remaining "
                                     "file is not evenly distributed by the "
                                     "given parameters.");
        }

        // Expected number of lines in the file
        _num_elements = static_cast<index_type>(data_size / _line_size_in_B);
        if (file_num_elements != 0) {
            if (_num_elements != file_num_elements) {
                throw std::runtime_error("Number of elements in the file does "
                                         "not match with the estimated one. "
                                         "Maybe a corrupted file?");
            }
        }

        if (_is_all_in_ram) {
            _block_size_in_lines = _num_elements;
        } else {
            // If the file does not fit in RAM, we calculate the best
            // power of 2 for block size that it fits in actual_max_size
            while (_block_size_in_lines*_line_size_in_B > actual_max_size_in_B) {
                _block_size_in_lines /= 2;
            }
        }
        // This holds 1 block of raw data
        _block_size_in_B = _block_size_in_lines*_line_size_in_B;
        _num_blocks = static_cast<index_type>(data_size/_block_size_in_B);
        // Done with header checking, now we can move to allocating data!
        _allocate_memory();

        _data_buffer.reserve(_block_size_in_B);
        // Technically done, but let's load the first block to memory
        // Start at number of blocks so the next function thinks we
        // are at the end of the buffer
        _current_block = _num_blocks;
        load_next_block();
    }

    ~DynamicStreamer() = default;

    // Indicates if all the file line of data are stored all in ram
    bool is_all_in_ram() { return _is_all_in_ram; }
    // Total lines of data found inside the file.
    index_type size() { return _num_elements; }
    // Returns the internal buffer size in bytes
    index_type get_buffer_size() { return _block_size_in_B; }
    // Returns the internal buffer number of lines.
    // Equal to size() if is_all_in_ram() returns true
    index_type get_num_lines() { return _block_size_in_lines;}

    // "Normal" container functions
    // These are meant to work as a "normal" dictionary
    // Returns a tuple of vectors of the elements at i
    data_type at(const index_type& i) {
        auto item_block = static_cast<index_type>(i / (_num_blocks * _block_size_in_lines));
        if (item_block != _current_block) {
            // We load the previous block as load_nex_block will
            // increment _current_block by 1.
            _current_block = item_block - 1;
            load_next_block();
        }

        data_type out_data;
        _copy_to_line(out_data, i % _block_size_in_lines);
        // Check bounds, if beyond: retrieve data. If within, turn i to
        // internal bounds index.
        return out_data;
    }

    template<typename TransformFunc>
    auto at(const index_type& i,
                 TransformFunc&& transform_func) {
        auto index_tuple = at(i);
        return std::apply(transform_func, index_tuple);
    }

    // "Efficient" functions
    // These are more efficient in terms of speed.
    template<size_t I>
    const auto& get() {
        return std::get<I>(_data);
    }

    template<Tools::ColumnName column_name>
    const auto& get() {
        return get<_find_index<column_name>()>();
    }

    void load_next_block() {
        // Here is the deal:
        // _header_size_in_B is the start of the data in file
        // _file_size is the end of the data in file.
        // We load 1 block size worth of memory
        // Except for the last buffer
        _current_block++;
        if (_current_block >= _num_blocks) {
            _current_block = 0;
        }
        // Start of the block position
        std::size_t start = _current_block*_block_size_in_B + \
                            _header_size_in_B;
        _stream.seekg(start);

        // Try to read 1 block size worth of lines
        _stream.read(_data_buffer.data(), _block_size_in_B);
        // The above can "fail". We check how many bytes it actually read
        auto read_bytes = static_cast<std::size_t>(_stream.gcount());
        auto lines = _block_size_in_lines;
        if (read_bytes != _block_size_in_B) {
            // TODO(Any): think what to do here.
        }

        _decode_buffer(lines);
    }

 private:
    template<std::size_t I, typename T>
    void _copy_to_column(T& column, const index_type& block_line) {
        auto data_column = std::get<I>(_data);
        column.resize(_type_total_size[I]);
        for(index_type i = 0; i < _type_total_size[I]; i++) {
            column[i] = data_column[i + block_line];
        }
    }

    // Helper for the bellow function
    template<std::size_t... I>
    void _copy_to_line_helper(data_type& line, const index_type& block_line,
                              std::index_sequence<I...>) {
        (_copy_to_column<I>(std::get<I>(line), block_line),...);
    }

    // Allocates the data buffers to sizes found in _type_total_sizes_in_B times
    // block size which should be all the memory we need.
    void _copy_to_line(data_type& line, const index_type& block_line) {
        _copy_to_line_helper(line, block_line,
                             std::make_index_sequence<num_columns>{});
    }

    // Other functions:

    template<Tools::ColumnName column_name>
    constexpr static std::size_t _find_index() {
        for(std::size_t i = 0; i < column_names.size(); i++) {
            if (column_names[i] == column_name.value) {
                return i;
            }
        }

        throw std::logic_error("Element was not found");
    }

    // This should be a STD library thing...
    // https://stackoverflow.com/questions/14265581/parse-split-a-string-in-c-using-string-delimiter-standard-c
    std::vector<std::string> _split(std::string_view s,
                                    std::string_view delimiter) {
        size_t pos_start = 0, pos_end, delim_len = delimiter.length();
        std::string token;
        std::vector<std::string> res;

        while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
            token = s.substr(pos_start, pos_end - pos_start);
            pos_start = pos_end + delim_len;
            res.push_back(token);
        }

        token = s.substr(pos_start);
        res.push_back(token);
        return res;
    }
};

} // namespace  SBCQueens::Binary

#endif //SBC_BINARYFORMAT_READER_H
