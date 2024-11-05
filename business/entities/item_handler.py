"""Module that contains the Item Handler"""

from abc import ABC, abstractmethod
from business.entities.interfaces import UpgradableItem

class ItemHandler(ABC):
    """Represents the Item Handler"""

    def __init__(self, list_of_items: list[UpgradableItem] = [UpgradableItem], max_items: int = 5):
        self._list_of_items = list_of_items
        self.max_items = max_items

    def get_all_items(self) -> list[UpgradableItem]:
        """Returns all items in the handler.

        Returns:
            list[UpgradableItem]: A list of all items.
        """
        return self._list_of_items

    def has_item(self, item_name: str) -> bool:
        """Checks if the specified item exists.

        Args:
            item_name (str): Name of the item to check.

        Returns:
            bool: True if the item exists, False otherwise.
        """
        for item in self._list_of_items:
            if item.item_name == item_name:
                return True
        return False

    def get_item_level(self, item_name: str) -> int:
        """Retrieves the level of the specified item.

        Args:
            item_name (str): Name of the item.

        Returns:
            int: The level of the item.

        Raises:
            ValueError: If the item is not found.
        """
        for item in self._list_of_items:
            if item.item_name == item_name:
                return item._level
        raise ValueError(f"Item with name '{item_name}' not found")

    def upgrade_item_next_level(self, item_name: str) -> bool:
        """Upgrades the specified item to the next level.

        Args:
            item_name (str): Name of the item to upgrade.

        Returns:
            bool: True if the upgrade was successful.

        Raises:
            ValueError: If the item is not found.
        """
        for item in self._list_of_items:
            if item.item_name == item_name:
                item.upgrade_next_level(item._upgrades, item.item_stats)
                return True
        raise ValueError(f"Item with name '{item_name}' not found")

    def has_reached_max_level(self, item_name: str) -> bool:
        """Checks if the specified item has reached its maximum level.

        Args:
            item_name (str): Name of the item to check.

        Returns:
            bool: True if the item has reached max level, False otherwise.

        Raises:
            ValueError: If the item is not found.
        """
        for item in self._list_of_items:
            if item.item_name == item_name:
                return item.has_reached_max_level()

    @abstractmethod
    def add_item(self, item_name: str):
        """Adds item to the player.
        
        Args:
            item_name (str): Name of the item.
        """
