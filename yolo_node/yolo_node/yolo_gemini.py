import rclpy
from rclpy.node import Node
import ros_numpy
from sensor_msgs.msg import Image
from ultralytics import YOLO

class UltralyticsNode(Node):
    def __init__(self):
        super().__init__("ultralytics")

        self.detection_model = YOLO("yolo11m.pt")
        self.segmentation_model = YOLO("yolo11m-seg.pt")

        self.det_image_pub = self.create_publisher(Image, "/ultralytics/detection/image", 5)
        self.seg_image_pub = self.create_publisher(Image, "/ultralytics/segmentation/image", 5)

        # QoS profile depth 
        self.create_subscription(Image, "/camera/color/image_raw", self.callback, 10)
        # self.subscription = 
        # self.subscription  # prevent unused variable warning

        self.get_logger().info("Ultralytics node started.")

    def callback(self, msg):
        try:
            """Callback function to process image and publish annotated images."""
            cv_image = ros_numpy.numpify(msg)

            # Check if there are subscribers before processing and publishing
            if self.det_image_pub.get_subscription_count() > 0:
                det_result = self.detection_model(cv_image)
                det_annotated = det_result[0].plot(show=False)
                self.det_image_pub.publish(ros_numpy.msgify(Image, det_annotated, encoding="rgb8"))

            if self.seg_image_pub.get_subscription_count() > 0:
                seg_result = self.segmentation_model(cv_image)
                seg_annotated = seg_result[0].plot(show=False)
                self.seg_image_pub.publish(ros_numpy.msgify(Image, seg_annotated, encoding="rgb8"))
        except Exception as e:
            self.get_logger().error(f"processing error: {str(e)}")

def main(args=None):
    rclpy.init(args=args)
    ultralytics_node = UltralyticsNode()
    rclpy.spin(ultralytics_node)
    ultralytics_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()