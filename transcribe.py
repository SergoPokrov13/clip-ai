from faster_whisper import WhisperModel
from pathlib import Path
import config

def transcribe(video_path):

    model = WhisperModel(
        config.MODEL_NAME,
        device="cpu",
        compute_type="int8"
    )

    segments, info = model.transcribe(
        video_path,
        language=config.LANGUAGE
    )

    transcript = []

    for segment in segments:

        transcript.append({
            "start": segment.start,
            "end": segment.end,
            "text": segment.text.strip()
        })

    return transcript
