from faster_whisper import WhisperModel
import os


_model = None


def get_model():
    """
    Lazy-load Whisper (чтобы не грузить каждый раз)
    """
    global _model

    if _model is None:
        print("🚀 Загружаем Whisper...")

        _model = WhisperModel(
            "base",
            device="cpu",   # можно поменять на cuda если есть GPU
            compute_type="int8"
        )

        print("✅ Whisper загружен")

    return _model


def clean_text(text: str) -> str:
    """
    Чистит мусорные повторы
    """
    text = text.strip()

    # убираем повторяющиеся артефакты
    bad_phrases = [
        "Субтитры сделал DimaTorzok",
        "субтитры сделал dimaTorzok"
    ]

    for bad in bad_phrases:
        text = text.replace(bad, "")

    # убираем двойные пробелы
    text = " ".join(text.split())

    return text


def clean_segments(segments):
    """
    Убираем дубли и мусор
    """
    cleaned = []
    prev_text = ""

    for s in segments:
        text = clean_text(s.text)

        if not text:
            continue

        if text == prev_text:
            continue

        cleaned.append({
            "start": float(s.start),
            "end": float(s.end),
            "text": text
        })

        prev_text = text

    return cleaned


def transcribe(video_path: str):
    """
    Основная функция распознавания
    """

    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Видео не найдено: {video_path}")

    model = get_model()

    print("🎙️ Начинаем распознавание...")

    segments_raw, info = model.transcribe(
        video_path,
        beam_size=5,
        vad_filter=True
    )

    segments = list(segments_raw)

    print("✅ Распознавание завершилось")
    print("✅ Сегменты собраны")

    segments = clean_segments(segments)

    return segments