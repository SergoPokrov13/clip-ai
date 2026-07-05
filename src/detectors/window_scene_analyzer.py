from src.video.frame_sampler import extract_frames
from src.detectors.yolo_detector import detect_objects, scene_type


def analyze_window_scene(video_path, start, end):
    """
    YOLO анализ одного окна
    """

    frames = extract_frames(
        video_path,
        start,
        end,
        max_frames=5
    )

    if not frames:
        return {
            "scene": "unknown",
            "detections": []
        }

    all_detections = []

    for frame in frames:

        detections = detect_objects(frame)

        all_detections.extend(detections)

    if not all_detections:
        return {
            "scene": "unknown",
            "detections": []
        }

    scene = scene_type(all_detections)

    return {
        "scene": scene,
        "detections": all_detections
    }