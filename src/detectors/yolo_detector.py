from ultralytics import YOLO
import numpy as np

# легкая модель
model = YOLO("yolov8n.pt")


def detect_objects(frame):

    results = model(frame, verbose=False)[0]

    detections = []

    for box in results.boxes:

        cls = int(box.cls[0])
        conf = float(box.conf[0])

        name = model.names[cls]

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        detections.append({
            "label": name,
            "confidence": conf,
            "box": (x1, y1, x2, y2)
        })

    return detections


def scene_type(detections):

    labels = [d["label"] for d in detections]

    has_person = "person" in labels
    has_tv = "tv" in labels or "monitor" in labels
    has_laptop = "laptop" in labels

    if has_tv or has_laptop:
        return "screen"

    if has_person:
        return "face_or_irl"

    return "unknown"