//
// Created by Hector Hawley Herrera on 2023-04-26.
//

// C STD includes
// C 3rd party includes
// C++ STD include
// C++ 3rd party includes
#include <doctest/doctest.h>

// my includes
#include "SBCBinaryFormat/Reader.hpp"
#include "SBCBinaryFormat/Writers.hpp"

using namespace SBC::BinaryFormat;

// This struct contains a row of data in the binary data.
struct TestHolder {
    int32_t t;
    double x;
    double y;
    double z;
    std::vector<double> momentum;
};

TEST_CASE("DYNAMIC_READER_TESTS")
{
    // This prepares the code for the column types of the files.
    // Note the last one, despite it being an array, it is still a double.
    using TestTypes = Tools::STDVectorColumnTypes<int32_t, double, double, double, double>;
    // This prepares the code for the column names found within the file.
    using TestColumnNames = Tools::ColumnNames<"t", "x", "y", "z", "momentum">;

    SUBCASE("Common IO errors") {
        // Check for the expected throws
        // File not found
        CHECK_THROWS([&]() {
            DynamicStreamer<TestTypes, TestColumnNames> streamer("data/imaginary.sbc.bin");
        }());

        // File is empty with no header
        CHECK_THROWS([&]() {
            DynamicStreamer<TestTypes, TestColumnNames> streamer("data/empty.sbc.bin");
        }());

        // File is directory
        CHECK_THROWS([&]() {
            DynamicStreamer<TestTypes, TestColumnNames> streamer("data");
        }());
    }

    SUBCASE("Opposite Endianess check") {

    }

    SUBCASE("Bad header checks") {

    }


    SUBCASE("Small good file checks") {
        DynamicStreamer<TestTypes, TestColumnNames> dB("data/test.sbc.bin");

        // There are 129 elements in the file, did the reader found them all?
        CHECK(dB.size() == 129);

//    auto data = streamer.get<"x">();
        auto data = dB.at(0);

        auto data_too = dB.at(0,
          [](std::vector<int32_t> t, std::vector<double> x,
                          std::vector<double> y, std::vector<double> z,
                          std::vector<double> momentum) -> TestHolder
            {
                return TestHolder{.t = t[0], .x = x[0], .y = y[0], .z = z[0],
                                  .momentum{momentum.begin(), momentum.end()}};
            }
        );

        CHECK(data_too.t == 1);
        CHECK(data_too.x == 2.0);
        CHECK(data_too.y == 3.0);
        CHECK(data_too.z == 4.0);
        CHECK(data_too.momentum.size() == 6);
        CHECK(data_too.momentum == std::vector<double>({1.0, 2.0, 4.0, 5.0, 7.0, 8.0}));
    }

    SUBCASE("Big good file checks") {
        
    }

}

TEST_CASE("WRITER_TEST") {
    SUBCASE("Small example") {
        // First, create the writer type with the types of the members
        // between the <...>: only allowed members: integer types (int16_t,
        // int8_t, int32_t, int64_t and their corresponding unsigned types.
        // char, double, and float are also allowed.
        // If it is not allowed, the program won´t compile!
        using TestDW = SBC::BinaryFormat::DynamicWriter<uint16_t, double>;

        // Names and ranks have to be an array where the length is equal
        // to the number of types passed to the writer
        std::array<std::string, 2> names = {"t", "x"};
        std::array<std::size_t, 2> ranks = {1, 2};
        // Size doesnt need to be an array but its length has to be equal
        // to the product of all the members of ranks
        std::vector<std::size_t> sizes = {1, 3, 2};
        // First is the name, then names...
        TestDW writer("out_test.sbc.bin", names, ranks, sizes);

        // The data to save has to be a span (vector, array, ...)
        // of the same underlying type in the same order as it was passed
        // to the writer types
        std::vector<uint16_t> t = {1};
        std::vector<double> x = {3.0, 4.0, 5.0, 6.0, 7.0, 8.0};
        writer.save(t, x);
    }
}