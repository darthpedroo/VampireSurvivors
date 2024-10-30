"""This module contains the implementation of the game world."""

from business.entities.interfaces import IBullet, IExperienceGem, IMonster, IPlayer
from business.world.interfaces import IGameWorld, IMonsterSpawner, ITileMap
from business.weapons.weapon_factory import WeaponFactory

import pygame
import random


class GameWorld(IGameWorld):
    """Represents the game world."""

    def __init__(self, spawner: IMonsterSpawner, tile_map: ITileMap, player: IPlayer, display: "Display"):
        # Initialize the player and lists for monsters, bullets and gems
        self.__player: IPlayer = player
        self.__monsters: list[IMonster] = []
        self.__bullets: list[IBullet] = []
        self.__experience_gems: list[IExperienceGem] = []
        self.tile_map: ITileMap = tile_map
        self.__monster_spawner: IMonsterSpawner = spawner
        self.__display = display
        self._paused = False
        self._upgrading = False
        self._random_weapons_to_choose = []
        self.__list_of_weapons = ["Auto_Joker",
                                  "Manual_Gun", "Manual_Joker", "The_Mega_Ice"]

    def add_random_weapons(self):
        weapons = self.__list_of_weapons.copy()
        for _ in range(3):
            if not weapons:
                print("No more ammo for you, little vater")
                break

            rnd_weapon = random.choice(weapons)
            if not self.__player.weapon_reached_max_level(rnd_weapon):
                weapon_instance = WeaponFactory().create_weapon(rnd_weapon)
                self._random_weapons_to_choose.append(weapon_instance)

            weapons.remove(rnd_weapon)

    def restore_random_weapons(self):
        self._random_weapons_to_choose = []

    def update_player(self, sprite_direction: str, x_mov: int, y_mov: int):
        if not self._paused:
            self.__player.sprite.change_to_walk_sprite(sprite_direction)
            self.__player.move(x_mov, y_mov)

    def change_paused_state(self):
        if self._paused:
            self._paused = False
        else:
            self._paused = True

    @property
    def paused(self):
        return self._paused

    def set_upgrading_state(self, state: bool):
        self._upgrading = state

    def set_paused_state(self, state: bool):
        self._paused = state

    def get_mouse_position(self):
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos

    def get_camera(self):
        return self.__display.camera

    def update(self):
        if not self._paused:
            self.player.update(self)
            for monster in self.monsters:
                monster.update(self)
            for bullet in self.__bullets:
                bullet.update(self)
            self.__monster_spawner.update(self)

    def add_monster(self, monster: IMonster):
        self.__monsters.append(monster)

    def remove_monster(self, monster: IMonster):
        self.__monsters.remove(monster)

    def add_experience_gem(self, gem: IExperienceGem):
        self.__experience_gems.append(gem)

    def remove_experience_gem(self, gem: IExperienceGem):
        self.__experience_gems.remove(gem)

    def add_bullet(self, bullet: IBullet):
        self.__bullets.append(bullet)

    def remove_bullet(self, bullet: IBullet):
        self.__bullets.remove(bullet)

    @property
    def player(self) -> IPlayer:
        return self.__player

    @property
    def monsters(self) -> list[IMonster]:
        return self.__monsters[:]

    @property
    def bullets(self) -> list[IBullet]:
        return self.__bullets[:]

    @property
    def experience_gems(self) -> list[IExperienceGem]:
        return self.__experience_gems[:]

    @property
    def paused(self):
        return self._paused

    @property
    def upgrading(self):
        return self._upgrading
