project(ServingTest)
################################################################################
# Include paths of header files 
################################################################################
set(LIBPipelineElementPulmonaryNodulePostProc_INCLUDES
	${SOURCECODE_PATH}/tensorflowServingProto/inc
	${GLOB_PY_INCLUDE}
)
include_directories(${LIBPipelineElementPulmonaryNodulePostProc_INCLUDES})


################################################################################
# unit test
################################################################################
add_executable(ServingTestUT 
    ${CMAKE_CURRENT_SOURCE_DIR}/ServingTest.cpp)
target_link_libraries(ServingTestUT tensorflowServingProto ${TFS_USE_LIB})
