# 🎬 AI Stream Cutter

> 🚧 **Проект в активной разработке (MVP → Product stage)**

AI Stream Cutter — локальный AI-инструмент для автоматического поиска и нарезки лучших моментов из длинных стримов, подкастов и игровых видео.

Проект превращает длинное видео в набор **готовых viral-clips (Shorts / Reels / TikTok)** полностью офлайн.

---

# 🚀 Что умеет сейчас (MVP v2)

- 🎙 Распознавание речи (Faster-Whisper)
- 🎧 Анализ аудио (громкость / динамика)
- ⭐ Оценка эмоциональности текста
- 🧠 Ранжирование “лучших моментов”
- 👁 YOLO детекция сцен (экран / лицо / IRL)
- 📊 Scene-aware scoring
- ✂ Автоматическая нарезка клипов через FFmpeg
- 📁 Умный выбор видео из папки input
- 🏷 Авто-именование клипов (score + time + scene)

---

# 🧠 AI-логика проекта

Система анализирует видео как человек:

- слушает речь (Whisper)
- понимает эмоции (text scoring)
- анализирует звук (energy peaks)
- смотрит кадры (YOLO)
- определяет тип сцены:
  - 🎮 screen / gameplay
  - 🧑 face / reaction
  - 🏠 IRL / real-life

---

# 🖥 Поддерживаемые платформы

- Windows 10 / 11
- Ubuntu 22.04+
- Python 3.10–3.12
- FFmpeg
- Git

---

# ⚙️ Установка

## 1. Клонирование

```bash
git clone https://github.com/YOUR_USERNAME/clip-ai.git
cd clip-ai
```

## 2. Виртуальное окружение

### Windows
```powershell
python -m venv venv
venv\Scripts\activate
```

### Ubuntu
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Установка зависимостей
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. FFmpeg

Windows: https://ffmpeg.org/download.html

Ubuntu:
```bash
sudo apt update
sudo apt install ffmpeg
```

## 5. YOLO
```bash
pip install ultralytics
```

---

# 📁 Структура проекта

```
clip-ai/
├── app.py
├── input/
├── output/
├── src/
│   ├── ai/
│   ├── audio/
│   ├── crop/
│   ├── detectors/
│   ├── scoring/
│   ├── video/
│   └── clipper.py
├── requirements.txt
└── README.md
```

---

# ▶️ Запуск

```bash
python app.py
```

---

# 📦 Output

```
output/
```

Пример:

```
clip_01_240s-270s_score47_screen.mp4
```

---

# 🧪 Pipeline

Video → Whisper → Windows → YOLO → Scoring → Clipping

---

# 📌 Roadmap

- Smart Crop (YOLO bbox)
- Subtitles (SRT + burn-in)
- Face tracking
- LLM titles
- Twitch / YouTube support
- Web UI

---

# 🎯 Цель

Автоматическое создание Shorts из стримов.

---

# ⚡ Tech

Python, Whisper, YOLOv8, OpenCV, FFmpeg, NumPy

---

# MIT
