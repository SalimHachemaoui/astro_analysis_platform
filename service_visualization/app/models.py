from pydantic import BaseModel
from typing import List, Dict

class DataPoint(BaseModel):
    time: str
    value: float

class VisualizationData(BaseModel):
    timestamp: str
    visualization_data: Dict[str, List[DataPoint]]
