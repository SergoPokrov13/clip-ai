import subprocess


def smart_crop(
    input_video,
    output_video,
    face
):
    x, y, w, h = face

    center = x + w // 2

    crop_x = max(0, center - 540)

    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        input_video,

        "-vf",
        f"crop=1080:1080:{crop_x}:0,"
        "scale=1080:1920",

        "-c:a",
        "copy",

        output_video
    ]

    subprocess.run(cmd)