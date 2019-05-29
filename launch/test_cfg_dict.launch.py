import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    composable_node = ComposableNode(package='test', node_plugin='Test',
    parameters=[{"a_string": "Hello world"}])
    container = ComposableNodeContainer(
            node_name='test_container',
            node_namespace='camera',
            package='rclcpp_components',
            node_executable='component_container',
            composable_node_descriptions=[composable_node],
            output='screen'
    )

    return launch.LaunchDescription([container])
