import pdfplumber
from typing import Dict, Any

class PDFExtractor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract(self) -> Dict[str, Any]:
        "TODO: add OCR"
        
        data = {"content": "", "metadata": {}}
        try:
            with pdfplumber.open(self.file_path) as pdf:
                for page in list(pdf.pages):
                    text = getattr(page, "extract_text", lambda: None)()
                    if text:
                        data["content"] += text
                data["metadata"] = pdf.metadata or {}
            return data
        except Exception as e:
            raise Exception(f"Ошибка при извлечении PDF: {str(e)}")