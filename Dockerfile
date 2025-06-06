# Используем базовый образ Python версии 3.10.4
FROM python:3.10.4

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы вашего приложения в контейнер
COPY . .

# Указываем команду для запуска приложения
CMD ["python3", "main.py"]
