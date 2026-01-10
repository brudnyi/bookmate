# BookMate

Приложение для обработки PDF-файлов с хранением в MongoDB.

## Быстрый старт

### 1. Настройка окружения

Скопируйте переменные окружения:
```bash
cp env.example .env
```

### 2. Запуск MongoDB

```bash
docker-compose up -d
```

Это запустит MongoDB replica set с 3 нодами на портах 30001, 30002, 30003.

### 3. Запуск приложения

```bash
# Установка зависимостей
uv sync

# Обработка PDF-файла
python main.py path/to/your/file.pdf [user_id]
```

## Разработка

### Подключение к MongoDB

Приложение подключается к MongoDB replica set:
- **Хост**: `mongo1:30001,mongo2:30002,mongo3:30003`
- **База данных**: `twin`
- **Реплика-сет**: `my-replica-set`

### Локальная разработка

Для локальной разработки раскомментируйте строку с localhost в `.env`:
```
MONGO_DATABASE_HOST=mongodb://localhost:30001,localhost:30002,localhost:30003/?replicaSet=my-replica-set
```

## Использование

```bash
# Базовое использование
python main.py document.pdf

# С пользовательским ID
python main.py document.pdf user123

# Помощь
python main.py --help
