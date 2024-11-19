cmake_minimum_required(VERSION 3.10)

project("chem_data")

file(GLOB SOURCES "*.c")

add_executable(${PROJECT_NAME} ${SOURCES})