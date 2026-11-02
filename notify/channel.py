
"""
This Module is responsible for sending push notification to the client
"""
import requests

NTFY_URL = "https://ntfy.sh"
PRIORITIES = {"min": 1, "low": 2, "default": 3, "high": 4, "urgent": 5}


def send_ntfy_push(topic: str, title: str, message: str, priority: str = "default") -> bool:
    """
    this function is responsible for sending push notification to the client it returns TRUE on success and FALSE otherwise
    """
    try:
        r = requests.post(
            NTFY_URL,
            json={
                "topic": topic,
                "title": title,
                "message": message,
                "priority": PRIORITIES.get(priority, 3),
            },
            timeout=10,
        )
        return r.ok
    except requests.RequestException:
        return False
