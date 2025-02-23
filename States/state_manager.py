"""
The state manager to control the states.
"""

import pygame
import config
import globs

from States.base import BaseState
from States.main_menu import MainMenu


class StateManager:
    """State manager class."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the state manager."""
        self._states = {
            config.States.MAIN_MENU: MainMenu()
        }

        self._currentState = None

        try:
            self._currentState = self._states[config.startingState]
        except KeyError:
            raise ValueError(f"State {config.startingState} does not exist. Please check the config file.")

    def set_state(self, state: config.States, resetPrevious: bool = True, resetNew: bool = True) -> None:
        """
        Set the current state.
        :param state: The state to set.
        :param resetPrevious: Whether to reset the previous state.
        :param resetNew: Whether to reset the new state.
        :raises ValueError: If the state is not in the states dictionary.
        :raises TypeError: If the state is not a config.States enum.
        :raises TypeError: If the reset prev/new arguments are not bools.
        :return:
        """

        # check types
        if not isinstance(state, config.States):
            raise TypeError("state must be a config.States enum.")

        if not isinstance(resetPrevious, bool):
            raise TypeError("resetPrevious must be a bool.")

        if not isinstance(resetNew, bool):
            raise TypeError("resetNew must be a bool.")

        # check if the state is in the states dictionary

        if state not in self._states:
            raise ValueError(f"state {state} is not in the states dictionary.")

        # reset the previous state
        if resetPrevious:
            self._currentState.reset()

        # set the current state
        self._currentState = self._states[state]

        # reset the new state
        if resetNew:
            self._currentState.reset()

    def get_state(self) -> BaseState:
        """
        Get the current state.
        :return: The current state.
        """
        return self._currentState

    def get_all_states(self) -> dict[config.States, BaseState]:
        """
        Get all the states.
        :return: All the states.
        """
        return self._states

    def update(self, *args, **kwargs) -> None:
        """
        Update the state manager, which updates the current state.
        This is called every frame, and should be used for updating positions, colors, etc.
        This function should not be used for rendering/drawing to the screen.
        :param args:
        :param kwargs:
        :return:
        """
        self._currentState.update(*args, **kwargs)

    def render(self, surface: pygame.Surface, *args, **kwargs) -> None:
        """
        Render the state manager, which renders the current state.
        This is called every frame, and should be used for drawing to the screen.
        :param surface: The surface to draw to.
        :param args:
        :param kwargs:
        :return:
        """
        self._currentState.render(surface, *args, **kwargs)

    def handle_event(self, event: pygame.event.Event, *args, **kwargs) -> None:
        """
        Handle an event.
        This is called for every single event.
        :param event: The event to handle.
        :param args:
        :param kwargs:
        :return:
        """
        self._currentState.handle_event(event, *args, **kwargs)
