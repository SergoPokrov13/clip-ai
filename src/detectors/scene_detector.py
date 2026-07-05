from src.detectors.yolo_detector import detect_objects, scene_type


def analyze_scene_frames(frames):
    """
    Анализирует несколько кадров и делает итоговую сцену
    """

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