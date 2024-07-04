from pydantic import BaseModel
from typing import List

class DataModel(BaseModel):
    timestamp: str
    value: float
    instrument_id: str

class AnalysisResult(BaseModel):
    total_entries: int
    average_value: float
