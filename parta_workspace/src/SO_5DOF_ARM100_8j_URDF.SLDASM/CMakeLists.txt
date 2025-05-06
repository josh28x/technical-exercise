cmake_minimum_required(VERSION 2.8.3)

project(SO_5DOF_ARM100_8j_URDF.SLDASM)

find_package(ament_cmake REQUIRED)

catkin_package()

find_package(roslaunch)

install(DIRECTORY config launch meshes urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
