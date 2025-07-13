from pydantic import UUID4, BaseModel, Field
from src.core.db.mongo import connection
import uuid
from typing import Any

class PDFDocument(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    file_name: str
    content: dict
    user_id: str = Field(alias="user_id")

    class Settings:
        name = "pdf_documents"

    def to_mongo(self, **kwargs: Any) -> dict:
        parsed = self.model_dump(exclude_unset=True, by_alias=True, **kwargs)
        if "_id" not in parsed and "id" in parsed:
            parsed["_id"] = str(parsed.pop("id"))
        return parsed

    def save(self) -> None:
        collection = connection.get_database().get_collection(self.Settings.name)
        collection.insert_one(self.to_mongo())