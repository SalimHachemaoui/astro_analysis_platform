from fastapi import APIRouter
from app.models import DataModel, AnalysisResult
from typing import List

analysis_router = APIRouter()

@analysis_router.post("/analyze/", response_model=AnalysisResult)
def analyze_data(data: List[DataModel]):
    total_entries = len(data)
    average_value = sum(d.value for d in data) / total_entries if total_entries > 0 else 0
    return AnalysisResult(total_entries=total_entries, average_value=average_value)
