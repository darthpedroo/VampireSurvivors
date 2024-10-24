"""This module contains the Monster factory, which manages what type of monster that should be spawned."""

from typing import List

from presentation.sprite import Sprite, ZombieSprite, SpiderSprite
from business.entities.zombie import Zombie
from business.entities.spider import Spider


class MonsterFactory:
    """A monster entity in the game."""

    @staticmethod
    def get_monster(monster_type: str, pos_x: int, pos_y: int):
        if monster_type == "zombie":
            return Zombie(pos_x, pos_y, ZombieSprite(pos_x, pos_y))
        elif monster_type == "spider":
            return Spider(pos_x, pos_y, SpiderSprite(pos_x, pos_y))
        else:
            raise ValueError("Not W")
