from fastapi import APIRouter
from .models import DataModel
from typing import List
import json
import requests  # Pour les requêtes HTTP
from pathlib import Path

data_router = APIRouter()

@data_router.post("/data/")
def collect_data(data: List[DataModel]):
    # Path to the data file
    data_file = Path(__file__).parent / "data" / "sample_data.json"
    
    # Load existing data
    if data_file.exists():
        with open(data_file, 'r') as f:
            existing_data = json.load(f)
    else:
        existing_data = []
    
    # Add new data
    new_data = [d.dict() for d in data]
    all_data = existing_data + new_data
    
    # Save updated data
    with open(data_file, 'w') as f:
        json.dump(all_data, f)
    
    for d in new_data:
        notification = {
            "timestamp": d["timestamp"],
            "message": f"New data collected for {d['instrument_id']}"
        }
        requests.post("http://notification:80/notifications/", json=notification)
    
    return {"status": "Data collected"}

@data_router.get("/data/")
def get_data():
    # Read data from the file
    data_file = Path(__file__).parent / "data" / "sample_data.json"
    if data_file.exists():
        with open(data_file, 'r') as f:
            data = json.load(f)
        return data
    else:
        return {"status": "No data found"}
