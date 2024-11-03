"""This module contains the Monster factory, which manages what type of monster that should be spawned."""

import random
from typing import List

from presentation.sprite import Sprite, ZombieSprite, SpiderSprite
from business.entities.monsters.zombie import Zombie
from business.entities.monsters.spider import Spider
from business.stats.stats import EntityStats


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
            
            max_health = 200
            speed = 1
            damage_multiplier = 3
            base_attack_speed = 10
            size = 10
            stats = EntityStats(max_health,speed,damage_multiplier,base_attack_speed,size)
            return Zombie(pos_x, pos_y, ZombieSprite(pos_x, pos_y,size),stats)
        elif monster_type == "spider":
            max_health = 100
            speed = 1
            damage_multiplier = 3
            base_attack_speed = 10
            size = 100
            stats = EntityStats(max_health,speed,damage_multiplier,base_attack_speed,size)
            return Spider(pos_x, pos_y, SpiderSprite(pos_x, pos_y,size),stats)
        else:
            raise ValueError("Not W")
