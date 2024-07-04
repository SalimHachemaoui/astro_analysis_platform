from fastapi import APIRouter
from .models import VisualizationData
import json
from pathlib import Path

visualization_router = APIRouter()

@visualization_router.get("/visualize/{data_id}", response_model=VisualizationData)
def visualize(data_id: int):
    # Simulated visualization logic using a sample JSON file
    visualization_file = Path(__file__).parent / "data" / "sample_visualization.json"
    with open(visualization_file, 'r') as f:
        visualization = json.load(f)
    return visualization
