from enum import Enum
from pydantic import BaseModel, Field

class dataSource(str, Enum):
    KAGGLE = "kaggle"
    LOCAL = "local"
    DATABASE = "database"

