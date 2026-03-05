# 🚀 YOLOv8 Live Webcam Object Detection

A real-time object detection system built using YOLOv8, OpenCV, and Python that detects objects directly from your webcam feed.

The application captures live video, performs object detection using a pretrained YOLOv8 model, and displays annotated frames with bounding boxes and labels in real time.

This project demonstrates the practical implementation of computer vision and deep learning for real-time inference.

# ✨ Features

🎥 Live Webcam Detection

🧠 YOLOv8 Deep Learning Model

📦 Pretrained COCO Dataset

🏷 Automatic Bounding Boxes & Labels

⚡ Real-Time Frame Processing

🖥 Simple Command Line Interface

# 🧠 Project Overview

The system works by:

Capturing video frames from a webcam

Running YOLOv8 inference on each frame

Detecting objects using a pretrained model

Drawing bounding boxes around detected objects

Displaying the annotated video stream in real time

This project is ideal for learning:

Computer Vision

Deep Learning Inference

Real-Time AI Applications

YOLO Object Detection

# 🛠 Technologies Used
Technology	Purpose
Python	Core programming language
OpenCV	Webcam capture & image display
Ultralytics YOLOv8	Object detection model
Argparse	Command-line argument parsing

# 📁 Project Structure

object-detection/
│
├── main.py        # Webcam object detection script
├── yolov8n.pt     # Pretrained YOLOv8 model
└── README.md

# ⚙️ Installation

1️⃣ Clone the Repository
git clone https://github.com/yourusername/Object-detection.git
cd Object-detection
2️⃣ Create a Virtual Environment (Recommended)
python -m venv venv

Activate the environment:

Windows
venv\Scripts\activate
Mac / Linux
source venv/bin/activate
3️⃣ Install Dependencies
pip install ultralytics opencv-python
▶️ Usage

Run the program using:

python main.py

Optional parameters:

python main.py --model-path yolov8n.pt --conf 0.25
# 🔧 Arguments
Argument	Description	Default
--model-path	Path to YOLOv8 model	yolov8n.pt
--conf	Detection confidence threshold	0.25
# ⚡ How It Works

The YOLOv8 model is loaded using Ultralytics.

OpenCV opens the system webcam.

Each frame is sent to the YOLO model.

The model detects objects and returns predictions.

Bounding boxes and labels are drawn on the frame.

The annotated frame is displayed in a live window.

Press ESC to exit the application.

# 🧪 Example Detected Objects

Using the COCO pretrained dataset, the model can detect objects such as:

👤 Person

🚗 Car

🐶 Dog

🐱 Cat

🚲 Bicycle

💻 Laptop

🧴 Bottle

📱 Phone


# 👨‍💻 Author

Segni Nadew

Data Science Enthusiast

Machine Learning Practitioner

Full Stack Developer

⭐ If you found this project helpful, consider starring the repository!
