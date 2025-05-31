
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image

from ultralytics import YOLO
from cv_bridge import CvBridge, CvBridgeError
# import cv2

class UltralyticsNode(Node):
    def __init__(self):
        super().__init__('ultralytics_node')

        self.model = YOLO("best.pt")
        self.publisher_ = self.create_publisher(String, '/ultralytics/detection/classes', 5)
        self.subscription = self.create_subscription(
            Image,
            '/image_raw',
            self.listener_callback,
            10
        )
        self.bridge = CvBridge()
        # /camera/color/image_raw...
        self.get_logger().info("Ultralytics YOLO node initialized (no ros_numpy).")

    def listener_callback(self, msg):
        try:
            # Convert ROS image message to OpenCV image (NumPy array)
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Run detection
            results = self.model(frame)

            if results and results[0].boxes is not None:
                classes = results[0].boxes.cls.cpu().numpy().astype(int)
                names = [results[0].names[i] for i in classes]
                self.publisher_.publish(String(data=str(names)))
                self.get_logger().info(f"Published classes: {names}")
            else:
                self.get_logger().warn("No detections.")

        except CvBridgeError as e:
            self.get_logger().error(f"cv_bridge error: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = UltralyticsNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
















'''
import os, sys
os.path.dirname(sys.executable)

import time

from sensor_msgs.msg import Image
from std_msgs.msg import String

from ultralytics import YOLO

import roslibpy
import ros_numpy

detection_model = YOLO("best.pt")
roslibpy.init_node("ultralytics")
time.sleep(1)
classes_pub = roslibpy.Publisher("/ultralytics/detection/classes", String, queue_size=5)


def callback(data):
    """Callback function to process image and publish detected classes."""
    array = ros_numpy.numpify(data)
    if classes_pub.get_num_connections():
        det_result = detection_model(array)
        classes = det_result[0].boxes.cls.cpu().numpy().astype(int)
        names = [det_result[0].names[i] for i in classes]
        classes_pub.publish(String(data=str(names)))


roslibpy.Subscriber("/image_raw", Image, callback)
while True:
    roslibpy.spin()
'''
