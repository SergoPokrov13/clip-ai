WINDOW_SIZE = 30

HYPE_WORDS = {
    "аха": 5,
    "хаха": 5,
    "ору": 4,
    "лол": 3,
    "бля": 2,
    "нах": 3,
    "пиздец": 4,
    "капец": 3,
    "охрен": 4,
    "жесть": 4,
    "вау": 3,
    "что": 1,
}

def score_text(text):

    score = 0

    text = text.lower()

    for word, value in HYPE_WORDS.items():

        if word in text:
            score += value

    return score

def analyze(segments):

    if not segments:
        return []

    duration = segments[-1]["end"]

    clips = []

    current = 0

    while current < duration:

        end = current + WINDOW_SIZE

        window = []

        for segment in segments:

            if current <= segment["start"] < end:
                window.append(segment)

        if not window:
            current += WINDOW_SIZE
            continue

        score = 0

        text = []

        for segment in window:

            score += score_text(segment["text"])

            text.append(segment["text"])

        score += len(window) // 3

        clips.append({

            "start": current,
            "end": end,
            "score": score,
            "text": " ".join(text)

        })

        current += WINDOW_SIZE

    clips.sort(key=lambda x: x["score"], reverse=True)

    return clips
