from src.data_pipeline.pdf.cleaner import DataCleaner
from src.data_pipeline.pdf.extractor import PDFExtractor
from src.models.mongo.pdf_document import PDFDocument
from src.core.logger_utils import get_logger
from typing import Dict

logger = get_logger(__name__)

class PDFDispatcher:
    def process_pdf(self, file_path: str, user_id: str) -> Dict[str, str]:
        try:
            extractor = PDFExtractor(file_path)
            raw_data = extractor.extract()

            cleaner = DataCleaner()
            cleaned_data = cleaner.process(raw_data)

            document = PDFDocument(
                file_name=file_path.split("/")[-1],
                content=cleaned_data,
                user_id=user_id
            )
            document.save()

            return {"status": "success", "message": f"PDF {file_path} обработан и сохранен"}
        except Exception as e:
            logger.error(f"Ошибка обработки PDF: {str(e)}")
            return {"status": "error", "message": str(e)}