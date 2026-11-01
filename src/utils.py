import cv2
from datetime import datetime


def draw_faces(frame, faces):

    for (x, y, w, h) in faces:

        # Draw bounding box around each face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Display total face count
    cv2.putText(
        frame,
        f"Faces Detected: {len(faces)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    return frame


def save_screenshot(frame, output_dir):

    filename = datetime.now().strftime(
        "face_%Y%m%d_%H%M%S.jpg"
    )

    filepath = output_dir / filename

    cv2.imwrite(str(filepath), frame)

    print(f"Screenshot saved: {filepath}")