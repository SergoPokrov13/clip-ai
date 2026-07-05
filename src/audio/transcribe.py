from faster_whisper import WhisperModel
from src import config


def transcribe(video_path):

    print("🚀 Загружаем Whisper...")

    model = WhisperModel(
        config.MODEL_NAME,
        device="cpu",
        compute_type="int8"
    )

    print("✅ Whisper загружен")

    print("🎙️ Начинаем распознавание...")

    segments, info = model.transcribe(
        video_path,
        language=config.LANGUAGE
    )

    print("✅ Распознавание завершилось")

    transcript = []

    for segment in segments:
        transcript.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })

    print("✅ Сегменты собраны")

    return transcript