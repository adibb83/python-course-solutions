from enum import Enum

class Target(Enum):
    MERCURY = 1
    VENUS = 2
    EARTH = 3
    MARS = 4
    JUPITER = 5
    SATURN = 6
    URANUS = 7
    NEPTUNE = 8
    PLUTO = 9
    MOON = 10
    SUN = 11

class MissionStatus(Enum):
    PLANNING = 1
    LAUNCHED = 2
    IN_TANSIT = 3
    COMPLITED = 4
    CANCELED = 5

class SpacecraftName(Enum):
    APOLLO = 1
    ARTEMIS = 2
    ORION = 3
    DRAGON = 4
    STARSHIP = 5

class SpacecraftSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3