"""Module that contains the WeaponHandler"""

from business.exceptions import ItemOverflow
from business.world.interfaces import IGameWorld
from business.weapons.weapon_factory import WeaponFactory
from business.entities.item_handler import ItemHandler


class WeaponHandler(ItemHandler):

    """Clase que permite manejar las distintas armas del jugador
    """

    def __init__(self, list_of_items =[] , max_items=5):
        super().__init__(list_of_items, max_items)

    def create_weapon_handler_json_data(self):
        
        list_of_items_data = []
        for item in self._list_of_items:
            list_of_items_data.append(item.create_weapon_json_data())
        weapon_handler_data = {"list_of_items": list_of_items_data, "max_items": self.max_items}
        return weapon_handler_data
    
    def add_item(self, item_name: str):
        if len(self._list_of_items) < self.max_items:
            weapon_factory = WeaponFactory()
            weapon = weapon_factory.create_weapon(item_name)
            self._list_of_items.append(weapon)
        else:
            raise ItemOverflow()

    def use_every_weapon(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time, player_base_damage_multiplier:int, player_base_attack_speed_multiplier:int):
        """Uses all the weapon the player has.
        
        Args:
            player_pos_x (int): The position of the player on the x axis.
            player_pos_y (int): The position of the player on the y axis.
            world (IGameWorld): The game world.
            current_time: The current time.
            player_base_damage_multiplier (int): The player base damage multiplier.
            player_base_attack_speed_multiplier (int): The player base attack speed multiplier.
        """
        for weapon in self._list_of_items:
            weapon.use(player_pos_x, 
                       player_pos_y,
                       world,
                       current_time,
                       player_base_damage_multiplier,
                       player_base_attack_speed_multiplier)
