"""
Base class for all states.
"""

import pygame


class BaseState:
    """Base state class."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the state."""

        # state variables to be initialized ONCE.

        self.reset()

    def reset(self, *args, **kwargs) -> None:
        """
        Reset the state, and all the variables that need to be reset.
        :param args:
        :param kwargs:
        :return:
        """

        # state variables to be initialized every time the state is reset.
        pass

    def update(self, *args, **kwargs) -> None:
        """
        Update the state.
        This is called every frame, and should be used for updating positions, colors, etc.
        This function should not be used for rendering/drawing to the screen.
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def render(self, surface: pygame.Surface, *args, **kwargs) -> None:
        """
        Render the state.
        This is called every frame, and should be used for drawing to the screen.
        :param surface: The surface to draw to.
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def handle_event(self, event: pygame.event.Event, *args, **kwargs) -> None:
        """
        Handle an event.
        This is called for every single event.
        :param event: The event to handle.
        :param args:
        :param kwargs:
        :return:
        """
        pass
