# C++ SBC Binary Format driver

A header-only library for the SBC binary format.

To install this library, there are two options:

1. Copy everything inside the "include" folder into your project include folder.
   Done!
2. Clone this github repository anywhere in your project and in your
   "CMakeLists.txt" add a line called `add_subdirectory
   (LOCATION_OF_THIS_LIBRARY)`. Then, in `target_link_libraries` add
   `RedDigitizer++::RedDigitizer++`. Done!

# Examples

There are tests (or examples) inside "test/source/basic_test.cpp" that can be compiled to test the library works. Its original intent is to make sure the code can compile in your computer and actually run with little to no bugs.

It uses a library called doctest, so it has some code that might look unusual.

# TODO:

* Better examples.
* Complete tests.
* Bug hunt, are there bugs?