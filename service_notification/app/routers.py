from fastapi import APIRouter
from typing import List
from .models import Notification
import json
from pathlib import Path

notification_router = APIRouter()

@notification_router.post("/notifications/", response_model=Notification)
def create_notification(notification: Notification):
    notifications_file = Path(__file__).parent / "data" / "sample_notifications.json"
    
    # Lire les notifications existantes
    if notifications_file.exists():
        with open(notifications_file, 'r') as f:
            notifications = json.load(f)
    else:
        notifications = []

    # Ajouter la nouvelle notification
    notifications.append(notification.dict())

    # Sauvegarder les notifications mises à jour
    with open(notifications_file, 'w') as f:
        json.dump(notifications, f, indent=4)

    return notification

@notification_router.get("/notifications/", response_model=List[Notification])
def get_notifications():
    notifications_file = Path(__file__).parent / "data" / "sample_notifications.json"
    
    # Lire les notifications existantes
    if notifications_file.exists():
        with open(notifications_file, 'r') as f:
            notifications = json.load(f)
        return notifications
    else:
        return []

