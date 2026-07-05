from src.scoring.score_engine import calculate_score


def rank_windows(windows, audio_data):
    """
    Рейтинг окон + YOLO сцены
    """

    results = []

    for window in windows:

        # базовый скоринг (УЖЕ dict)
        score_obj = calculate_score(window, audio_data)

        base_score = score_obj["score"]
        audio_score = score_obj["audio_score"]
        emotion_score = score_obj["emotion_score"]

        scene = window.get("scene", "unknown")
        scene_bonus = get_scene_bonus(scene)

        final_score = base_score + scene_bonus

        results.append({
            "start": window["start"],
            "end": window["end"],
            "text": window["text"],

            "score": final_score,

            "base_score": base_score,
            "audio_score": audio_score,
            "emotion_score": emotion_score,

            "scene": scene,
            "scene_bonus": scene_bonus
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results


def get_scene_bonus(scene):
    """
    YOLO влияние на рейтинг
    """

    if scene == "screen":
        return 8

    if scene == "face_or_irl":
        return 5

    if scene == "gameplay":
        return 3

    return 0