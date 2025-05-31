# import time
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from ultralytics import YOLO
from cv_bridge import CvBridge

class UltralyticsNode(Node):
    def __init__(self):
        super().__init__("ultralytics_node")

        # Initialize models
        self.detection_model = YOLO("best.pt")
        # self.segmentation_model = YOLO("yolo11m-seg.pt")

        # Initialize CV Bridge for image conversion
        self.bridge = CvBridge()
        
        # Create publishers
        self.det_image_pub = self.create_publisher(Image, "/ultralytics/detection/image", 5)
        # self.seg_image_pub = self.create_publisher(Image, "/ultralytics/segmentation/image", 5)
        
        # Create subscriber
        self.image_sub = self.create_subscription(
            Image,
            "/image_raw",
            self.callback,
            5
        )
        
        self.get_logger().info("Ultralytics node initialized")

    def callback(self, msg):
        """Callback function to process image and publish annotated images."""
        try:
            # Convert ROS Image message to OpenCV array
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="rgb8")

            # Check if detection publisher has subscribers
            if self.det_image_pub.get_subscription_count() > 0:
                det_result = self.detection_model(cv_image)
                det_annotated = det_result[0].plot(show=False)
                
                # Convert back to ROS Image message
                det_image_msg = self.bridge.cv2_to_imgmsg(det_annotated, encoding="rgb8")
                det_image_msg.header = msg.header  # Preserve original timestamp
                self.det_image_pub.publish(det_image_msg)
            
            # Check if segmentation publisher has subscribers
            # if self.seg_image_pub.get_subscription_count() > 0:
            #     seg_result = self.segmentation_model(cv_image)
            #     seg_annotated = seg_result[0].plot(show=False)

            #     # Convert back to ROS Image message
            #     seg_image_msg = self.bridge.cv2_to_imgmsg(seg_annotated, encoding="rgb8")
            #     seg_image_msg.header = msg.header  # Preserve original timestamp
            #     self.seg_image_pub.publish(seg_image_msg)

        except Exception as e:
            self.get_logger().error(f"processing error: {str(e)}")

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