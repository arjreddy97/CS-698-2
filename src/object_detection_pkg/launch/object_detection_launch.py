import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    config_file = os.path.join(get_package_share_directory('object_detection_pkg'), 'config', 'object_detection_params.yaml')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'run', 'object_detection_pkg', 'object_detection_node', '--ros-args', '--params-file', config_file],
            output='screen'
        )
    ])
