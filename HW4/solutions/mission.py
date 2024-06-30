from system_enums import MissionStatus

class Mission:
    def __init__(self, mission_id, launch_date, spacecraft_id, destination, distance, status = MissionStatus.PLANNING):
        self.id = mission_id
        self.Launch_Date = launch_date
        self.spacecraft_id = spacecraft_id
        self.destination = destination
        self.distance = distance
        self.status = status
