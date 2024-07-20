from enum import Enum


class Target(Enum):
    MERCURY = "MERCURY"
    VENUS = "VENUS"
    EARTH = "EARTH"
    MARS = "MARS"
    JUPITER = "JUPITER"
    SATURN = "SATURN"
    URANUS = "URANUS"
    NEPTUNE = "NEPTUNE"
    PLUTO = "PLUTO"
    MOON = "MOON"
    SUN = "SUN"


class MissionStatus(Enum):
    PLANNING = "PLANNING"
    LAUNCHED = "LAUNCHED"
    IN_TRANSIT = "IN_TRANSIT"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"


class SpacecraftName(Enum):
    APOLLO = "APOLLO"
    ARTEMIS = "ARTEMIS"
    ORION = "ORION"
    DRAGON = "DRAGON"
    STARSHIP = "STARSHIP"


class SpacecraftSize(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
