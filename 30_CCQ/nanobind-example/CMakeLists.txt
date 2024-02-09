cmake_minimum_required(VERSION 3.15...3.27)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED)
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(array_example_module src/example_pkg/array_example_module.cpp)
nanobind_add_module(struct_example_module src/example_pkg/struct_example_module.cpp)

install(TARGETS array_example_module LIBRARY DESTINATION example_pkg)
install(TARGETS struct_example_module LIBRARY DESTINATION example_pkg)
