"""Module for monster's persistence"""

from abc import ABC

class MonsterDao(ABC):
    """Represents monster's persistence"""
    def get_monsters(self):
        """Gets all the monsters from a persistency file
        """
    
    def save_monsters(self):
       """Adds the monsters to a persistency file
        """