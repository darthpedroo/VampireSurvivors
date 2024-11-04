"""Module used for the in-game clock"""

import pygame
import settings

class ClockSingleton:
    """Defines the clock of the game"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ClockSingleton, cls).__new__(cls)
            cls._instance.clock = pygame.time.Clock()
            cls._instance.__ms = 0
            cls._instance.__fps = settings.FPS
            cls._instance.__paused = False

        return cls._instance

    def tick(self):
        """Makes the clock advance by a specific frame rate.
        
        Returns:
           tick: The number of ms passed since the last frame.
        """
        if not self.__paused:
            tick = self.clock.tick(self.__fps)
            self.__ms += tick
            return tick
        else:
            # When paused, just call tick() without advancing __ms
            self.clock.tick(self.__fps)
            return 0

    def set_paused(self, state: bool):
        """Pauses or unpauses the clock.
        
        Args:
            state: True to pause the clock, False to unpause.
        """
        self.__paused = state

    def get_time(self):
        """Gets the total time of the game in milliseconds.

        Returns:
            time: The total time of the game.
        """
        return self.__ms
