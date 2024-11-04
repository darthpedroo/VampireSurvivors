"""This module contains the Monster factory, which manages what type of monster that should be spawned.""" #pylint: disable=line-too-long

import random

from presentation.sprite import ZombieSprite, SpiderSprite
from business.entities.monsters.zombie import Zombie
from business.entities.monsters.spider import Spider
from business.stats.stats import EntityStats
from business.clock.clock import ClockSingleton


class MonsterFactory:
    """A monster entity in the game."""

    ALL_MONSTERS = ["spider", "zombie"]
    CLOCK = ClockSingleton()
    TIME_STATS_MULTIPLIER = CLOCK.get_time() / 1000

    @staticmethod
    def get_random_monster(pos_x: int, pos_y: int):
        """Gets a random monster
        
        Args:
            pos_x (int): The position of the monster to be spawned on the x axis.
            pos_y (int): The position of the monster to be spawned on the y axis.
        
        Returns:
            Zombie | Spider: An instance of the monster depending on which monster was chosen.
        """
        random_monster = random.choice(MonsterFactory.ALL_MONSTERS)
        return MonsterFactory.get_monster(random_monster, pos_x, pos_y)

    @staticmethod
    def get_monster(monster_type: str, pos_x: int, pos_y: int):
        """Gets a random monster
        
        Args:
            monster_type (str): The type of monster to be spawned.
            pos_x (int): The position of the monster to be spawned on the x axis.
            pos_y (int): The position of the monster to be spawned on the y axis.
        
        Returns:
            Zombie | Spider: An instance of the monster depending on which monster was chosen.
        """
        if monster_type == "zombie":
            max_health = 200 + MonsterFactory.TIME_STATS_MULTIPLIER
            speed = 1 + MonsterFactory.TIME_STATS_MULTIPLIER/100
            damage_multiplier = 3  + MonsterFactory.TIME_STATS_MULTIPLIER/1000
            base_attack_speed = 10  + MonsterFactory.TIME_STATS_MULTIPLIER
            size = 100
            stats = EntityStats(max_health,speed,damage_multiplier,base_attack_speed,size)
            return Zombie(pos_x, pos_y, ZombieSprite(pos_x, pos_y,size),stats)
        elif monster_type == "spider":
            max_health = 100  + MonsterFactory.TIME_STATS_MULTIPLIER
            speed = 1 + MonsterFactory.TIME_STATS_MULTIPLIER/100
            damage_multiplier = 3  + MonsterFactory.TIME_STATS_MULTIPLIER
            base_attack_speed = 10  + MonsterFactory.TIME_STATS_MULTIPLIER
            size = 100
            stats = EntityStats(max_health,speed,damage_multiplier,base_attack_speed,size)
            return Spider(pos_x, pos_y, SpiderSprite(pos_x, pos_y,size),stats)
        else:
            raise ValueError("Not A Valid Enemy")
