cmake_minimum_required(VERSION 3.10)

project("substring")

file(GLOB SOURCES "10234900421hw_substring.c")

add_executable(${PROJECT_NAME} ${SOURCES})