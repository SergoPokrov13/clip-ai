import subprocess
from pathlib import Path


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_clips(video_path, clips):
    """
    Сохраняет топ клипы через ffmpeg (fast cut)
    """

    print("\n✂️ Начинаем нарезку клипов...\n")

    for i, clip in enumerate(clips, start=1):

        start = clip["start"]
        end = clip["end"]
        score = int(clip.get("score", 0))
        scene = clip.get("scene", "unknown")

        duration = end - start

        output_name = f"clip_{i:02d}_{int(start)}s-{int(end)}s_score{score}_{scene}.mp4"
        output_path = OUTPUT_DIR / output_name

        print(f"[{i}/{len(clips)}] ➜ {output_name}")

        cmd = [
            "ffmpeg",
            "-y",

            # input
            "-ss", str(start),
            "-i", str(video_path),

            # fast seek
            "-t", str(duration),

            # no re-encode (fast)
            "-c", "copy",

            str(output_path)
        ]

        try:
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"❌ Ошибка клипа {i}: {e}")

    print("\n✅ Все клипы сохранены в папку output/")