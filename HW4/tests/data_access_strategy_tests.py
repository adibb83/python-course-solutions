import unittest
from HW4.solutions.data_access_strategy import DataAccessFacade
from HW4.solutions.spacecraft import Spacecraft
from HW4.solutions.mission import Mission
from HW4.solutions.system_enums import MissionStatus
from datetime import datetime, timedelta


class TestDataAccessFacade(unittest.TestCase):
    def setUp(self):
        self.facade = DataAccessFacade()
        # Mock data setup
        self.mock_spacecraft = Spacecraft(id=1, name="MockCraft", max_speed=10000)
        self.mock_mission = Mission(id=1, spacecraft_id=1, destination_id=1, distance=100000,
                                    launch_date=datetime.now(), status=MissionStatus.PLANNED)
        self.facade.baron_data_base.create_spacecraft(self.mock_spacecraft)
        self.facade.baron_data_base.create_mission(self.mock_mission)

    def test_get_spacecraft_by_id(self):
        spacecraft = self.facade.get_spacecraft_by_id(1)
        self.assertIsNotNone(spacecraft)
        self.assertEqual(spacecraft.id, 1)

    def test_get_available_spacecrafts(self):
        available_spacecrafts = self.facade.get_available_spacecrafts()
        self.assertTrue(len(available_spacecrafts) > 0)
        self.assertIn(self.mock_spacecraft, available_spacecrafts)

    def test_get_mission_by_id(self):
        mission = self.facade.get_mission_by_id(1)
        self.assertIsNotNone(mission)
        self.assertEqual(mission.id, 1)

    def test_set_mission_status(self):
        self.facade.set_mission_status(1, MissionStatus.COMPLETED)
        mission = self.facade.get_mission_by_id(1)
        self.assertEqual(mission.status, MissionStatus.COMPLETED)

    def test_update_mission(self):
        success = self.facade.update_mission(1, status=MissionStatus.COMPLETED)
        self.assertTrue(success)
        mission = self.facade.get_mission_by_id(1)
        self.assertEqual(mission.status, MissionStatus.COMPLETED)

    def test_create_mission(self):
        new_mission = Mission(id=2, spacecraft_id=1, destination_id=1, distance=100000,
                              launch_date=datetime.now() + timedelta(days=1), status=MissionStatus.PLANNED)
        created_mission = self.facade.create_mission(new_mission)
        self.assertIsNotNone(created_mission)
        self.assertEqual(created_mission.id, 2)

    # Add more tests for other methods...

    def tearDown(self):
        # Clean up code if necessary
        pass


if __name__ == '__main__':
    unittest.main()
