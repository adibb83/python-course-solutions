from HW4.solutions.DB_Mock import BaronDB
from HW4.solutions.mission import Mission
from HW4.solutions.message import Message
from typing import List
from datetime import datetime, timedelta
from HW4.solutions.spacecraft import Spacecraft
from HW4.solutions.system_enums import MissionStatus
from final_project.main.communication_service import CommunicationService
import time
from threading import Thread

message_service = CommunicationService()


class DataAccessFacade:
    baron_data_base: BaronDB = BaronDB()

    def __init__(self):
        self.available_spacecrafts = self.baron_data_base.get_available_spacecrafts()
        self.missions_list = self.baron_data_base.get_missions_list()

    def get_spacecraft_by_id(self, spacecraft_id: int) -> Spacecraft:
        available_spacecrafts = self.baron_data_base.get_available_spacecrafts()
        for spacecraft in available_spacecrafts:
            if spacecraft.id == spacecraft_id:
                return spacecraft

    def get_available_spacecrafts(self) -> List[Spacecraft]:
        available_spacecrafts = self.baron_data_base.get_available_spacecrafts()
        spacecrafts: list[Spacecraft] = []
        for spacecraft in available_spacecrafts:
            if not any(mission.spacecraft_id == spacecraft.id for mission in self.missions_list):
                spacecrafts.append(spacecraft)
            elif any(mission.spacecraft_id == spacecraft.id and (mission.status != MissionStatus.LAUNCHED) and (
                    mission.status != MissionStatus.IN_TRANSIT) for mission in self.missions_list):
                spacecrafts.append(spacecraft)
        return spacecrafts

    def get_mission_by_id(self, mission_id: int) -> Mission:
        missions_list = self.baron_data_base.get_missions_list()
        for mission in missions_list:
            if mission.id == mission_id:
                return mission

    def set_mission_status(self, id: int, status: str) -> None:
        missions_list = self.baron_data_base.get_missions_list()
        for mission in missions_list:
            if mission.id == id:
                mission.status = status
                self.baron_data_base.update_mission(id, mission)
                message = Message('server', 'client', f'mission {id} status updated to {status}')
                message_service.send_message(message)
                if mission.status == MissionStatus.LAUNCHED:
                    self.start_mission_threaded(mission)

    def update_mission(self, mission_id: int, spacecraft_id: int = None, destination: int = None, distance: int = None,
                       launch_date: datetime = None, status: str = None) -> bool:
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
        return self.baron_data_base.get_missions_list()

    def get_missions_by_status(self, status: str) -> List[Mission]:
        return list(filter(lambda mission: mission.status == status, self.baron_data_base.get_missions_list()))

    def create_mission(self, mission: Mission) -> Mission:
        if mission.launch_date is not None:
            if not self.check_mission_date_availability(mission.launch_date):
                raise ValueError(f"{mission.launch_date} is already taken")
            if not self.check_spacecraft_availability(mission.spacecraft_id):
                raise ValueError(f"Spacecraft with id {mission.spacecraft_id} is not available")
        else:
            mission.launch_date = self.find_next_available_launch_date()

        self.baron_data_base.create_mission(mission)
        message = Message('server', 'client', f'mission {mission.id}  created')
        message_service.send_message(message)
        return mission

    def check_mission_date_availability(self, launch_date: datetime) -> bool:
        missions_list = self.baron_data_base.get_missions_list()
        for mission in missions_list:
            if mission.launch_date == launch_date:
                return False
        return True

    def check_spacecraft_availability(self, spacecraft_id: int) -> bool:
        missions_list = self.baron_data_base.get_missions_list()
        for mission in missions_list:
            if mission.spacecraft_id == spacecraft_id and (mission.status != MissionStatus.LAUNCHED) and (
                    mission.status != MissionStatus.IN_TRANSIT):
                return False
        return True

    def get_mission_by_spacecraft_id(self, spacecraft_id: int) -> Mission:
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

    def get_planet_by_id(self, planet_id: int):
        return self.baron_data_base.get_planet_by_id(planet_id)

    def start_mission_threaded(self, mission: Mission):
        mission_thread = Thread(target=self.start_mission, args=(mission,))
        mission_thread.start()

    def start_mission(self, mission: Mission):
        data_access_facade = DataAccessFacade()
        spacecraft = data_access_facade.get_spacecraft_by_id(mission.spacecraft_id)
        destination = data_access_facade.get_planet_by_id(mission.destination_id)
        spacecraft_distance = 0
        message = Message('server', 'client',f"Mission {mission.id} launched. Spacecraft {spacecraft.id} is on its way to {destination.name}")
        message_service.send_message(message)
        data_access_facade.set_mission_status(mission.id, MissionStatus.IN_TRANSIT)
        while mission.status != MissionStatus.COMPLETED:

            if destination.distance_from_earth <= spacecraft_distance:
                mission.status = MissionStatus.COMPLETED
                data_access_facade.update_mission(mission.id, mission)
                data_access_facade.set_mission_status(mission.id, mission.status)
                print(f"Mission {mission.id} completed")
                message = Message('server', 'client', f"Mission {mission.id} completed")
                message_service.send_message(message)
            else:
                time.sleep(1)
                spacecraft_distance += spacecraft.max_speed
                message = Message('server', 'client',
                                  f"Spacecraft {spacecraft.id} is {spacecraft_distance} units away from {destination.name}")
                message_service.send_message(message)
