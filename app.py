from pathlib import Path

from src.audio.transcribe import transcribe
from src.crop.window_builder import build_windows
from src.audio.audio_analyzer import analyze_audio
from src.scoring.ranker import rank_windows
from src.clipper import save_clips
from src.detectors.window_scene_analyzer import analyze_window_scene


INPUT_DIR = Path("input")


def choose_video():

    videos = []

    for ext in ("*.mp4", "*.mkv", "*.mov", "*.avi", "*.webm"):
        videos.extend(INPUT_DIR.glob(ext))
        videos.extend(INPUT_DIR.glob(f"**/{ext}"))

    videos = sorted(set(videos))

    if not videos:
        print("❌ Нет видео в input/")
        raise SystemExit

    print("\n📂 Видео:\n")

    for i, v in enumerate(videos, 1):
        print(f"{i:2}. {v.relative_to(INPUT_DIR)}")

    choice = input("\nВведите номер видео: ").strip()

    if not choice.isdigit():
        raise SystemExit

    idx = int(choice) - 1

    if idx < 0 or idx >= len(videos):
        raise SystemExit

    return str(videos[idx])


def main():

    print("=" * 70)
    print("🎬 AI STREAM CUTTER v1 (YOLO EDITION)")
    print("=" * 70)

    video = choose_video()

    print(f"\n📹 Видео: {video}")

    # --------------------
    print("\n🎙 [1/5] Whisper transcription...")
    segments = transcribe(video)
    print(f"✅ segments: {len(segments)}")

    # --------------------
    print("\n🪟 [2/5] Building windows...")
    windows = build_windows(segments)
    print(f"✅ windows: {len(windows)}")

    # --------------------
    print("\n🎧 [3/5] Audio analysis...")
    audio = analyze_audio(video)
    print(f"✅ audio length: {len(audio)}")

    # --------------------
    print("\n👁 [4/5] YOLO scene analysis...")

    for i, window in enumerate(windows):

        try:
            scene = analyze_window_scene(
                video,
                window["start"],
                window["end"]
            )

            window["scene"] = scene["scene"]
            window["detections"] = scene["detections"]

        except Exception as e:
            print(f"⚠️ YOLO error window {i}: {e}")
            window["scene"] = "unknown"
            window["detections"] = []

    print("✅ YOLO done")

    # --------------------
    print("\n⭐ [5/5] Ranking...")
    best = rank_windows(windows, audio)

    print("\n" + "=" * 70)
    print("🏆 TOP-20 CLIPS")
    print("=" * 70)

    for i, clip in enumerate(best[:20], 1):

        print(f"\n#{i}")
        print(f"Score   : {clip['score']}")
        print(f"Audio   : {clip['audio_score']}")
        print(f"Emotion : {clip['emotion_score']}")
        print(f"Scene   : {clip.get('scene', 'unknown')}")
        print(f"{clip['start']:.1f}s → {clip['end']:.1f}s")
        print(clip["text"])
        print("-" * 70)

    # --------------------
    print()

    answer = input("💾 Save TOP-5 clips? (y/n): ").lower()

    if answer == "y":
        save_clips(video, best[:5])

    print("\n✅ Done.")


if __name__ == "__main__":
    main()