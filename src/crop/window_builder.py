from typing import List, Dict

# YOLO сцены (опционально, пока НЕ используем напрямую)
try:
    from src.detectors.scene_detector import analyze_scene_frames
    SCENE_AVAILABLE = True
except Exception:
    SCENE_AVAILABLE = False


def build_windows(segments: List[Dict], window_size: int = 30):
    """
    Собирает окна по N секунд из сегментов Whisper.
    YOLO НЕ вызывается здесь напрямую — только структура под него готовится.
    """

    windows = []

    if not segments:
        return windows

    current_window = []

    current_start = segments[0]["start"]
    current_end = current_start + window_size

    for segment in segments:

        if segment["end"] <= current_end:
            current_window.append(segment)
            continue

        if current_window:
            windows.append(_build_window(current_window))

        current_window = [segment]
        current_start = segment["start"]
        current_end = current_start + window_size

    if current_window:
        windows.append(_build_window(current_window))

    return windows


def _build_window(window_segments: List[Dict]):
    """
    Собирает одно окно (text + timestamps + дефолтная сцена)
    """

    start = window_segments[0]["start"]
    end = window_segments[-1]["end"]

    text = " ".join(x["text"] for x in window_segments)

    # 🔥 ВАЖНО: нормальный дефолт
    scene_info = {
        "scene": "unknown",
        "detections": []
    }

    # YOLO hook (ПОКА не используется)
    # позже сюда будет подключаться frame_sampler → YOLO
    if SCENE_AVAILABLE:
        try:
            # пока нет кадров на уровне window_builder
            # поэтому просто оставляем fallback

            scene_info = {
                "scene": "unknown",
                "detections": []
            }

        except Exception:
            scene_info = {
                "scene": "unknown",
                "detections": []
            }

    return {
        "start": start,
        "end": end,
        "text": text,

        # 🔥 всегда валидные поля
        "scene": scene_info["scene"],
        "detections": scene_info["detections"]
    }