import cv2


def extract_frames(video_path, start_time, end_time, max_frames=5):
    """
    Достаёт N кадров из видео между start_time и end_time
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise RuntimeError(f"Не удалось открыть видео: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0:
        fps = 25  # fallback

    frames = []

    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    step = max(1, (end_frame - start_frame) // max_frames)

    for frame_idx in range(start_frame, end_frame, step):

        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)

        ret, frame = cap.read()

        if not ret:
            continue

        frames.append(frame)

        if len(frames) >= max_frames:
            break

    cap.release()

    return frames