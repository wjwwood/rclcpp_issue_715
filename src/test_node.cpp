#include <cstdio>
#include <test/test_component.hpp>

int main(int argc, char ** argv)
{
  (void) argc;
  (void) argv;

  printf("hello world test package\n");
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Test>());
  rclcpp::shutdown();
  return 0;
}
