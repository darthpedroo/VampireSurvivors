"""Module of the stats of the game"""

from abc import ABC

class BaseStats(ABC):
    """Represents the base stats"""
    def __init__(self):
        super().__init__()

class EntityStats(ABC):
    """Represents the entity stats
    
    Args:
        max_health (int): The maximum health of the entity.
        movement_speed (int): The movement speed of the entity.
        base_damage_multiplier (int): The base damage multiplier for the entity.
        base_attack_speed (int): The base attack speed of the entity.
        size (int): The size of the entity.
    """
    def __init__(self, max_health: int, movement_speed:int, base_damage_multiplier: int, base_attack_speed:int, size:int):
        self.max_health = max_health
        self.movement_speed = movement_speed
        self.base_damage_multiplier = base_damage_multiplier
        self.base_attack_speed = base_attack_speed
        self.size = size
    
    def create_entity_stats_json_data(self):
        monster_stats = {
            "max_health": self.max_health,
            "movement_speed": self.movement_speed,
            "base_damage_multiplier": self.base_damage_multiplier,
            "base_attack_speed": self.base_attack_speed,
            "size": self.size
        }
        return monster_stats


class PerkStats(BaseStats):
    """The stats of the perks

    Args:
        max_health_multiplier (float): The maximum multiplier of the perk.
        movement_speed_multiplier (float): The movement speed multiplier of the perk.
        base_damage_multiplier (float): The base damage multiplier for the perk.
        attack_speed_multiplier (float): The attack speed multiplier of the perk.
        regeneration_rate_multiplier (float): The regeneration rate multiplier of the perk.
        regeneration_percentage_multiplier (float): The regeneration percentage multiplier of the perk.
        xp_multiplier (float): The experience points multiplier of the perk.
        luck_multiplier (float): The luck multiplier of the perk.
    """
    def __init__(self, max_health_multiplier: float=1, movement_speed_multiplier: float=1, base_damage_multiplier: float=1, attack_speed_multiplier: float=1, regeneration_rate_multiplier: float=1, regeneration_percentage_multiplier: float=1, xp_multiplier: float=1, luck_multiplier: float=1):
        self.max_health_multiplier = max_health_multiplier
        self.movement_speed_multiplier = movement_speed_multiplier
        self.base_damage_multiplier = base_damage_multiplier
        self.attack_speed_multiplier = attack_speed_multiplier
        self.regeneration_rate_multiplier = regeneration_rate_multiplier
        self.regeneration_percentage_multiplier = regeneration_percentage_multiplier
        self.xp_multiplier = xp_multiplier
        self.luck_multiplier = luck_multiplier
    
    def create_perk_stats_json_data(self):
        weapon_stats = {"max_health": self.max_health, "movement_speed": self.movement_speed, "base_damage_multiplier": self.base_damage_multiplier, "base_attack_speed": self.base_attack_speed, "size": self.size, "regeneration_rate": self.regeneration_rate, "regeneration_percentage": self.regeneration_percentage, "xp_multiplier": self.xp_multiplier, "luck": self.luck}
        return weapon_stats

class WeaponStats(BaseStats):
    """Represents the weapon stats
    
    Args:
        damage (int): The damage multiplier for the weapon.
        speed (int): The speed of the weapon.
        cooldown (int): The cooldown of the weapon.
    """
    def __init__(self, damage: int=1, speed:int=1, cooldown:int=1):
        self.damage = damage
        self.movement_speed = speed
        self.cooldown = cooldown

    def create_weapon_stats_json_data(self):
        weapon_stats = {"damage": self.damage, "movement_speed": self.movement_speed, "cooldown": self.cooldown}
        return weapon_stats
    


class BulletStats(BaseStats):
    """The stats of a bullet

    Args:
        movement_speed (int): The movement speed of the bullet.
        damage (int): The damage multiplier for the bullet.
        cooldown (int): The cooldown of the bullet.
        size (int): The size of the bullet.
    """
    def __init__(self, movement_speed:int, damage:int, cooldown:int, size:int):
        self.movement_speed = movement_speed
        self.damage = damage
        self.cooldown = cooldown
        self.size = size
    
    def create_bullets_stats_json_data(self):
        return {"movement_speed": self.movement_speed, "damage": self.damage, "cooldown": self.cooldown, "size": self.size}

class PlayerStats(EntityStats):
    """The stats of the player

    Args:
        max_health (int): The maximum health of the player.
        movement_speed (int): The movement speed of the player.
        base_damage_multiplier (int): The base damage multiplier for the player.
        base_attack_speed (int): The base attack speed of the player.
        size (int): The size of the player.
        regeneration_rate (int): The regeneration rate of the player.
        regeneration_percentage (int): The regeneration percentage of the player.
        xp_multiplier (int): The experience points multiplier for the player.
        luck (int): The luck of the player.
    """
    def __init__(self, max_health=1, movement_speed=1, base_damage_multiplier=1, base_attack_speed=1, size:int=1, regeneration_rate: int=1, regeneration_percentage:int=1, xp_multiplier:int=1, luck:int=1):
        super().__init__(max_health, movement_speed, base_damage_multiplier, base_attack_speed,size)
        self.regeneration_rate = regeneration_rate
        self.regeneration_percentage = regeneration_percentage
        self.xp_multiplier = xp_multiplier
        self.luck = luck

    def create_player_stats_json_data(self):
        weapon_stats = {"max_health": self.max_health, "movement_speed": self.movement_speed, "base_damage_multiplier": self.base_damage_multiplier, "base_attack_speed": self.base_attack_speed, "size": self.size, "regeneration_rate": self.regeneration_rate, "regeneration_percentage": self.regeneration_percentage, "xp_multiplier": self.xp_multiplier, "luck": self.luck}
        return weapon_stats

