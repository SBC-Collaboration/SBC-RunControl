cmake_minimum_required(VERSION 3.14...3.22)

project(SBCBinaryFormatTests LANGUAGES CXX C)

# ---- Options ----

option(ENABLE_TEST_COVERAGE "Enable test coverage" OFF)
#option(TEST_INSTALLED_VERSION "Test the version found by find_package" OFF)

# --- Import tools ----

include(cmake/tools.cmake)

# ---- Dependencies ----

include(cmake/CPM.cmake)

CPMAddPackage("gh:onqtam/doctest@2.4.8")
CPMAddPackage("gh:TheLartians/Format.cmake@1.7.3")

if(TEST_INSTALLED_VERSION)
    find_package(SBCBinaryFormat REQUIRED)
else()
    CPMAddPackage(NAME SBCBinaryFormat SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/..)
endif()

# ---- Create binary ----

file(GLOB sources CONFIGURE_DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/source/*.cpp)
add_executable(${PROJECT_NAME} ${sources})
target_link_libraries(${PROJECT_NAME} PUBLIC doctest::doctest SBCBinaryFormat::SBCBinaryFormat)
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 20)

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/data/test.sbc.bin DESTINATION
        ${CMAKE_CURRENT_BINARY_DIR}/data)

# enable compiler warnings
if(NOT TEST_INSTALLED_VERSION)
    if(CMAKE_CXX_COMPILER_ID MATCHES "Clang" OR CMAKE_CXX_COMPILER_ID MATCHES "GNU")
        target_compile_options(SBCBinaryFormatTests PUBLIC -Wall -Wpedantic -Wextra)
    elseif(MSVC)
        target_compile_options(SBCBinaryFormatTests PUBLIC /W4 /WX)
        target_compile_definitions(${PROJECT_NAME} PUBLIC DOCTEST_CONFIG_USE_STD_HEADERS)
    endif()
endif()

# ---- Add SipmAnalysisTests ----

enable_testing()

# Note: doctest and similar testing frameworks can automatically configure CMake tests. For other
# testing frameworks add the tests target instead: add_test(NAME ${PROJECT_NAME} COMMAND
# ${PROJECT_NAME})

include(${doctest_SOURCE_DIR}/scripts/cmake/doctest.cmake)
doctest_discover_tests(${PROJECT_NAME})

# ---- code coverage ----

if(ENABLE_TEST_COVERAGE)
    target_compile_options(SBCBinaryFormatTests PUBLIC -O0 -g -fprofile-arcs -ftest-coverage)
    target_link_options(SBCBinaryFormatTests PUBLIC -fprofile-arcs -ftest-coverage)
endif()
