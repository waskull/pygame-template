"""
Pygame Template
by Y9K

This is a template for pygame projects.
It includes the game loop, a state manager, and a few basic tools.

Made for Python 3.10
"""

from States.state_manager import StateManager
import config
import globs
import pygame


class MainLoop:
    """The main loop for the window."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the main loop."""
        self.window = pygame.display.set_mode(config.windowResolution)
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = config.windowFps
        self.stateManager = StateManager()

        globs.mainWindow = self
        globs.stateManager = self.stateManager

        pygame.display.set_caption(config.windowTitle)

    def main_loop(self) -> None:
        """The main loop."""

        while self.running:
            globs.dt = self.clock.tick(self.fps)

            self.handle_events()
            self.update()
            self.render()

    def handle_events(self) -> None:
        """Handle events for the window."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            self.stateManager.handle_event(event)

    def update(self) -> None:
        """Update the window."""
        self.stateManager.update()

    def render(self) -> None:
        """Render the window."""

        self.stateManager.render(self.window)

        pygame.display.flip()


def main() -> None:
    """The main function."""
    if not pygame.get_init():
        pygame.init()

    mainWindow = MainLoop()
    mainWindow.main_loop()

    pygame.quit()


if __name__ == "__main__":
    main()

else:
    raise ImportError("This module is not meant to be imported.")
