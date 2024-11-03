from abc import ABC

class BaseStats(ABC):
    def __init__(self):
        super().__init__()

class EntityStats(ABC):
    """_summary_
    """
    def __init__(self, max_health: int, movement_speed:int, base_damage_multiplier: int, base_attack_speed:int, size:int):
        self.max_health = max_health
        self.movement_speed = movement_speed
        self.base_damage_multiplier = base_damage_multiplier
        self.base_attack_speed = base_attack_speed
        self.size = size

class PerkStats(BaseStats):
    def __init__(self, max_health_multiplier: float=1, movement_speed_multiplier: float=1, base_damage_multiplier: float=1, 
attack_speed_multiplier: float=1, regeneration_rate_multiplier: float=1, regeneration_percentage_multiplier: float=1, 
xp_multiplier: float=1, luck_multiplier: float=1):
        
        self.max_health_multiplier = max_health_multiplier
        self.movement_speed_multiplier = movement_speed_multiplier
        self.base_damage_multiplier = base_damage_multiplier
        self.attack_speed_multiplier = attack_speed_multiplier
        self.regeneration_rate_multiplier = regeneration_rate_multiplier
        self.regeneration_percentage_multiplier = regeneration_percentage_multiplier
        self.xp_multiplier = xp_multiplier
        self.luck_multiplier = luck_multiplier

class WeaponStats(BaseStats):
    def __init__(self, damage: int, speed:int, cooldown:int):
        self.damage = damage
        self.movement_speed = speed
        self.cooldown = cooldown

class BulletStats(BaseStats):
    def __init__(self, movement_speed:int, damage:int, cooldown:int, size:int):
        self.movement_speed = movement_speed
        self.damage = damage
        self.cooldown = cooldown
        self.size = size

class PlayerStats(EntityStats):
    """The Stats of a Player

    Args:
        BaseStats (_type_): _description_
    """
    def __init__(self, max_health=1, movement_speed=1, base_damage_multiplier=1, base_attack_speed=1, size:int=1, regeneration_rate: int=1, regeneration_percentage:int=1, xp_multiplier:int=1, luck:int=1):
        super().__init__(max_health, movement_speed, base_damage_multiplier, base_attack_speed,size)
        self.regeneration_rate = regeneration_rate
        self.regeneration_percentage = regeneration_percentage
        self.xp_multiplier = xp_multiplier
        self.luck = luck

    

class MonsterStats(EntityStats):
    def __init__(self, max_health, movement_speed, base_damage_multiplier, base_attack_speed, size):
        super().__init__(max_health, movement_speed, base_damage_multiplier, base_attack_speed, size)




