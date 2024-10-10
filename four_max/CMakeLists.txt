cmake_minimum_required(VERSION 3.10)

project(FOUR_MAX)

file(GLOB SOURCES "*.c")

add_executable(${PROJECT_NAME} ${SOURCES})