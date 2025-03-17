import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    world_file = os.path.join(get_package_share_directory('turtlebot_simulation'), 'worlds', 'custom_maze.world')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')),
            launch_arguments={'world': world_file}.items(),
        ),
        ExecuteProcess(
            cmd=['ros2', 'launch', 'object_detection_pkg', 'object_detection_launch.py'],
            output='screen'
        )
    ])
