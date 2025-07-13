import structlog
from typing import Any

def get_logger(cls: str) -> Any:
    return structlog.get_logger().bind(cls=cls)