import uuid
import datetime

class Event:
    def __init__(self,event_name,capacity):
        self.event_name = event_name
        self.maximum_participant = capacity
        self.event_id = uuid.uuid4()
        self.date = datetime.datetime.utcnow()
    
    def __str__(self) -> str:
        return f"{self.event_id} - {self.event_id}"
    