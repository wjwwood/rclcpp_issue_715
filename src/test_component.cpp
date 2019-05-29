#include <test/test_component.hpp>

Test::Test(const rclcpp::NodeOptions options)
: Node("test_node_otto", options) {
    std::cout << "test node" << std::endl;

    declare_parameter<std::string>("a_string", "...");

    std::string message;
    get_parameter_or<std::string>("a_string", message, "...");

    std::cout << "message: " << message << std::endl;
}

#include <rclcpp_components/register_node_macro.hpp>
RCLCPP_COMPONENTS_REGISTER_NODE(Test)