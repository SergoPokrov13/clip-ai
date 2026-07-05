import subprocess
import json


def get_video_info(video):

    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_streams",
        video
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    data = json.loads(result.stdout)

    stream = next(
        s for s in data["streams"]
        if s["codec_type"] == "video"
    )

    fps = eval(stream["r_frame_rate"])

    return {
        "width": stream["width"],
        "height": stream["height"],
        "fps": fps
    }