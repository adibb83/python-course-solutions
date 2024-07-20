from datetime import datetime
from HW4.solutions.data_access_strategy import DataAccessFacade
from HW4.solutions.mission import Mission
from HW4.solutions.system_enums import MissionStatus

data_access_facade = DataAccessFacade()


class MissionControlService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MissionControlService, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.missions = {}
        self.spacecraft = {}
        self.__initialized = True

    def plan_mission(self, mission: Mission):
        data_access_facade.create_mission(mission)

    def launch_mission(self, mission_id):
        data_access_facade.set_mission_status(mission_id, MissionStatus.LAUNCHED)

    def get_mission_status(self, mission_id):
       mission = data_access_facade.get_mission_by_id(mission_id)
       print(f"Mission {mission_id} status: {mission.status}")


    def get_spacecraft_status(self, spacecraft_id):
        mission = data_access_facade.get_mission_by_spacecraft_id(spacecraft_id)
        if mission:
            print(f"Spacecraft {spacecraft_id} status: {mission.status}")
        else:
            print(f"Spacecraft {spacecraft_id} status: UNASSIGNED")


mission_control_service = MissionControlService()
new_mission: Mission = Mission(spacecraft_id="1", destination_id="10", launch_date=datetime.now(), status="PLANNED")
mission_control_service.plan_mission(new_mission)
mission_control_service.launch_mission(new_mission.id)
