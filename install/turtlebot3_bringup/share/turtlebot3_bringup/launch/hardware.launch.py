#!/usr/bin/env python3
#
# Copyright 2022 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Darby Lim

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch.substitutions import LaunchConfiguration
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node

from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    namespace = LaunchConfiguration('namespace')
    LDS_MODEL = os.environ['LDS_MODEL']

    if LDS_MODEL == 'LDS-01':
        lidar_launch = PathJoinSubstitution(
            [
                FindPackageShare('hls_lfcd_lds_driver'),
                'launch',
                'hlds_laser.launch.py'
            ]
        )
    elif LDS_MODEL == 'LDS-02':
        lidar_launch = PathJoinSubstitution(
            [
                FindPackageShare('ld08_driver'),
                'launch',
                'ld08.launch.py'
            ]
        )

    start_rviz = LaunchConfiguration('start_rviz')
    prefix = LaunchConfiguration('prefix')
    use_fake_hardware = LaunchConfiguration('use_fake_hardware')

    return LaunchDescription([
        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='Specifying namespace of turtlebot3'),
        DeclareLaunchArgument(
            'start_rviz',
            default_value='false',
            description='Whether execute rviz2'),

        DeclareLaunchArgument(
            'prefix',
            default_value='""',
            description='Prefix of the joint and link names'),

        DeclareLaunchArgument(
            'use_fake_hardware',
            default_value='false',
            description='Start robot with fake hardware mirroring command to its states.'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/base.launch.py']),
            launch_arguments={
                'namespace': namespace,
                'start_rviz': start_rviz,
                'prefix': prefix,
                'use_fake_hardware': use_fake_hardware,
            }.items(),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [
                    lidar_launch
                ]
            ),
            launch_arguments={
                'namespace': namespace,
                'port': '/dev/ttyUSB0',
                'frame_id': 'base_scan',
            }.items(),
        ),

        Node(
            namespace=namespace,
            package='v4l2_camera',
            executable='v4l2_camera_node',
            output='screen',
            parameters=[
                {'image_size': [640,480],
                'time_per_frame': [1, 10],
                'camera_frame_id': 'camera_link_optical',
                'image_raw.compressed.jpeg_quality': 20
                },
            ],
        )
    ])
