# BookMate

Приложение для обработки PDF-файлов с сохранением данных в MongoDB.

## Быстрый старт

### 1. Настройка окружения

Скопируйте файл с переменными окружения:

    cp env.example .env

### 2. Запуск MongoDB

    docker-compose up -d

Это запустит реплика-сет MongoDB из 3 узлов на портах 30001, 30002 и 30003.

### 3. Запуск приложения

    # Установите зависимости
    uv sync

    # Обработать PDF-файл
    python main.py path/to/your/file.pdf [user_id]

## Разработка

### Подключение к MongoDB

Приложение подключается к реплика-сету MongoDB:
- **Хост**: `mongo1:30001,mongo2:30002,mongo3:30003`
- **База данных**: `twin`
- **Replica Set**: `my-replica-set`

### Локальная разработка

Для локальной разработки раскомментируйте строку с localhost в файле `.env`:

    MONGO_DATABASE_HOST=mongodb://localhost:30001,localhost:30002,localhost:30003/?replicaSet=my-replica-set

## Использование

    # Базовое использование
    python main.py document.pdf

    # С указанием пользовательского ID
    python main.py document.pdf user123

    # Показать справку
    python main.py --help
