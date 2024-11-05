"""This module contains the CooldownHandler class."""

from business.clock.clock import ClockSingleton

class CooldownHandler:
    """A handler for cooldowns."""

    def __init__(self, cooldown_time: int):
        self.clock = ClockSingleton()
        self.__last_action_time = self.clock.get_time()
        self.__cooldown_time = cooldown_time

    def is_action_ready(self):
        """Check if the action is ready to be performed."""
        current_time = self.clock.get_time()
        return current_time - self.__last_action_time >= self.__cooldown_time

    def put_on_cooldown(self):
        """Put the action on cooldown by updating the last action time."""
        self.__last_action_time = self.clock.get_time()

    def update_cooldown_time(self, new_time:int):
        self.__cooldown_time = new_time