import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    composable_node = ComposableNode(package='test', node_plugin='Test',
    parameters=[get_package_share_directory('test')+"/cfg/demo.yaml"])
    container = ComposableNodeContainer(
            node_name='test_container',
            node_namespace='camera',
            package='rclcpp_components',
            node_executable='component_container',
            composable_node_descriptions=[composable_node],
            output='screen'
    )

    return launch.LaunchDescription([container])
