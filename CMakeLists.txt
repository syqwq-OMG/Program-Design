cmake_minimum_required(VERSION 3.10)

project("")

file(GLOB SOURCES "*.c")

add_executable(${PROJECT_NAME} ${SOURCES})