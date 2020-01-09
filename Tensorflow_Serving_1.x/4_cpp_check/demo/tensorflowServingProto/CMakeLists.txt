project(tensorflowServingProto)
################################################################################
# Include paths of header files 
################################################################################
set(LIBCOMMON_INCLUDES
    ${CMAKE_CURRENT_SOURCE_DIR}/inc
    ${GLOB_PY_INCLUDE}
)
include_directories(${LIBCOMMON_INCLUDES})

################################################################################
# Configure source files
################################################################################
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/src CURRENT_SOURCES)
    

if(BUILD_SHARED_LIBS)
    add_library(tensorflowServingProto SHARED ${CURRENT_SOURCES} )
    target_link_libraries(tensorflowServingProto ${TFS_USE_LIB})
else()
    add_library(tensorflowServingProto STATIC ${CURRENT_SOURCES} )
    target_link_libraries(tensorflowServingProto ${TFS_USE_LIB})
endif()    

