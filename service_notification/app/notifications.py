from .models import Notification
import json
from pathlib import Path

def send_notification(event: Notification):
    # Simulated notification logic (In a real scenario, this might send an email or SMS)
    notification_file = Path(__file__).parent / "data" / "sample_notifications.json"
    with open(notification_file, 'w') as f:
        json.dump(event.dict(), f)
