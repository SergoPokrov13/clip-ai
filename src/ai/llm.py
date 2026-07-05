from ollama import chat
import json
import re


def analyze_clip(window):

    prompt = f"""
Ты профессиональный монтажер TikTok.

Тебе дан фрагмент стрима.

Информация:

Начало: {window["start"]:.1f} сек
Конец: {window["end"]:.1f} сек

Громкость (0-10):
{window["audio_score"]}

Текст:

{window["text"]}

Оцени этот момент.

Ответь строго JSON.

{{
    "score": 1,
    "title": "",
    "reason": "",
    "category": "",
    "hook": "",
    "emotion": ""
}}
"""

    print(
        f"\n🎧 Audio score: {window['audio_score']}"
    )

    response = chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    answer = re.sub(
        r"```json|```",
        "",
        answer
    ).strip()

    try:

        data = json.loads(answer)

        return {
            "score": data.get("score", 1),
            "title": data.get("title", ""),
            "reason": data.get("reason", ""),
            "category": data.get("category", ""),
            "hook": data.get("hook", ""),
            "emotion": data.get("emotion", ""),
            "start": window["start"],
            "end": window["end"],
            "text": window["text"]
        }

    except Exception:

        return {
            "score": 1,
            "title": "",
            "reason": answer,
            "category": "",
            "hook": "",
            "emotion": "",
            "start": window["start"],
            "end": window["end"],
            "text": window["text"]
        }