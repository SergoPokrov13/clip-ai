from pathlib import Path

from src.audio.transcribe import transcribe
from src.crop.window_builder import build_windows
from src.audio.audio_analyzer import analyze_audio
from src.scoring.ranker import rank_windows
from src.clipper import save_clips


INPUT_DIR = Path("input")


def choose_video():

    videos = []

    # Все видео в input
    for ext in ("*.mp4", "*.mkv", "*.mov", "*.avi", "*.webm"):
        videos.extend(INPUT_DIR.glob(ext))

    # Все видео во вложенных папках (например input/parts/)
    for ext in ("**/*.mp4", "**/*.mkv", "**/*.mov", "**/*.avi", "**/*.webm"):
        videos.extend(INPUT_DIR.glob(ext))

    videos = sorted(set(videos))

    if not videos:
        print("❌ В папке input нет видео.")
        raise SystemExit

    print("\n📂 Найденные видео:\n")

    for i, video in enumerate(videos, start=1):
        print(f"{i:2}. {video.relative_to(INPUT_DIR)}")

    choice = input("\nВведите номер видео: ").strip()

    if not choice.isdigit():
        print("❌ Нужно ввести номер.")
        raise SystemExit

    index = int(choice) - 1

    if index < 0 or index >= len(videos):
        print("❌ Неверный номер.")
        raise SystemExit

    return str(videos[index])


def main():

    print("=" * 80)
    print("🎬 AI Stream Cutter")
    print("=" * 80)

    video = choose_video()

    print(f"\n📹 Выбрано:\n{video}")

    print("\n🎙 Whisper...\n")

    segments = transcribe(video)

    print(f"Сегментов: {len(segments)}")

    print("\n🪟 Создаем окна...\n")

    windows = build_windows(segments)

    print(f"Окон: {len(windows)}")

    print("\n🎧 Анализ аудио...\n")

    audio = analyze_audio(video)

    print(f"Секунд аудио: {len(audio)}")

    print("\n⭐ Считаем рейтинг...\n")

    best = rank_windows(
        windows,
        audio
    )

    print("=" * 80)
    print("ТОП-20")
    print("=" * 80)

    for i, clip in enumerate(best[:20], start=1):

        print()

        print(f"#{i}")
        print(f"Общий рейтинг : {clip['score']}")
        print(f"Audio         : {clip['audio_score']}")
        print(f"Emotion       : {clip['emotion_score']}")
        print(f"Время         : {clip['start']:.1f} - {clip['end']:.1f}")

        print()
        print(clip["text"])
        print("-" * 80)

    print()

    answer = input("💾 Сохранить ТОП-5 клипов? (y/n): ").lower()

    if answer == "y":

        save_clips(
            video,
            best[:5]
        )

    print("\n✅ Готово.")


if __name__ == "__main__":
    main()