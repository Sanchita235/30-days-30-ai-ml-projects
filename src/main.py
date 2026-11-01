import cv2
from pathlib import Path

from face_detector import FaceDetector
from utils import draw_faces, save_screenshot


# Get project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


def main():

    # Initialize face detector
    detector = FaceDetector()

    # Access webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not access webcam.")
        return

    print("\n========== FACE DETECTION SYSTEM ==========")
    print("Webcam started successfully!")
    print("Press Q to quit")
    print("Press S to save screenshot")
    print("===========================================\n")

    while True:

        success, frame = camera.read()

        if not success:
            print("Failed to capture frame.")
            break

        # Detect faces
        faces = detector.detect_faces(frame)

        # Draw bounding boxes and face count
        frame = draw_faces(frame, faces)

        # Display webcam output
        cv2.imshow("Real-Time Face Detection", frame)

        # Keyboard controls
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        elif key == ord('s'):
            save_screenshot(frame, OUTPUT_DIR)

    # Release resources
    camera.release()
    cv2.destroyAllWindows()

    print("Face Detection System Closed.")


if __name__ == "__main__":
    main()