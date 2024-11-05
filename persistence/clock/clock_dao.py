"""Module for clock's persistence"""
from abc import ABC
from business.clock.clock import ClockSingleton

class ClockDao(ABC):
    """Represents clock's persistence"""
    def get_clock(self):
        """Gets clock from persistency"""
    
    def save_clock(self, clock:ClockSingleton):
        """Saves clock to persistency"""

    