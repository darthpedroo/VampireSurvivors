"""Player entity module."""

import pygame

from business.entities.bullet import Bullet
from business.entities.entity import MovableEntity
from business.entities.experience_gem import ExperienceGem
from business.entities.interfaces import ICanDealDamage, IDamageable, IPlayer
from business.world.interfaces import IGameWorld
from business.entities.weapon_handler import WeaponHandler, GunWithBullets
from presentation.sprite import Sprite

class Player(MovableEntity, IPlayer, IDamageable, ICanDealDamage):
    """Player entity.

    The player is the main character of the game. It can move around the game world and shoot at monsters.
    """

    BASE_DAMAGE = 5

    def __init__(self, pos_x: int, pos_y: int, sprite: Sprite):
        super().__init__(pos_x, pos_y, 5, sprite)

        self.__health: int = 100
        self.__last_shot_time = pygame.time.get_ticks()
        self.__experience = 0
        self.__level = 1
        self.__luck = 1
        self._logger.debug("Created %s", self)
        self.__weapon_handler = WeaponHandler([GunWithBullets("Bullet_Guided",1000,20), GunWithBullets("Bullet",7000,10)]) #Tratar de usar dependency Injection
        
    def __str__(self):
        return f"Player(hp={self.__health}, xp={self.__experience}, lvl={self.__level}, pos=({self._pos_x}, {self._pos_y}))"

    def set_position(self, pos_x:int, pos_y:int):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
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
        return self.__level * 30

    @property
    def level(self):
        return self.__level

    @property
    def damage_amount(self):
        return Player.BASE_DAMAGE

    @property
    def health(self) -> int:
        return self.__health

    @property
    def luck(self) -> int:
        return self.__luck

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        self.sprite.take_damage()

    def pickup_gem(self, gem: ExperienceGem):
        self.__gain_experience(gem.amount)

    def __gain_experience(self, amount: int):
        self.__experience += amount
        while self.__experience >= self.experience_to_next_level:
            self.__experience -= self.experience_to_next_level
            self.__level += 1
    
    def update(self, world: IGameWorld):
        super().update(world)
        
        current_time = pygame.time.get_ticks()
        try:
            self.__weapon_handler.use_every_weapon(self.pos_x, self.pos_y, world, current_time)
        except AttributeError as error:
            print("Loading...", error)