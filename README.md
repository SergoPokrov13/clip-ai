# 🎬 AI Stream Cutter

Локальный инструмент для автоматического поиска лучших моментов со стримов.

Проект умеет:

- 🎙️ Расшифровывать речь с помощью Faster-Whisper

- 🔍 Искать самые эмоциональные моменты

- 🤖 Анализировать их с помощью локальной LLM (Qwen через Ollama)

- ✂️ В дальнейшем автоматически нарезать клипы

- 📝 Добавлять субтитры

Все работает **локально** и **бесплатно**.

---

# Требования

- Ubuntu 22.04 / 24.04

- Python 3.12+

- Git

- ffmpeg

---

# 1. Установка зависимостей

Обновляем систему

```bash

sudo apt update

```

Устанавливаем необходимые пакеты

```bash

sudo apt install -y \

python3 \

python3-venv \

python3-pip \

ffmpeg \

git

```

Проверяем

```bash

python3 --version

ffmpeg -version

git --version

```

---

# 2. Клонируем проект

```bash

git clone https://github.com/USERNAME/clip-ai.git

```

```bash

cd clip-ai

```

---

# 3. Создаем виртуальное окружение

```bash

python3 -m venv venv

```

Активируем

```bash

source venv/bin/activate

```

---

# 4. Устанавливаем Python-библиотеки

```bash

pip install --upgrade pip

```

```bash

pip install faster-whisper

```

---

# 5. Устанавливаем Ollama

```bash

curl -fsSL https://ollama.com/install.sh | sh

```

Проверяем

```bash

ollama --version

```

---

# 6. Скачиваем модель

Рекомендуется

```bash

ollama pull qwen3:4b

```

Можно использовать другую модель.

---

# 7. Проверяем работу Whisper

```bash

python

```

```python

from faster_whisper import WhisperModel

```

Если ошибок нет — всё установлено правильно.

Выход

```python

exit()

```

---

# 8. Структура проекта

```

clip-ai/

├── app.py

├── analyze.py

├── transcribe.py

├── input/

│   └── test.mp4

├── output/

├── venv/

└── README.md

```

---

# 9. Добавьте видео

Положите видео в папку

```

input/

```

Например

```

input/test.mp4

```

---

# 10. Запуск

Активируем окружение

```bash

source venv/bin/activate

```

Запускаем

```bash

python app.py

```

---

# Что делает программа

```

Видео

        │

        ▼

Whisper

        │

        ▼

Текст + таймкоды

        │

        ▼

Поиск эмоциональных окон

        │

        ▼

Оценка каждого окна

        │

        ▼

ТОП лучших моментов

```

---

# Используемые технологии

- Python

- Faster-Whisper

- Ollama

- Qwen

- FFmpeg

---

# Roadmap

- [x] Расшифровка видео

- [x] Поиск эмоциональных моментов

- [ ] Анализ моментов через Qwen

- [ ] Автоматическая нарезка клипов

- [ ] Генерация субтитров

- [ ] Автоматические заголовки

- [ ] GUI

- [ ] Поддержка Twitch URL

- [ ] Поддержка YouTube

---

# Лицензия

MIT

