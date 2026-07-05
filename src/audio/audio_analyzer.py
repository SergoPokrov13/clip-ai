import librosa
import numpy as np


def analyze_audio(video_path):

    print("🎧 Загружаем аудио...")

    audio, sr = librosa.load(
        video_path,
        sr=16000,
        mono=True
    )

    print("✅ Аудио загружено")

    rms = librosa.feature.rms(
        y=audio,
        frame_length=sr,
        hop_length=sr
    )[0]

    mean = np.mean(rms)
    std = np.std(rms)

    result = []

    for i, energy in enumerate(rms):

        score = 0

        if energy > mean:
            score += 1

        if energy > mean + std:
            score += 2

        if energy > mean + 2 * std:
            score += 3

        result.append({
            "start": i,
            "end": i + 1,
            "energy": float(energy),
            "score": score
        })

    return result