cmake_minimum_required(VERSION 3.10)

project(Adder)

file(GLOB SOURCES "hw_*.c")

add_executable(Adder ${SOURCES})