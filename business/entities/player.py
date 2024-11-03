"""Player entity module."""

import pygame

from business.entities.state_machine.entity import MovableEntity
from business.entities.experience_gem import ExperienceGem
from business.entities.interfaces import ICanDealDamage, IDamageable, IPlayer
from business.world.interfaces import IGameWorld
from business.entities.weapon_handler import WeaponHandler
from business.perks.perks_handler import PerksHandler
from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState
from business.stats.stats import PlayerStats
from presentation.sprite import Sprite
#from business.perks.perk import Perk
#from business.perks.perk_factory import PerkFactory

class Player(MovableEntity, IPlayer, IDamageable, ICanDealDamage):
    """Player entity.

    The player is the main character of the game. It can move around the game world and shoot at monsters.

    Args:
        pos_x (int): Position of the player on the x axis.
        pos_y (int): Position of the player on the y axis.
        sprite (Sprite): Sprite of the player.
        player_stats (PlayerStats): Stats of the player.
    """ #pylint: disable=line-too-long
    def __init__(self, pos_x: int, pos_y: int, sprite: Sprite, player_stats: PlayerStats):
        super().__init__(pos_x, pos_y, player_stats, sprite)

        self.__health: int = self._stats.max_health
        self.__experience = 0
        self.__level = 1
        self.__last_regeneration_time = 0
        self._weapon_handler = WeaponHandler()
        self._perks_handler = PerksHandler(self._stats)
        self.__upgrading = False

    def get_player_weapons(self) -> list:
        """Gets the player weapons.

        Returns:
            list: A list of the player weapons.
        """
        return self._weapon_handler.get_all_items()

    def get_player_perks(self):
        """Gets the player perks.

        Returns:
            list: A list of the player perks.
        """
        return self._perks_handler.get_all_items()

    def add_item(self, item_name: str):
        """Adds an item to the player.

        Args:
            item_name (str): The name of the item.
        """
        self.__upgrading = False
        try:
            self._weapon_handler.add_item(item_name)
        except ValueError:
            self._perks_handler.add_item(item_name, self._stats)
            self._perks_handler.apply_perk_to_player_stats(item_name, self._stats)

    def has_item(self, item_name: str):
        """Checks if the player has an item.

        Args:
            item_name (str): The name of the item.

        Returns:
            bool: True if the player has the item, false otherwise.
        """
        return self._weapon_handler.has_item(item_name) or self._perks_handler.has_item(item_name)

    def get_item_level(self, item_name: str):
        """Gets the level of an item.

        Args:
            item_name (str): The name of the item.

        Returns:
            item_level: The level of the item.
        """
        try:
            return self._weapon_handler.get_item_level(item_name)
        except ValueError:
            return self._perks_handler.get_item_level(item_name)

    def upgrade_item_next_level(self, item_name: str):
        """Upgrades the level of an item.

        Args:
            item_name (str): The name of the item.

        Returns:
            bool: True after upgrading the item.

        Raises:
            ValueError: If the item could not be upgraded
        """
        try:
            # Try upgrading the item with weapon handler
            return self._weapon_handler.upgrade_item_next_level(item_name)
        except ValueError:
            # If it fails, try upgrading with perks handler
            success = self._perks_handler.upgrade_item_next_level(item_name)
            # Apply perk if the upgrade was successful
            if success:
                self._perks_handler.apply_perk_to_player_stats(item_name, self._stats)
                return success
            else:
                # Raise an error if neither handler can upgrade the item
                raise ValueError(f"Item '{item_name}' could not be upgraded by any handler")

    def item_reached_max_level(self, item_name: str):
        """Checks if an item has reached max level.

        Args:
            item_name (str): The name of the item.

        Returns:
            bool
        """
        return self._weapon_handler.has_reached_max_level(item_name) or self._perks_handler.has_reached_max_level(item_name) #pylint: disable=line-too-long

    def __str__(self):
        return f"Player(hp={self.__health}, xp={self.__experience}, lvl={self.__level}, pos=({self._pos_x}, {self._pos_y}))" #pylint: disable=line-too-long

    def set_position(self, pos_x: int, pos_y: int):
        """Sets the position of the player.

        Args:
            pos_x (int): The position of the player on the x axis.
            pos_y (int): The position of the player on the y axis.
        """
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_upgrading(self, new_state: bool):
        """Sets the upgrading state.

        Args:
            new_state (bool): The state of upgrading (true or false).
        """
        self.__upgrading = new_state

    @property
    def pos_x(self) -> float:
        return self._pos_x

    @pos_x.setter
    def pos_x(self, value: float) -> None:
        self._pos_x = value

    @property
    def pos_y(self) -> float:
        return self._pos_y

    @pos_y.setter
    def pos_y(self, value: float) -> None:
        self._pos_y = value

    @property
    def experience(self):
        return self.__experience

    @property
    def experience_to_next_level(self):
        return 5 + (2*self.__level)**2

    @property
    def level(self):
        return self.__level

    @property
    def damage_amount(self):
        return self._stats.base_damage_multiplier

    @property
    def health(self) -> int:
        return self.__health

    @property
    def luck(self) -> int:
        return self._stats.luck

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        self.sprite.take_damage()

    def pickup_gem(self, gem: ExperienceGem):
        self.__gain_experience(gem.amount)

    def __gain_experience(self, amount: int):
        self.__experience += amount * self._stats.xp_multiplier
        while self.__experience >= self.experience_to_next_level:
            self.__experience -= self.experience_to_next_level
            self.__level += 1
            self.__upgrading = True

    def regenerate_health(self, current_time):
        """Regenerates the health of the player if possible.
        
        Args:
            current_time: The current time.
        """
        if self.__health < self._stats.max_health:
            if current_time - self.__last_regeneration_time >= self._stats.regeneration_rate:
                self.sprite.heal()
                self.__health += self._stats.max_health * self._stats.regeneration_percentage / 100
                if self.__health > self._stats.max_health:
                    self.__health = self._stats.max_health
                self.__last_regeneration_time = current_time

    def update(self, world: IGameWorld, current_state: MovableEntityBaseState):
        """Updates the player.
        
        Args:
            world (IGameWorld): The game world.
            current_state (MovableEntityBaseState): The current state of the player
        """
        current_state.update_state(self)
        if self.__upgrading:
            world.set_upgrading_state(True)
            world.set_paused_state(True)

        current_time = pygame.time.get_ticks()
        self.regenerate_health(current_time)

        try:
            self._weapon_handler.use_every_weapon(
                self.pos_x,
                self.pos_y,
                world,
                current_time,
                self._stats.base_damage_multiplier,
                self._stats.base_attack_speed)
        except AttributeError as error:
            print("Loading...", error)
