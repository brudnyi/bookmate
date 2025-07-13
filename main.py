import sys
import argparse
from pathlib import Path
from src.data_pipeline.pdf.dispatcher import PDFDispatcher
from src.core.logger_utils import get_logger

logger = get_logger(__name__)

def main() -> None:
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Process PDF files and save to MongoDB",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
        Examples:
        python main.py document.pdf
        python main.py /path/to/document.pdf user123
                """
    )
    
    parser.add_argument(
        "pdf_path",
        type=str,
        help="Path to the PDF file to process"
    )
    
    parser.add_argument(
        "user_id",
        nargs="?",
        default="default_user",
        help="User ID for the document (default: default_user)"
    )
    
    args = parser.parse_args()
    
    pdf_path = Path(args.pdf_path)
    if not pdf_path.exists():
        logger.error(f"❌ PDF file not found: {pdf_path}")
        sys.exit(1)
    
    if not pdf_path.suffix.lower() == '.pdf':
        logger.error(f"❌ File is not a PDF: {pdf_path}")
        sys.exit(1)
    
    # Process the PDF
    try:
        logger.info(f"🚀 Processing PDF: {pdf_path}")
        logger.info(f"👤 User ID: {args.user_id}")
        
        dispatcher = PDFDispatcher()
        result = dispatcher.process_pdf(str(pdf_path), args.user_id)
        
        if result["status"] == "success":
            logger.info("✅ PDF processing successful!")
            logger.info(f"📝 {result['message']}")
            sys.exit(0)
        else:
            logger.error("❌ PDF processing failed!")
            logger.error(f"💥 Error: {result['message']}")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
