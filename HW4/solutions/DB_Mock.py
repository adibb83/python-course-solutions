class BaronDB:
    def __init__(self):
        """
        Initializes the mock database with predefined spacecrafts and missions.
        """
        self.available_spacecrafts_Mock = [
            Spacecraft(SpacecraftName.APOLLO, 25000, 1969, SpacecraftSize.SMALL, 1),
            Spacecraft(SpacecraftName.ARTEMIS, 50000, 2024, SpacecraftSize.MEDIUM, 2),
            Spacecraft(SpacecraftName.ORION, 30000, 2014, SpacecraftSize.MEDIUM, 3),
            Spacecraft(SpacecraftName.DRAGON, 20000, 2010, SpacecraftSize.LARGE, 4),
            Spacecraft(SpacecraftName.STARSHIP, 70000, 2021, SpacecraftSize.LARGE, 5)
        ]
        self.missions_list_Mock = [
            Mission(1, self.set_random_date(), 1, Target.MARS, 1000000, MissionStatus.COMPLITED),
            Mission(2, self.set_random_date(), 2, Target.VENUS, 500000, MissionStatus.IN_TANSIT),
            Mission(3, self.set_random_date(), 3, Target.JUPITER, 2000000, MissionStatus.LAUNCHED),
            Mission(4, self.set_random_date(), 4, Target.SATURN, 3000000, MissionStatus.PLANNING),
            Mission(5, self.set_random_date(), 5, Target.URANUS, 4000000, MissionStatus.PLANNING)
        ]

    def create_mission(self, mission: Mission) -> None:
        """
        Adds a new mission to the missions list.

        Parameters:
        - mission (Mission): The mission object to be added.
        """
        try:
            self.missions_list_Mock.append(mission)
        except Exception as e:
            print(f"Failed to create mission: {e}")

    def read_mission(self, mission_id: int):
        """
        Retrieves a mission by its ID.

        Parameters:
        - mission_id (int): The ID of the mission to retrieve.

        Returns:
        - Mission: The mission object if found, None otherwise.
        """
        try:
            for mission in self.missions_list_Mock:
                if mission.id == mission_id:
                    return mission
        except Exception as e:
            print(f"Failed to read mission with ID {mission_id}: {e}")
        return None

    def update_mission(self, mission_id: int, new_mission) -> bool:
        """
        Updates a mission in the missions list.

        Parameters:
        - mission_id (int): The ID of the mission to update.
        - new_mission (Mission): The new mission object to replace the old one.

        Returns:
        - bool: True if the update was successful, False otherwise.
        """
        try:
            for i, mission in enumerate(self.missions_list_Mock):
                if mission.id == mission_id:
                    self.missions_list_Mock[i] = new_mission
                    return True
        except Exception as e:
            print(f"Failed to update mission with ID {mission_id}: {e}")
        return False

    def delete_mission(self, mission_id: int) -> bool:
        """
        Deletes a mission from the missions list.

        Parameters:
        - mission_id (int): The ID of the mission to delete.

        Returns:
        - bool: True if the deletion was successful, False otherwise.
        """
        try:
            for i, mission in enumerate(self.missions_list_Mock):
                if mission.id == mission_id:
                    del self.missions_list_Mock[i]
                    return True
        except Exception as e:
            print(f"Failed to delete mission with ID {mission_id}: {e}")
        return False

    def create_spacecraft(self, spacecraft: Spacecraft) -> None:
        """
        Adds a new spacecraft to the available spacecrafts list.

        Parameters:
        - spacecraft (Spacecraft): The spacecraft object to be added.
        """
        try:
            self.available_spacecrafts_Mock.append(spacecraft)
        except Exception as e:
            print(f"Failed to create spacecraft: {e}")

    def read_spacecraft(self, spacecraft_id: int):
        """
        Retrieves a spacecraft by its ID.

        Parameters:
        - spacecraft_id (int): The ID of the spacecraft to retrieve.

        Returns:
        - Spacecraft: The spacecraft object if found, None otherwise.
        """
        try:
            for spacecraft in self.available_spacecrafts_Mock:
                if spacecraft.id == spacecraft_id:
                    return spacecraft
        except Exception as e:
            print(f"Failed to read spacecraft with ID {spacecraft_id}: {e}")
        return None

    def update_spacecraft(self, spacecraft_id: int, new_spacecraft: Spacecraft) -> bool:
        """
        Updates a spacecraft in the available spacecrafts list.

        Parameters:
        - spacecraft_id (int): The ID of the spacecraft to update.
        - new_spacecraft (Spacecraft): The new spacecraft object to replace the old one.

        Returns:
        - bool: True if the update was successful, False otherwise.
        """
        try:
            for i, spacecraft in enumerate(self.available_spacecrafts_Mock):
                if spacecraft.id == spacecraft_id:
                    self.available_spacecrafts_Mock[i] = new_spacecraft
                    return True
        except Exception as e:
            print(f"Failed to update spacecraft with ID {spacecraft_id}: {e}")
        return False

    def delete_spacecraft(self, spacecraft_id: int) -> bool:
        """
        Deletes a spacecraft from the available spacecrafts list.

        Parameters:
        - spacecraft_id (int): The ID of the spacecraft to delete.

        Returns:
        - bool: True if the deletion was successful, False otherwise.
        """
        try:
            for i, spacecraft in enumerate(self.available_spacecrafts_Mock):
                if spacecraft.id == spacecraft_id:
                    del self.available_spacecrafts_Mock[i]
                    return True
        except Exception as e:
            print(f"Failed to delete spacecraft with ID {spacecraft_id}: {e}")
        return False

    def get_available_spacecrafts(self) -> List[Spacecraft]:
        """
        Retrieves the list of available spacecrafts.

        Returns:
        - List[Spacecraft]: The list of available spacecrafts.
        """
        return self.available_spacecrafts_Mock

    def get_missions_list(self) -> List[Mission]:
        """
        Retrieves the list of missions.

        Returns:
        - List[Mission]: The list of missions.
        """
        return self.missions_list_Mock

    def set_random_date(self) -> datetime:
        """
        Generates a random datetime.

        Returns:
        - datetime: A randomly generated datetime.
        """
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
            return datetime.now()  # Fallback to current time