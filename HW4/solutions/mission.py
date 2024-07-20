import uuid
from datetime import datetime
from HW4.solutions.system_enums import MissionStatus


class Mission:
    def __init__(self, launch_date: datetime, spacecraft_id: str, destination_id: str, status=MissionStatus.PLANNING):
        self.id = str(uuid.uuid4())
        self.launch_date = launch_date
        self.spacecraft_id = spacecraft_id
        self.destination_id = destination_id
        self.status = status
