// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from turtlebot3_msgs:msg/Sound.idl
// generated code does not contain a copyright notice
#ifndef TURTLEBOT3_MSGS__MSG__DETAIL__SOUND__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define TURTLEBOT3_MSGS__MSG__DETAIL__SOUND__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "turtlebot3_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "turtlebot3_msgs/msg/detail/sound__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_turtlebot3_msgs
bool cdr_serialize_turtlebot3_msgs__msg__Sound(
  const turtlebot3_msgs__msg__Sound * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_turtlebot3_msgs
bool cdr_deserialize_turtlebot3_msgs__msg__Sound(
  eprosima::fastcdr::Cdr &,
  turtlebot3_msgs__msg__Sound * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_turtlebot3_msgs
size_t get_serialized_size_turtlebot3_msgs__msg__Sound(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_turtlebot3_msgs
size_t max_serialized_size_turtlebot3_msgs__msg__Sound(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_turtlebot3_msgs
bool cdr_serialize_key_turtlebot3_msgs__msg__Sound(
  const turtlebot3_msgs__msg__Sound * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_turtlebot3_msgs
size_t get_serialized_size_key_turtlebot3_msgs__msg__Sound(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_turtlebot3_msgs
size_t max_serialized_size_key_turtlebot3_msgs__msg__Sound(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_turtlebot3_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, turtlebot3_msgs, msg, Sound)();

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT3_MSGS__MSG__DETAIL__SOUND__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
