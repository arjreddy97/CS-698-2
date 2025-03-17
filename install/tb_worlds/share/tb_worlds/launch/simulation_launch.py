import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    world_file = os.path.join(get_package_share_directory('turtlebot3_simulation'), 'worlds', 'custom_maze.world')

    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='gzserver',
            arguments=[world_file],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='gzclient',
            output='screen'
        ),
        Node(
            package='turtlebot3_gazebo',
            executable='spawn_model',
            arguments=['-entity', 'turtlebot3', '-x', '0', '-y', '0', '-z', '0.1'],
            output='screen'
        )
    ])
