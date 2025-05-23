// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from turtlebot3_msgs:srv/Sound.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "turtlebot3_msgs/srv/sound.h"


#ifndef TURTLEBOT3_MSGS__SRV__DETAIL__SOUND__STRUCT_H_
#define TURTLEBOT3_MSGS__SRV__DETAIL__SOUND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/Sound in the package turtlebot3_msgs.
typedef struct turtlebot3_msgs__srv__Sound_Request
{
  uint8_t value;
} turtlebot3_msgs__srv__Sound_Request;

// Struct for a sequence of turtlebot3_msgs__srv__Sound_Request.
typedef struct turtlebot3_msgs__srv__Sound_Request__Sequence
{
  turtlebot3_msgs__srv__Sound_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot3_msgs__srv__Sound_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'message'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Sound in the package turtlebot3_msgs.
typedef struct turtlebot3_msgs__srv__Sound_Response
{
  bool success;
  rosidl_runtime_c__String message;
} turtlebot3_msgs__srv__Sound_Response;

// Struct for a sequence of turtlebot3_msgs__srv__Sound_Response.
typedef struct turtlebot3_msgs__srv__Sound_Response__Sequence
{
  turtlebot3_msgs__srv__Sound_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot3_msgs__srv__Sound_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  turtlebot3_msgs__srv__Sound_Event__request__MAX_SIZE = 1
};
// response
enum
{
  turtlebot3_msgs__srv__Sound_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/Sound in the package turtlebot3_msgs.
typedef struct turtlebot3_msgs__srv__Sound_Event
{
  service_msgs__msg__ServiceEventInfo info;
  turtlebot3_msgs__srv__Sound_Request__Sequence request;
  turtlebot3_msgs__srv__Sound_Response__Sequence response;
} turtlebot3_msgs__srv__Sound_Event;

// Struct for a sequence of turtlebot3_msgs__srv__Sound_Event.
typedef struct turtlebot3_msgs__srv__Sound_Event__Sequence
{
  turtlebot3_msgs__srv__Sound_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} turtlebot3_msgs__srv__Sound_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TURTLEBOT3_MSGS__SRV__DETAIL__SOUND__STRUCT_H_
