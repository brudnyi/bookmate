from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.database import Database
from src.core.logger_utils import get_logger
from src.core.settings import settings
from typing import Optional, Any

logger = get_logger(__name__)

class MongoDatabaseConnector:
    """Singleton class to connect to MongoDB database."""

    _instance: Optional['MongoDatabaseConnector'] = None
    _client: Optional[MongoClient] = None
    
    def __new__(cls, *args: Any, **kwargs: Any) -> 'MongoDatabaseConnector':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            try:
                cls._client = MongoClient(settings.MONGO_DATABASE_HOST)
                logger.info(
                    f"Connection to database with uri: {settings.MONGO_DATABASE_HOST} successful"
                )
            except ConnectionFailure:
                logger.error("Couldn't connect to the database.")
                raise
        
        return cls._instance
    
    def get_database(self) -> Database:
        assert self._client, "Database connection not initialized"
        return self._client[settings.MONGO_DATABASE_NAME]
    
    def close(self) -> None:
        if self._client:
            self._client.close()
            logger.info("Connected to database has been closed.")
    
connection = MongoDatabaseConnector()
        