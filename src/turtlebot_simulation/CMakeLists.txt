cmake_minimum_required(VERSION 3.5)
project(turtlebot_simulation)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(gazebo_ros REQUIRED)

# Install models, worlds, and launch files
install(
    DIRECTORY launch models worlds
    DESTINATION share/${PROJECT_NAME}
)

ament_package()
