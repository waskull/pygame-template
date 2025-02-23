from enum import Enum

# ---- Window Variables ----

windowWidth = 1920
windowHeight = 1080
windowResolution = (windowWidth, windowHeight)
windowTitle = "Pygame Template"
windowFps = 60


# ---- States ----

class States(Enum):
    """The states of the game."""
    MAIN_MENU = "MAIN_MENU"


startingState = States.MAIN_MENU
