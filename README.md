# 🖐️ Real-Time Hand Detection & Landmark Tracking

A computer vision project that detects human hands through a webcam and tracks their 21 key landmarks in real time using Python, OpenCV, and MediaPipe.

The objective is to understand how hand landmark detection works and build a foundation for gesture recognition and interactive computer vision applications.

## ✨ Features

- **Real-time hand detection:** Detects hands using a live webcam feed.
- **21 Landmark Detection:** Identifies 21 key points on a detected hand.
- **Fingertip Tracking:** Tracks the index fingertip using landmark ID 8.
- **Landmark Visualisation:** Displays hand landmarks and connections on the webcam feed.
- **Live Coordinate Tracking:** Extracts landmark coordinates from each frame.
- **Configurable Detection:** Uses detection and tracking confidence thresholds of 0.7.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| OpenCV | Webcam input and image processing |
| MediaPipe 0.10.21 | Hand detection and landmark tracking |
| NumPy | Numerical and image processing operations |

## 🧠 Understanding Hand Landmarks

MediaPipe detects 21 landmarks for each hand.

These landmarks represent important hand joints and anatomical positions.

### Key Landmark IDs

| Landmark | ID |
|---|---:|
| Wrist | 0 |
| Thumb tip | 4 |
| Index fingertip | 8 |
| Middle fingertip | 12 |
| Ring fingertip | 16 |
| Pinky fingertip | 20 |

The landmark coordinates are normalised relative to the image dimensions.

- X represents horizontal position.
- Y represents vertical position.
- Z represents relative depth.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate into the project

```bash
cd AquaTouch
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install opencv-python mediapipe==0.10.21 numpy
```

## ▶️ Running the Project

Test your webcam:

```bash
python src/camera_test.py
```

Run the main application:

```bash
python main.py
```

Make sure your webcam is connected and accessible.

Press `Q` to exit the webcam window.

## 🔍 How It Works

The hand detection pipeline follows these stages:

1. **Video Capture:** OpenCV captures frames from the webcam.
2. **Image Processing:** Frames are prepared for MediaPipe processing.
3. **Hand Detection:** MediaPipe identifies the hand in the frame.
4. **Landmark Extraction:** The model extracts 21 hand landmarks.
5. **Coordinate Mapping:** Normalised landmark coordinates are mapped to pixel positions.
6. **Visualisation:** OpenCV draws the landmarks and hand connections.
7. **Tracking:** Landmark positions are updated continuously across video frames.

## 🧪 What I'm Exploring

Through this project, I'm learning:

- Fundamentals of computer vision
- Pretrained landmark detection models
- Real-time image processing
- Normalised versus pixel coordinates
- Hand anatomy and landmark topology
- Webcam frame processing
- Object tracking fundamentals

## 🚀 Future Improvements

- [ ] Multi-hand detection
- [ ] Track all five fingertips
- [ ] Finger counting system
- [ ] Gesture recognition
- [ ] Hand gesture classification
- [ ] Dynamic gesture detection
- [ ] Integration with interactive simulations
- [ ] Performance optimisation

## 🔗 Connection to AquaTouch

This hand tracking module serves as the computer vision foundation for AquaTouch, an interactive water simulation controlled through hand movements.

The broader objective is to connect real-world hand movements with virtual environments.

## 👩‍💻 About

This project is part of my journey into computer vision and AI/ML engineering.

Rather than treating pretrained models as black boxes, I'm exploring their underlying concepts, experimenting with landmark coordinates, and building applications around them.

**Built with Python, OpenCV, and MediaPipe.**
