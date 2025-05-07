cmake_minimum_required(VERSION 3.5)

project(so_5dof_arm100_8j_urdf_sldasm)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch meshes urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
