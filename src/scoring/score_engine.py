from src.detectors.emotion_detector import emotion_score


def calculate_score(window, audio_events):
    """
    Вычисляет общий рейтинг окна.
    """

    audio_score = 0

    for event in audio_events:

        if window["start"] <= event["start"] <= window["end"]:
            audio_score += event["score"]

    emotion = emotion_score(window["text"])

    total = emotion + audio_score

    return {
        "start": window["start"],
        "end": window["end"],
        "text": window["text"],
        "emotion_score": emotion,
        "audio_score": audio_score,
        "score": total
    }