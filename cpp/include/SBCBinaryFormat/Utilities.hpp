/*
 * Author: Hector Hawley Herrera
 *
 * This file contains a bunch of C++20 utilities used through all of the files
 * to do some template magic.
 *
 * Examples: a struct that turns strings into a template parameter, a
 * type container, and integral type to sbc type string
 *
 * */
#ifndef SBC_BINARYFORMAT_TOOLS_H
#define SBC_BINARYFORMAT_TOOLS_H
#pragma once

// C STD includes
// C 3rd party includes
// C++ STD includes
#include <type_traits>
#include <string_view>
#include <algorithm>
#include <array>

// C++ 3rd party includes
// my includes

namespace SBC::BinaryFormat::Tools {
// The BinaryFormat only accepts arithmetic pointers.
// ex: const char* returns true
//      std::string return false
//      double* return true;
template<typename T>
concept is_arithmetic_ptr = std::is_arithmetic_v<
                             std::remove_cvref_t<
                             std::remove_pointer_t<T>>> and not std::is_pointer_v<T>;

template<typename... T>
concept is_arithmetic_ptr_unpack = requires(T x) {
    (... and is_arithmetic_ptr<T>);
};

template<typename T>
requires is_arithmetic_ptr<T>
constexpr static std::string_view type_to_string() {
    // We get the most pure essence of T: no consts, no references,
    // and no []
    using T_no_const = std::remove_pointer_t<std::remove_all_extents_t<
            std::remove_reference_t<std::remove_const_t<T>>>>;
    if constexpr (std::is_same_v<T_no_const, char>) {
        return "char";
    } else if constexpr (std::is_same_v<T_no_const, uint8_t>) {
        return "uint8";
    } else if constexpr (std::is_same_v<T_no_const, uint16_t>) {
        return "uint16";
    } else if constexpr (std::is_same_v<T_no_const, uint32_t>) {
        return "uint32";
    } else if constexpr (std::is_same_v<T_no_const, uint64_t>) {
        return "uint64";
    } else if constexpr (std::is_same_v<T_no_const, int8_t>) {
        return "int8";
    } else if constexpr (std::is_same_v<T_no_const, int16_t>) {
        return "int16";
    } else if constexpr (std::is_same_v<T_no_const, int32_t>) {
        return "int32";
    } else if constexpr (std::is_same_v<T_no_const, int64_t>) {
        return "int64";
    } else if constexpr (std::is_same_v<T_no_const, float>) {
        return "single";
    } else if constexpr (std::is_same_v<T_no_const, double>) {
        return "double";
    } else if constexpr (std::is_same_v<T_no_const, long double>) {
        return "float128";
    }
    // TODO(All): maybe the default should be uint32? or no default?
}

template<size_t N>
struct ColumnName {
    constexpr ColumnName(const char (&str)[N]) {
        // The explicit breaks this, maybe we can find a more suitable solution?
        std::copy_n(str, N, value);
    }

    char value[N];
};

template<ColumnName... column_names>
struct ColumnNames {
    static constexpr auto names = std::to_array({column_names.value...});
    static constexpr std::size_t size = names.size();
};

template<template<class> class container, typename... T>
struct ColumnTypes {
    using types = std::tuple<T...>;
    static constexpr std::size_t size = sizeof...(T);
    static constexpr auto type_sizes = std::to_array({sizeof(T)...});
    static constexpr auto type_str = std::to_array({type_to_string<T>()...});
    using data_type = std::tuple<container<T>...>;

    constexpr ColumnTypes() {}
};

template<typename... T>
struct STDVectorColumnTypes : public ColumnTypes<std::vector, T...> {};


} // namespace SBC::BinaryFormat::Tools

#endif //SBC_BINARYFORMAT_TOOLS_H
