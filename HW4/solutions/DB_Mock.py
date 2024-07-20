from HW4.solutions.mission import Mission
from HW4.solutions.planet import Planet
from HW4.solutions.spacecraft import Spacecraft
from HW4.solutions.system_enums import SpacecraftName, SpacecraftSize, Target, MissionStatus
from typing import List
from datetime import datetime
import random
from HW4.solutions.message import Message
from final_project.main.communication_service import CommunicationService

message_service = CommunicationService()




class BaronDB:
    def __init__(self):

        self.available_planets_Mock = [
            Planet(Target.MARS, 0.39, "1"),
            Planet(Target.VENUS, 0.72, "2"),
            Planet(Target.EARTH, 1 , "3"),
            Planet(Target.JUPITER, 1.52, "4"),
            Planet(Target.SATURN, 5.20, "5"),
            Planet(Target.PLUTO, 9.58, "6"),
            Planet(Target.URANUS, 19.22,"7" ),
            Planet(Target.MERCURY, 30.05,"8"),
            Planet(Target.SUN, 14.05 , "9"),
            Planet(Target.NEPTUNE, 44.05 , "10"),
            Planet(Target.MOON, 0.00257 , "11")
        ]

        self.available_spacecrafts_Mock = [
            Spacecraft(SpacecraftName.APOLLO, 2, 1969, SpacecraftSize.SMALL, "1"),
            Spacecraft(SpacecraftName.ARTEMIS, 5, 2024, SpacecraftSize.MEDIUM, "2"),
            Spacecraft(SpacecraftName.ORION, 3, 2014, SpacecraftSize.MEDIUM, "3"),
            Spacecraft(SpacecraftName.DRAGON, 2, 2010, SpacecraftSize.LARGE, "4"),
            Spacecraft(SpacecraftName.STARSHIP, 7, 2021, SpacecraftSize.LARGE, "5")
        ]
        self.missions_list_Mock = [
            Mission(self.set_random_date(), self.available_spacecrafts_Mock[1].id, self.available_planets_Mock[1].id, MissionStatus.IN_TRANSIT),
            Mission(self.set_random_date(), self.available_spacecrafts_Mock[2].id, self.available_planets_Mock[2].id, MissionStatus.LAUNCHED),
            Mission(self.set_random_date(), self.available_spacecrafts_Mock[3].id, self.available_planets_Mock[4].id,  MissionStatus.PLANNING),
            Mission(self.set_random_date(), self.available_spacecrafts_Mock[4].id, self.available_planets_Mock[3].id,  MissionStatus.PLANNING)
        ]

        self.massage_list_Mock = []

    def get_available_planets(self) -> List[Planet]:
        return self.available_planets_Mock

    def get_planet_by_id(self, planet_id: int) -> Planet:
        for planet in self.available_planets_Mock:
            if planet.id == planet_id:
                return planet
    def create_message(self, message: Message) -> None:
        try:
            self.massage_list_Mock.append(message)
        except Exception as e:
            print(f"Failed to create message: {e}")

    def create_mission(self, mission: Mission) -> None:
        try:
            self.missions_list_Mock.append(mission)
        except Exception as e:
            print(f"Failed to create mission: {e}")

    def read_mission(self, mission_id: int):
        try:
            for mission in self.missions_list_Mock:
                if mission.id == mission_id:
                    return mission
        except Exception as e:
            print(f"Failed to read mission with ID {mission_id}: {e}")
        return None

    def update_mission(self, mission_id: int, new_mission) -> bool:
        try:
            for i, mission in enumerate(self.missions_list_Mock):
                if mission.id == mission_id:
                    self.missions_list_Mock[i] = new_mission
                    return True
        except Exception as e:
            print(f"Failed to update mission with ID {mission_id}: {e}")
        return False

    def delete_mission(self, mission_id: int) -> bool:
        try:
            for i, mission in enumerate(self.missions_list_Mock):
                if mission.id == mission_id:
                    del self.missions_list_Mock[i]
                    return True
        except Exception as e:
            print(f"Failed to delete mission with ID {mission_id}: {e}")
        return False

    def create_spacecraft(self, spacecraft: Spacecraft) -> None:
        try:
            self.available_spacecrafts_Mock.append(spacecraft)
        except Exception as e:
            print(f"Failed to create spacecraft: {e}")

    def read_spacecraft(self, spacecraft_id: int):
        try:
            for spacecraft in self.available_spacecrafts_Mock:
                if spacecraft.id == spacecraft_id:
                    return spacecraft
        except Exception as e:
            print(f"Failed to read spacecraft with ID {spacecraft_id}: {e}")
        return None

    def update_spacecraft(self, spacecraft_id: int, new_spacecraft: Spacecraft) -> bool:
        try:
            for i, spacecraft in enumerate(self.available_spacecrafts_Mock):
                if spacecraft.id == spacecraft_id:
                    self.available_spacecrafts_Mock[i] = new_spacecraft
                    return True
        except Exception as e:
            print(f"Failed to update spacecraft with ID {spacecraft_id}: {e}")
        return False

    def delete_spacecraft(self, spacecraft_id: int) -> bool:
        try:
            for i, spacecraft in enumerate(self.available_spacecrafts_Mock):
                if spacecraft.id == spacecraft_id:
                    del self.available_spacecrafts_Mock[i]
                    return True
        except Exception as e:
            print(f"Failed to delete spacecraft with ID {spacecraft_id}: {e}")
        return False

    def get_available_spacecrafts(self) -> List[Spacecraft]:
        return self.available_spacecrafts_Mock

    def get_missions_list(self) -> List[Mission]:
        return self.missions_list_Mock

    @staticmethod
    def set_random_date() -> datetime:
        try:
            year = random.randint(2000, 2025)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            return datetime(year, month, day, hour, minute, second)
        except Exception as e:
            print(f"Failed to generate random date: {e}")
            return datetime.now()
