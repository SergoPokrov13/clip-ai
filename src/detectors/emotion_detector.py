EMOTION_WORDS = {
    "бля": 3,
    "блять": 3,
    "ебать": 4,
    "пиздец": 4,
    "сука": 3,
    "ахах": 5,
    "хаха": 5,
    "хахаха": 6,
    "орал": 5,
    "ржу": 5,
    "жесть": 3,
    "капец": 2,
    "нет": 1,
    "дааа": 3,
    "ооо": 2,
    "ого": 3,
    "неее": 2,
    "ох": 2,
}


def emotion_score(text: str) -> int:
    """
    Возвращает оценку эмоциональности текста.
    """

    score = 0

    text = text.lower()

    for word, value in EMOTION_WORDS.items():
        score += text.count(word) * value

    return score