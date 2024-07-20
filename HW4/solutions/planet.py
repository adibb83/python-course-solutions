import uuid


class Planet:
    def __init__(self, name: str, distance_from_earth: float, planet_id: str = None):
        self.id = planet_id or str(uuid.uuid4())
        self.name = name
        self.distance_from_earth = distance_from_earth
