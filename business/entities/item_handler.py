from abc import ABC, abstractmethod
from business.entities.interfaces import UpgradableItem

class ItemHandler(ABC):
    def __init__(self, list_of_items: list = [UpgradableItem], max_items=5):
        self._list_of_items = list_of_items
        self.max_items = max_items
    
    def get_all_items(self):
        return self._list_of_items
    
    def has_item(self, item_name:str):
        for item in self._list_of_items:
            if item.item_name == item_name:
                return True
        return False
    
    def get_item_level(self, item_name:str):
        for item in self._list_of_items:
            if item.item_name == item_name:
                return item._level
        raise ValueError
    
    def upgrade_item_next_level(self, item_name: str):
        for item in self._list_of_items:
            if item.item_name == item_name:
                item.upgrade_next_level(item.item_stats)
                return True # Exit the function after upgrading the item
        # If the loop completes without finding the item, raise ValueError
        raise ValueError(f"Item with name '{item_name}' not found")

    
    def has_reached_max_level(self, item_name:str):
        for item in self._list_of_items:
            if item.item_name == item_name:
                return item.has_reached_max_level()
        
    
    @abstractmethod
    def add_item(self):
        pass