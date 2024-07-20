import uuid


class Spacecraft:
    def __init__(self, name: str, max_speed: int, year: int, size: str, spacecraft_id: str = None):
        self.name = name
        self.max_speed = max_speed
        self.year = year
        self.size = size
        self.id = spacecraft_id or str(uuid.uuid4())
