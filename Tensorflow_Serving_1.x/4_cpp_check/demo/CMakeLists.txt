cmake_minimum_required(VERSION 3.8)
project(ServingTestCPP)

SET(SOURCECODE_PATH ${CMAKE_CURRENT_SOURCE_DIR})
# output dir
SET(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/BIN)
SET(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/BIN)

#g++ configuration in linux
set(CMAKE_BUILD_TYPE Release)
set(CMAKE_CXX_FLAGS "$ENV{CXXFLAGS} -std=c++11 -g1 -O3 -Wall -fno-strict-aliasing -fno-omit-frame-pointer -fthreadsafe-statics -fexceptions -frtti -fopenmp")
set(CMAKE_CXX_FLAGS_DEBUG "$ENV{CXXFLAGS} -std=c++11 -g2 -gdwarf-2 -O0 -Wall -fno-strict-aliasing -fno-omit-frame-pointer -fthreadsafe-statics -fexceptions -frtti -fopenmp")
set(ThirdLIB_DIR "/opt/third")
list(APPEND CMAKE_PREFIX_PATH ${ThirdLIB_DIR}/lib/cmake/ITK-4.13)
set(GLOB_PY_INCLUDE
    ${ThirdLIB_DIR}/include/proto_output
    ${ThirdLIB_DIR}/include)

FIND_LIBRARY(GRPC_LIB grpc ${ThirdLIB_DIR}/lib)
message(STATUS "grpc lib path:" ${GRPC_LIB})
if(NOT GRPC_LIB)
    message(FATAL_ERROR "not find the grpc lib" )
endif(NOT GRPC_LIB)    

FIND_LIBRARY(GRPCPP_LIB grpc++ ${ThirdLIB_DIR}/lib)
message(STATUS "grpc++ lib path:" ${GRPCPP_LIB})
if(NOT GRPCPP_LIB)
    message(FATAL_ERROR "not find the grpc++ lib" )
endif(NOT GRPCPP_LIB)    

FIND_LIBRARY(PROTOBUF_LIB protobuf ${ThirdLIB_DIR}/lib)
message(STATUS "protobuf lib path:" ${PROTOBUF_LIB})
if(NOT PROTOBUF_LIB)
    message(FATAL_ERROR "not find the protobuf lib" )
endif(NOT PROTOBUF_LIB)    

FIND_LIBRARY(TENSORFLOW_FRAMEWORK_LIB tensorflow_framework_13 ${ThirdLIB_DIR}/lib)
message(STATUS "tensorflow_framework lib path:" ${TENSORFLOW_FRAMEWORK_LIB})
if(NOT TENSORFLOW_FRAMEWORK_LIB)
    message(FATAL_ERROR "not find the tensorflow_framework lib" )
endif(NOT TENSORFLOW_FRAMEWORK_LIB)    


set(TFS_USE_LIB
	${GRPC_LIB}
	${GRPCPP_LIB}
	${PROTOBUF_LIB}
	${TENSORFLOW_FRAMEWORK_LIB})
	

add_subdirectory(tensorflowServingProto)
add_subdirectory(ServingTest)
	