"""Module for player's persistence"""

from abc import ABC

class PlayerDao(ABC):
    """Represents player's persistence"""
    def get_player(self):
        """Gets the player from a persistency file
        """
    
    def save_player(self):
        """Adds the player to a persistency file
        """