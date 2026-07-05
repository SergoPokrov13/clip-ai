import subprocess
import os


def make_vertical(input_video, output_video):
    """
    Делает вертикальное видео 1080x1920.
    Пока просто центрирует кадр.
    """

    os.makedirs(os.path.dirname(output_video), exist_ok=True)

    cmd = [
        "ffmpeg",
        "-y",
        "-i", input_video,

        "-vf",
        (
            "crop=ih*9/16:ih,"
            "scale=1080:1920"
        ),

        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "20",

        "-c:a", "aac",

        output_video
    ]

    subprocess.run(cmd, check=True)