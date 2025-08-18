# PDF Processor and MongoDB Ingestor

## Description
This project provides a robust Python application designed to process PDF documents, extract their content, clean the extracted data, and store it efficiently in a MongoDB database. It's built to handle various PDF inputs and integrate seamlessly with a MongoDB backend for data persistence.

## Features
- **PDF Content Extraction**: Extracts text and potentially other data from PDF files.
- **Data Cleaning**: Processes raw extracted data to ensure consistency and usability.
- **MongoDB Integration**: Stores processed PDF content, along with metadata like file name and user ID, directly into a MongoDB collection.
- **Command-Line Interface (CLI)**: Easy-to-use interface for processing individual PDF files.
- **Error Handling**: Includes logging and error management for robust operation.

## Project Structure
- `main.py`: The main entry point for the application, handling CLI arguments and orchestrating the PDF processing flow.
- `agent.py`: (Further investigation might be needed, but not directly used by `main.py` for core PDF processing).
- `app.py`: (Likely a web application or API component, not directly used by `main.py` for core PDF processing).
- `config.yaml`: Configuration file for the application (e.g., MongoDB connection details).
- `docker-compose.yml`: Docker Compose file for setting up the application and its dependencies (e.g., MongoDB).
- `requirements.txt`: Python dependencies.
- `src/`: Contains the core logic of the application.
    - `src/data_pipeline/pdf/`:
        - `dispatcher.py`: Orchestrates the PDF extraction, cleaning, and saving process.
        - `extractor.py`: Handles the extraction of data from PDF files.
        - `cleaner.py`: Processes and cleans the extracted data.
    - `src/models/mongo/pdf_document.py`: Defines the MongoDB document structure for processed PDFs.
    - `src/core/logger_utils.py`: Utility for logging.
- `tests/`: Contains unit and integration tests.

## Installation

### Prerequisites
- Python 3.8+
- MongoDB (local or remote instance)
- Docker (optional, for `docker-compose` setup)

### Steps

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # Or using poetry (if pyproject.toml is the primary source)
    # poetry install
    ```

4.  **Configure MongoDB:**
    Ensure your MongoDB instance is running and accessible. Update `config.yaml` with your MongoDB connection details if necessary.
    A `docker-compose.yml` is provided for easy setup of MongoDB:
    ```bash
    docker-compose up -d mongodb
    ```

5.  **Environment Variables:**
    Copy `.env.example` to `.env` and fill in any necessary environment variables (e.g., MongoDB connection string if not in `config.yaml`).
    ```bash
    cp env.example .env
    # Edit .env if needed
    ```

## Usage

To process a PDF file, run the `main.py` script from the command line:

```bash
python main.py <path_to_pdf_file> [user_id]
```

-   `<path_to_pdf_file>`: The absolute or relative path to the PDF document you want to process.
-   `[user_id]`: (Optional) A user ID to associate with the processed document. If not provided, it defaults to `default_user`.

### Examples:

Process a PDF named `document.pdf` in the current directory:
```bash
python main.py document.pdf
```

Process a PDF with a specific user ID:
```bash
python main.py /path/to/your/document.pdf user123
```

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details (if available).
