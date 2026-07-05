from src.audio.audio_analyzer import analyze_audio


def build_features(video_path, windows):

    print("🎧 Анализируем аудио...")

    audio = analyze_audio(video_path)

    features = []

    for window in windows:

        total_score = 0
        count = 0

        for second in audio:

            if window["start"] <= second["start"] <= window["end"]:
                total_score += second["score"]
                count += 1

        if count > 0:
            audio_score = round(total_score / count, 2)
        else:
            audio_score = 0

        window["audio_score"] = audio_score

        features.append(window)

    return features