import time

import rclpy
from rclpy.node import Node
import ros2_numpy as ros_numpy
from sensor_msgs.msg import Image
from ultralytics import YOLO

class UltralyticsNode(Node):
    def __init__(self):
        super().__init__("ultralytics")
        
        # Load models
        self.detection_model = YOLO("yolo11m.pt")
        self.segmentation_model = YOLO("yolo11m-seg.pt")
        
        # Create publishers
        self.det_image_pub = self.create_publisher(
            Image, "/ultralytics/detection/image", 5
        )
        self.seg_image_pub = self.create_publisher(
            Image, "/ultralytics/segmentation/image", 5
        )
        
        # Create subscriber
        self.subscription = self.create_subscription(
            Image,
            "/camera/color/image_raw",
            self.callback,
            10
        )
        
        # Optional: Add a short delay to ensure everything is initialized
        time.sleep(1)
        self.get_logger().info("Ultralytics node initialized")

    def callback(self, data):
        """Callback function to process image and publish annotated images."""
        try:
            array = ros_numpy.numpify(data)
            
            if self.det_image_pub.get_subscription_count() > 0:
                det_result = self.detection_model(array)
                det_annotated = det_result[0].plot(show=False)
                self.det_image_pub.publish(
                    ros_numpy.msgify(Image, det_annotated, encoding="rgb8")
                )

            if self.seg_image_pub.get_subscription_count() > 0:
                seg_result = self.segmentation_model(array)
                seg_annotated = seg_result[0].plot(show=False)
                self.seg_image_pub.publish(
                    ros_numpy.msgify(Image, seg_annotated, encoding="rgb8")
                )
                
        except Exception as e:
            self.get_logger().error(f"Error in callback: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    node = UltralyticsNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()