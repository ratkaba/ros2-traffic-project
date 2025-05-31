
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from ultralytics import YOLO
from cv_bridge import CvBridge
# import cv2

class UltralyticsNode(Node):
    def __init__(self):
        super().__init__("ultralytics_node")

        self.detection_model = YOLO("best.pt")
        # self.segmentation_model = YOLO("yolo11m-seg.pt")

        self.bridge = CvBridge()
        self.det_image_pub = self.create_publisher(Image, "/ultralytics/detection/image", 5)
        # self.seg_image_pub = self.create_publisher(Image, "/ultralytics/segmentation/image", 5)
        self.image_sub = self.create_subscription(
            Image,
            "/image_raw",
            self.callback,
            10
        )
        self.get_logger().info("Ultralytics detection + segmentation ultralytics_node started.")
    def callback(self, msg):
        try:
            # Convert ROS image to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="rgb8")
            # Run detection model
            if (1):
                det_result = self.detection_model(cv_image)
                det_annotated = det_result[0].plot(show=False)
                det_image_msg = self.bridge.cv2_to_imgmsg(det_annotated, encoding="rgb8")
                self.det_image_pub.publish(det_image_msg)
            # Run segmentation model
            # if (1):
            #     seg_result = self.segmentation_model(cv_image)
            #     seg_annotated = seg_result[0].plot(show=False)
            #     seg_image_msg = self.bridge.cv2_to_imgmsg(seg_annotated, encoding="rgb8")
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