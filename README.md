# BookMate

PDF processing application with MongoDB storage.

## Quick Start

### 1. Setup Environment

Copy environment variables:
```bash
cp env.example .env
```

### 2. Start MongoDB

```bash
docker-compose up -d
```

This will start a MongoDB replica set with 3 nodes on ports 30001, 30002, 30003.

### 3. Run Application

```bash
# Install dependencies
uv sync

# Process a PDF file
python main.py path/to/your/file.pdf [user_id]
```

## Development

### MongoDB Connection

The application connects to MongoDB replica set:
- **Host**: `mongo1:30001,mongo2:30002,mongo3:30003`
- **Database**: `twin`
- **Replica Set**: `my-replica-set`

### Local Development

For local development, uncomment the localhost line in `.env`:
```
MONGO_DATABASE_HOST=mongodb://localhost:30001,localhost:30002,localhost:30003/?replicaSet=my-replica-set
```

## Usage

```bash
# Basic usage
python main.py document.pdf

# With custom user ID
python main.py document.pdf user123

# Help
python main.py --help
```
