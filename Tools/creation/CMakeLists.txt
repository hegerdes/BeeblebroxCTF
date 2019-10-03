###############################################################################
# Declare the minimum cmake version required
###############################################################################
cmake_minimum_required(VERSION 3.0.2)

project(CTF_TOOLS)


###############################################################################
# With cmake we can define additional compiler flags for different 
# configurations. CMAKE_CXX_FLAGS are for the default case. The debug config
# can be used to generate debug symbols for gdb. The release option uses
# special optimization flags
###############################################################################

set( CMAKE_CXX_FLAGS         "-std=c++11 -O3 -Wall" )
set( CMAKE_CXX_FLAGS_RELEASE "-O3 -msse3 -Wno-deprecated-declarations -Wno-unused -Wcpp" )
set( CMAKE_CXX_FLAGS_DEBUG   "-g -Wall" )

###############################################################################
# Find required libraries.Right now we need glut and OpenGL. The required 
# options forces this packages to be present. For non-mandatory packages you 
# can leave this flag out. The can then check if they were found by using
# IF(OpenGL_found) etc.
###############################################################################

include_directories(${CMAKE_SOURCE_DIR})

set(Boost_USE_MULTITHREADED     ON)

find_package( Boost 1.54
    COMPONENTS
    program_options
    filesystem
    system
    thread
    serialization
    REQUIRED )

link_directories(${Boost_LIBRARY_DIR})
include_directories(${Boost_INCLUDE_DIRS})
add_definitions(${Boost_LIB_DIAGNOSTIC_DEFINITIONS})

find_package (Threads)

set(ADDER_SOURCES
    PrefixAdder.cpp
)

set(BINWRITER_SOURCES
    BinaryWriter.cpp
)

set(PINFORPW_SOURCES
    PinForPW.cpp
)

set(SERVER1_SOURCES
    Server1.cpp
)

set(SERVER2_SOURCES
Server2.cpp
)

set(CLIENT_SOURCES
    Client.cpp
)
set(TOOLS_DEPENDS     
    ${Boost_PROGRAM_OPTIONS_LIBRARY}
    ${Boost_SYSTEM_LIBRARY}
    ${Boost_THREAD_LIBRARY}
    ${Boost_FILESYSTEM_LIBRARY}
    ${CMAKE_THREAD_LIBS_INIT}
)

###############################################################################
# The executable fpr our project
###############################################################################

add_executable(PrefixAdder ${ADDER_SOURCES} )
add_executable(PW-Safe ${PINFORPW_SOURCES} )
add_executable(BinaryWriter ${BINWRITER_SOURCES} )
add_executable(Server1 ${SERVER1_SOURCES} )
add_executable(Server2 ${SERVER2_SOURCES} )
add_executable(Client ${CLIENT_SOURCES} )

###############################################################################
# External library dependencys
###############################################################################

message(STATUS)
target_link_libraries(PrefixAdder ${TOOLS_DEPENDS})
target_link_libraries(PW-Safe ${TOOLS_DEPENDS})
target_link_libraries(BinaryWriter ${TOOLS_DEPENDS})
target_link_libraries(Server1 ${TOOLS_DEPENDS})
target_link_libraries(Server2 ${TOOLS_DEPENDS})
target_link_libraries(Client ${TOOLS_DEPENDS})
