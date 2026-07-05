import cv2


def detect_face(video_path):
    """
    Возвращает координаты лица на первом найденном кадре.
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise Exception("Не удалось открыть видео")

    face = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    found = None

    while True:

        ok, frame = cap.read()

        if not ok:
            break

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = face.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        if len(faces):

            largest = max(
                faces,
                key=lambda f: f[2] * f[3]
            )

            found = largest
            break

    cap.release()

    return found