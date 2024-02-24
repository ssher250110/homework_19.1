# Путь до файла index.html
from pathlib import Path

ROOT_PATH = Path(__file__).parent
INDEX_HTML = Path.joinpath(ROOT_PATH, "index.html")

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети
