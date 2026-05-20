cmake_minimum_required(VERSION 3.0.2)
project(mokaliks_service)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_service_files(
  FILES
  QueryCategory.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs message_runtime
)

catkin_install_python(PROGRAMS
  scripts/category_server.py
  scripts/category_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
