from pathlib import Path
import subprocess


def save_clips(video_path, clips, output_dir="output/clips", reencode=False):
    """
    reencode=False  -> очень быстро, возможен сдвиг до ближайшего keyframe
    reencode=True   -> медленнее, но обрезка точная
    """

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    total = len(clips)

    print("\n🎬 Начинаем сохранение клипов...\n")

    for i, clip in enumerate(clips, start=1):

        start = float(clip["start"])
        end = float(clip["end"])
        duration = end - start

        outfile = output_dir / f"clip_{i:02d}.mp4"

        print(f"[{i}/{total}] {outfile.name}")
        print(f"    {start:.1f}s → {end:.1f}s ({duration:.1f}s)")

        if reencode:

            cmd = [
                "ffmpeg",
                "-y",
                "-ss", str(start),
                "-i", str(video_path),
                "-t", str(duration),
                "-c:v", "libx264",
                "-preset", "veryfast",
                "-crf", "18",
                "-c:a", "aac",
                str(outfile)
            ]

        else:

            cmd = [
                "ffmpeg",
                "-y",
                "-ss", str(start),
                "-i", str(video_path),
                "-t", str(duration),
                "-c", "copy",
                str(outfile)
            ]

        subprocess.run(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    print("\n✅ Все клипы сохранены.")