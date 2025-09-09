# Используем образ Python
FROM python:3.12-slim

# Установим рабочую директорию
WORKDIR /app

# Скопируем файл hello_world.py в контейнер
COPY hello_world.py .

# Команда для запуска приложения
CMD ["python", "hello_world.py"]
