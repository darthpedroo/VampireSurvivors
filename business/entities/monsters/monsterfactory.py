"""This module contains the Monster factory, which manages what type of monster that should be spawned."""

import random

from presentation.sprite import ZombieSprite, SpiderSprite, ShulkerSprite
from business.entities.monsters.zombie import Zombie
from business.entities.monsters.spider import Spider
from business.entities.monsters.shulker import Shulker
from business.stats.stats import MonsterStats
from business.clock.clock import ClockSingleton


class MonsterFactory:
    """A monster entity in the game."""

    ALL_MONSTERS = ["shulker"]
    CLOCK = ClockSingleton()

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
        print("random_monster: ", random_monster)
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
        CLOCK = ClockSingleton()
        time_stats_multiplier = CLOCK.get_time()/1000
        if monster_type == "zombie":
            max_health = 200 + time_stats_multiplier
            speed = 1 + time_stats_multiplier/10000
            damage_multiplier = 3  + time_stats_multiplier/100
            base_attack_speed = 10  + time_stats_multiplier
            size = 100
            precision = 60
            stats = MonsterStats(max_health,speed,damage_multiplier,base_attack_speed,size,precision)
            return Zombie(pos_x, pos_y, ZombieSprite(pos_x, pos_y,size),stats)
        elif monster_type == "spider":
            max_health = 100  + time_stats_multiplier
            speed = 1 + time_stats_multiplier/10000
            damage_multiplier = 3  + time_stats_multiplier/100
            base_attack_speed = 10  + time_stats_multiplier
            size = 100
            precision = 1
            stats = MonsterStats(max_health,speed,damage_multiplier,base_attack_speed,size,precision)
            return Spider(pos_x, pos_y, SpiderSprite(pos_x, pos_y,size),stats)
        
        elif monster_type == "shulker":            
            max_health = 100  + time_stats_multiplier
            speed = (1 + time_stats_multiplier/10000) * 2 #DUPLICO LA VELOCIDAD BASE
            damage_multiplier = 3  + time_stats_multiplier/100
            base_attack_speed = 10  + time_stats_multiplier
            size = 100
            shield_value = 20
            precision = 1
            stats = MonsterStats(max_health,speed,damage_multiplier,base_attack_speed,size,precision)
            return Shulker(pos_x, pos_y,ShulkerSprite(pos_x,pos_y,size),stats,shield_value)
        else:
            raise ValueError("Not A Valid Enemy")
