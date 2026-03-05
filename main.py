import cv2
import argparse
from ultralytics import YOLO


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 Live Webcam Detection")

    parser.add_argument(
        "--model-path",
        default=r"C:\Users\USER\Desktop\object-detection\yolov8n.pt",
        type=str
    )

    
    parser.add_argument(
        "--conf",
        default=0.25,
        type=float
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    print(f"Loading model: {args.model_path}")
    model = YOLO(args.model_path)

    cap = cv2.VideoCapture(0)

    print("Press ESC to exit...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO inference
        results = model(frame, conf=args.conf)

        # Use YOLO built-in plot (THIS is what CLI uses)
        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Live Detection", annotated_frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()