"""This module contains the MonsterSpawner class."""

import logging
import random

import pygame

import settings
from business.entities.monsters.zombie import Zombie
from business.world.interfaces import IGameWorld, IMonsterSpawner
from business.world.monsterfactory import MonsterFactory


class MonsterSpawner(IMonsterSpawner):
    """Spawns monsters in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self._max_monsters = 30
        

    def update(self, world: IGameWorld):
        if len(world.monsters) < self._max_monsters:
            self.spawn_monster(world)
        
        
    def spawn_monster(self, world: IGameWorld):
        pos_x = random.randint(0, settings.WORLD_WIDTH)
        pos_y = random.randint(0, settings.WORLD_HEIGHT)
        monster = MonsterFactory().get_random_monster(pos_x, pos_y)
        world.add_monster(monster)
        self.__logger.debug("Spawning monster at (%d, %d)", pos_x, pos_y)
