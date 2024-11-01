"""This module contains the Monster factory, which manages what type of monster that should be spawned."""

import random
from typing import List

from presentation.sprite import Sprite, ZombieSprite, SpiderSprite
from business.entities.monsters.zombie import Zombie
from business.entities.monsters.spider import Spider


class MonsterFactory:
    """A monster entity in the game."""

    ALL_MONSTERS = ["spider", "zombie"]

    @staticmethod
    def get_random_monster(pos_x: int, pos_y: int):
        random_monster = random.choice(MonsterFactory.ALL_MONSTERS)
        return MonsterFactory.get_monster(random_monster, pos_x, pos_y)

    @staticmethod
    def get_monster(monster_type: str, pos_x: int, pos_y: int):
        if monster_type == "zombie":
            return Zombie(pos_x, pos_y, ZombieSprite(pos_x, pos_y))
        elif monster_type == "spider":
            return Spider(pos_x, pos_y, SpiderSprite(pos_x, pos_y))
        else:
            raise ValueError("Not W")
