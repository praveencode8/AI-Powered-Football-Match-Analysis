### Project Title

**AI/ML Football Match Analysis System (YOLO, Advanced Computer Vision, and Tracking)**

***

### Project Description

This AI/ML project delivers detailed football match analysis by applying state-of-the-art object detection, tracking, and advanced computer vision techniques to video footage.

![Screenshot](output_videos/screenshot.png)

**Key Features and Technical Contributions:**

*   **Object Detection and Tracking:** Developed and fine-tuned a custom **YOLOv11** object detection model using the **Ultralytics** library to accurately identify and classify **players, referees, goalkeepers, and the football** across video frames. Implemented the **Byte Tracker** (via the Supervision library) to maintain persistent track IDs for players and objects throughout the match.
*   **Team Assignment via Clustering:** Assigned players to specific teams by analyzing and **segmenting player t-shirt colors** within their bounding boxes using **K-means clustering**.
*   **Precise Movement Compensation:** Employed **Optical Flow** to accurately measure and compensate for **camera movement** (e.g., pan and zoom), ensuring player movement calculations are robust and uncontaminated by camera artifacts.
*   **Real-World Perspective Transformation:** Utilized **Perspective Transformation** (View Transformer) to map pixel coordinates from the camera's distorted 2D viewpoint into **accurate real-world positions (in meters)**, addressing depth and perspective issues inherent in video capture.
*   **Statistical Analysis & Key Metrics:**
    *   Calculated **player speed in kilometers/hour** and **distance covered in meters** using the perspective-transformed, camera-adjusted positions.
    *   Measured and displayed **Team Ball Acquisition Percentage** by determining which player had possession of the ball (based on foot proximity) in each frame.
*   **Data Handling and Visualization:** Used **OpenCV (CV2)** for video reading, saving, and drawing custom annotations (circles, triangles, speed labels). Managed large-scale tracking data and handled missing ball detections through **Pandas interpolation**.

## Modules Used
The following modules are used in this project:
- YOLO: AI object detection model
- Kmeans: Pixel segmentation and clustering to detect t-shirt color
- Optical Flow: Measure camera movement
- Perspective Transformation: Represent scene depth and perspective
- Speed and distance calculation per player

## Requirements
To run this project, you need to have the following requirements installed:
- Python 3.x
- ultralytics
- supervision
- OpenCV
- NumPy
- Matplotlib
- Pandas
