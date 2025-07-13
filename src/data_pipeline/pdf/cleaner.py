import re
from typing import Dict, Any

class DataCleaner:
    @staticmethod
    def clean_text(text: str) -> str:
        text = re.sub(r'\s+', ' ', text.strip())
        text = re.sub(r'[^\w\s.,!?]', '', text)
        return text

    def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data["content"] = self.clean_text(data["content"])
        return data