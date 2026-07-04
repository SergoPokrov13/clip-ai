from pathlib import Path

from transcribe import transcribe
from analyze import analyze

# Наш тестовый файл
video = Path("input/test.mp4")

print("🎙️ Расшифровываем видео...\n")

segments = transcribe(str(video))

print("✅ Расшифровка завершена")
print(f"Количество сегментов: {len(segments)}")

print("\n🔍 Ищем лучшие моменты...\n")

best = analyze(segments)

print("=" * 80)
print("ТОП-20 МОМЕНТОВ")
print("=" * 80)

for i, clip in enumerate(best[:20], start=1):
    print(f"\n#{i}")
    print(f"Оценка: {clip['score']}")
    print(f"Время: {clip['start']:.2f} - {clip['end']:.2f}")
    print(f"Текст: {clip['text']}")
