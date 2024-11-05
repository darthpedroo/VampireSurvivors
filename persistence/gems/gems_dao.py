"""Module for gem's persistence"""

from abc import ABC

class GemsDao(ABC):
    """Represents gem's persistence"""
    def get_gems(self):
        """Gets all the gems from a persistency file
        """

    def add_gems(self):
        """Adds the gems to a persistency file
        """