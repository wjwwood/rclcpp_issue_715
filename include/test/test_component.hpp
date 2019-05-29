#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"


class Test : public rclcpp::Node {
public:
  explicit Test(const rclcpp::NodeOptions options = rclcpp::NodeOptions());

};
