import unittest
from datetime import datetime
from HW4.solutions.data_access_strategy import DataAccessFacade
from HW4.solutions.mission import Mission
from HW4.solutions.system_enums import MissionStatus
from final_project.main.mission_control_service import MissionControlService

class TestMissionControlService(unittest.TestCase):
    def setUp(self):
        self.mission_control_service = MissionControlService()
        self.data_access_facade = DataAccessFacade()
        # Assuming DataAccessFacade is already tested and works as expected
        # Setup mock data for missions and spacecrafts
        self.test_mission = Mission(spacecraft_id=1, destination_id=10, launch_date=datetime.now(), status=MissionStatus.PLANNED)
        self.data_access_facade.create_mission(self.test_mission)

    def test_plan_mission(self):
        self.mission_control_service.plan_mission(self.test_mission)
        # Verify the mission was planned correctly
        retrieved_mission = self.data_access_facade.get_mission_by_id(self.test_mission.id)
        self.assertIsNotNone(retrieved_mission)
        self.assertEqual(retrieved_mission.status, MissionStatus.PLANNED)

    def test_launch_mission(self):
        self.mission_control_service.launch_mission(self.test_mission.id)
        # Verify the mission status is updated to LAUNCHED
        updated_mission = self.data_access_facade.get_mission_by_id(self.test_mission.id)
        self.assertEqual(updated_mission.status, MissionStatus.LAUNCHED)

    def test_get_mission_status(self):
        # This test will need to capture printed output if checking for print statements
        # Alternatively, refactor get_mission_status to return status instead of printing
        pass

    def test_get_spacecraft_status(self):
        # Similar to test_get_mission_status, this depends on the implementation details
        pass

    def tearDown(self):
        # Clean up code if necessary
        pass

if __name__ == '__main__':
    unittest.main()