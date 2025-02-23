"""
Main Menu State.
This is the first state that is loaded.
"""

from States.base import BaseState
import pygame


class MainMenu(BaseState):
    """Main Menu."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the state."""
        super().__init__(*args, **kwargs)

    # you can override the functions from the base class here.

    # here we are overriding the render function, so we can draw something to the screen.
    def render(self, surface: pygame.Surface, *args, **kwargs) -> None:
        """
        Render the state.
        This is called every frame, and should be used for drawing to the screen.
        :param surface: The surface to draw to.
        :param args:
        :param kwargs:
        :return:
        """

        # we are filling the surface with red. This can also be done with surface.fill("red").
        surface.fill((255, 0, 0))
