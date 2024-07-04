import json
from pathlib import Path
from .models import VisualizationData

def generate_visualization(data_id: int) -> VisualizationData:
    # Simulated visualization logic using a sample JSON file
    visualization_file = Path(__file__).parent / "data" / "sample_visualization.json"
    with open(visualization_file, 'r') as f:
        visualization = json.load(f)
    return VisualizationData(**visualization)
