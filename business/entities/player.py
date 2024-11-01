"""Player entity module."""

import pygame

from business.entities.state_machine.entity import MovableEntity
from business.entities.experience_gem import ExperienceGem
from business.entities.interfaces import ICanDealDamage, IDamageable, IPlayer
from business.world.interfaces import IGameWorld
from business.entities.weapon_handler import WeaponHandler
from business.entities.state_machine.movable_entity_base_state import MovableEntityBaseState
from business.stats.stats_handler import PlayerStats
from presentation.sprite import Sprite


class Player(MovableEntity, IPlayer, IDamageable, ICanDealDamage):
    """Player entity.

    The player is the main character of the game. It can move around the game world and shoot at monsters.
    """
    def __init__(self, pos_x: int, pos_y: int, sprite: Sprite, player_stats: PlayerStats):
        super().__init__(pos_x, pos_y, 5, sprite)

        self.__player_stats = player_stats
        self.__health: int = self.__player_stats.max_health
        self.__experience = 0
        self.__level = 1
        self.__last_regeneration_time = 0
        self._weapon_handler = WeaponHandler()
        self.__upgrading = False

    def get_player_weapons(self):
        return self._weapon_handler.get_all_weapons()

    def add_weapon(self, weapon_name: str, world: IGameWorld):
        self.__upgrading = False
        self._weapon_handler.add_weapon(weapon_name)
        world.set_upgrading_state(False)
        world.set_paused_state(False)

    def has_weapon(self, weapon_name: str):
        return self._weapon_handler.has_weapon(weapon_name)

    def get_weapon_level(self, weapon_name: str):
        return self._weapon_handler.get_weapon_level(weapon_name)

    def upgrade_weapon_next_level(self, weapon_name: str):
        self._weapon_handler.upgrade_weapon_next_level(weapon_name)

    def weapon_reached_max_level(self, weapon_name: str):
        return self._weapon_handler.has_reached_max_level(weapon_name)

    def __str__(self):
        return f"Player(hp={self.__health}, xp={self.__experience}, lvl={self.__level}, pos=({self._pos_x}, {self._pos_y}))"

    def set_position(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def set_upgrading(self, new_state: bool):
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
        return 1 + (2 * self.__level ** 2)

    @property
    def level(self):
        return self.__level

    @property
    def damage_amount(self):
        return self.__player_stats.base_damage_multiplier

    @property
    def health(self) -> int:
        return self.__health

    @property
    def luck(self) -> int:
        return self.__player_stats.luck

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        self.sprite.take_damage()

    def pickup_gem(self, gem: ExperienceGem):
        self.__gain_experience(gem.amount)

    def __gain_experience(self, amount: int):
        self.__experience += amount * self.__player_stats.xp_multiplier
        while self.__experience >= self.experience_to_next_level:
            self.__experience -= self.experience_to_next_level
            self.__level += 1
            self.__upgrading = True

    def regenerate_health(self, current_time):

        if self.__health < self.__player_stats.max_health:
            if current_time - self.__last_regeneration_time >= self.__player_stats.regeneration:
                self.sprite.heal()
                self.__health += self.__player_stats.max_health * self.__player_stats.regeneration_percentage / 100
                if self.__health > self.__player_stats.max_health:
                    self.__health = self.__player_stats.max_health
                self.__last_regeneration_time = current_time

    def update(self, world: IGameWorld, current_state:MovableEntityBaseState):
        
        current_state.update_state(self)
        
        if self.__upgrading:
            world.set_upgrading_state(True)
            world.set_paused_state(True)

        current_time = pygame.time.get_ticks()
        self.regenerate_health(current_time)

        try:
            self._weapon_handler.use_every_weapon(
                self.pos_x, self.pos_y, world, current_time, self.__player_stats.base_damage_multiplier, self.__player_stats.base_attack_speed)
        except AttributeError as error:
            print("Loading...", error)
