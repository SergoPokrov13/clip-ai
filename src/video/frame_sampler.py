import cv2


def sample_frames(video, interval=5):

    cap = cv2.VideoCapture(video)

    fps = cap.get(cv2.CAP_PROP_FPS)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    duration = frame_count / fps

    frames = []

    t = 0

    while t < duration:

        cap.set(cv2.CAP_PROP_POS_MSEC, t * 1000)

        ret, frame = cap.read()

        if ret:
            frames.append(frame)

        t += interval

    cap.release()

    return frames