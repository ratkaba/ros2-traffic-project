import time

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from sensor_msgs.msg import Image
import ros2_numpy
from ultralytics import YOLO

class UltralyticsNode(Node):
    def __init__(self):
        super().__init__("ultralytics")
        time.sleep(1)  # Allow ultralytics_node initialization
        
        # Initialize YOLO models
        self.detection_model = YOLO("yolo11m.pt")
        self.segmentation_model = YOLO("yolo11m-seg.pt")
        
        # Define QoS profile
        qos = QoSProfile(
            depth=5,
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST
        )
        
        # Create publishers
        self.det_image_pub = self.create_publisher(
            Image, 
            "/ultralytics/detection/image", 
            qos
        )
        self.seg_image_pub = self.create_publisher(
            Image, 
            "/ultralytics/segmentation/image", 
            qos
        )
        
        # Create subscriber
        self.create_subscription(
            Image,
            "/camera/color/image_raw",
            self.callback,
            qos
        )

    def callback(self, msg):
        """Callback function to process image and publish annotated images."""
        cv_image = ros2_numpy.numpify(msg)
        
        # Process detection if there are subscribers
        if self.det_image_pub.get_subscription_count():
            det_result = self.detection_model(cv_image)
            det_annotated = det_result[0].plot(show=False)
            self.det_image_pub.publish(
                ros2_numpy.msgify(Image, det_annotated, encoding="rgb8")
            )

        # Process segmentation if there are subscribers
        if self.seg_image_pub.get_subscription_count():
            seg_result = self.segmentation_model(cv_image)
            seg_annotated = seg_result[0].plot(show=False)
            self.seg_image_pub.publish(
                ros2_numpy.msgify(Image, seg_annotated, encoding="rgb8")
            )

def main(args=None):
    rclpy.init(args=args)
    ultralytics_node = UltralyticsNode()
    try:
        rclpy.spin(ultralytics_node)
    except KeyboardInterrupt:
        pass
    finally:
        ultralytics_node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()