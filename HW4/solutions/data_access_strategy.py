from mission import Mission
from spacecraft import Spacecraft
from typing import List
from system_enums import MissionStatus
from datetime import datetime, timedelta
from DB_Mock import BaronDB

class DataAccessFacade:
    baron_data_base: BaronDB = BaronDB()

    def __init__(self):
        # Initialize the facade with available spacecrafts and missions list from the database
        self.available_spacecrafts = self.baron_data_base.get_available_spacecrafts()
        self.missions_list = self.baron_data_base.get_missions_list()
        
    def get_spacecarft_by_id(self, id: int) -> Spacecraft:
        # Retrieve a spacecraft by its ID
        available_spacecrafts = self.baron_data_base.get_available_spacecrafts()
        for spacecraft in available_spacecrafts:
            if spacecraft.id == id:
                return spacecraft
    
    def get_available_spacecrafts(self) -> List[Spacecraft]:
        # Get a list of spacecrafts that are not currently assigned to an active mission
        available_spacecrafts = self.baron_data_base.get_available_spacecrafts()
        spacecrafts: list[Spacecraft] = []
        for spacecraft in available_spacecrafts:
            if not any(mission.spacecraft_id == spacecraft.id for mission in self.missions_list):
                spacecrafts.append(spacecraft)
            elif any(mission.spacecraft_id == spacecraft.id and (mission.status != MissionStatus.LAUNCHED) and (mission.status != MissionStatus.IN_TANSIT)  for mission in self.missions_list):
                spacecrafts.append(spacecraft)
        return spacecrafts
        
    def get_mission_by_id(self, id: int) -> Mission:
        # Retrieve a mission by its ID
        missions_list = self.baron_data_base.get_missions_list()
        for mission in missions_list:
            if mission.id == id:
                return mission

    def set_mission_status(self, id: int, status: str) -> None:
        # Update the status of a mission
        missions_list = self.baron_data_base.get_missions_list()
        for mission in missions_list:
            if mission.id == id:
                mission.status = status
                self.baron_data_base.update_mission(id, mission)
    
    
    def update_mission(self, mission_id: int, spacecraft_id: int = None, destination: int = None, distance: int = None, launch_date: datetime = None, status: str = None) -> bool:
    """
    Updates the details of an existing mission.

    Parameters:
    - mission_id (int): The ID of the mission to update.
    - spacecraft_id (int, optional): The new spacecraft ID for the mission.
    - destination (int, optional): The new destination ID for the mission.
    - distance (int, optional): The new distance for the mission.
    - launch_date (datetime, optional): The new launch date for the mission.
    - status (str, optional): The new status of the mission.

    Returns:
    - bool: True if the update was successful, False otherwise.
    """
    mission = self.get_mission_by_id(mission_id)
    if mission:
        if spacecraft_id is not None:
            mission.spacecraft_id = spacecraft_id
        if destination is not None:
            mission.destination = destination
        if distance is not None:
            mission.distance = distance
        if launch_date is not None:
            mission.launch_date = launch_date
        if status is not None:
            mission.status = status
        self.baron_data_base.update_mission(mission_id, mission)
        return True
    else:
        return False

    def get_missions_list(self) -> List[Mission]:
        # Get the list of all missions
        return self.baron_data_base.get_missions_list()
        
    def get_missions_by_status(self, status: str) -> List[Mission]:
        # Retrieve missions by their status
        return list(filter(lambda mission: mission.status == status, self.baron_data_base.get_missions_list()))
        
    def create_mission(self, spacecraft_id: int, destination: int, distance: int, launch_date: datetime = None) -> Mission:
        # Create a new mission with the given parameters
        missions_list = self.get_missions_list()
        id = len(missions_list) + 1
        if launch_date is not None:
            if not self.check_mission_date_availability(launch_date):
                raise ValueError(f"{launch_date} is already taken")
            if not self.check_spacecraft_availability(spacecraft_id):
                raise ValueError(f"Spacecraft with id {spacecraft_id} is not available")
        else:
            launch_date = self.find_next_available_launch_date()

        mission = Mission(id, launch_date, spacecraft_id, destination, distance)
        self.baron_data_base.create_mission(mission)
        return mission
        
    def check_mission_date_availability(self, launch_date: datetime) -> bool:
        # Check if the launch date is available for a new mission
        missions_list = self.baron_data_base.get_missions_list()
        for mission in missions_list:
            if mission.launch_date == launch_date:
                return False
        return True
        
    def check_spacecraft_availability(self, spacecraft_id: int) -> bool:
        # Check if the spacecraft is available for a new mission
        missions_list = self.baron_data_base.get_missions_list()
        for mission in missions_list:
            if mission.spacecraft_id == spacecraft_id and (mission.status != MissionStatus.LAUNCHED) and (mission.status != MissionStatus.IN_TANSIT):
                return False
        return True

    def get_mission_by_spacecraft_id(self, spacecraft_id: int) -> Mission:
        # Retrieve a mission by the spacecraft ID
        for mission in self.missions_list:
            if mission.spacecraft_id == spacecraft_id:
                return mission

    def find_next_available_launch_date(self, start_date: datetime = datetime.now()) -> datetime:
        # Find the next available date for launching a mission
        missions_list = self.sort_missions_by_date()
        current_date = start_date
        while True:
            if not any(mission.launch_date.date() == current_date.date() for mission in missions_list):
                return datetime(current_date.year, current_date.month, current_date.day, 16, 0, 0)
            current_date += timedelta(days=1)

    def sort_missions_by_date(self) -> List[Mission]:
        # Sort missions by their launch date
        missions_list = self.baron_data_base.get_missions_list()
        return sorted(missions_list, key=lambda x: x.launch_date)