"""Factory of the weapons"""
from business.weapons.auto_aim_gun import AutoAimGun
from business.weapons.manual_gun import ManualGun
from business.stats.stats import WeaponStats


class WeaponFactory:
    """Represents the factory of the weapons"""
    @staticmethod
    def create_weapon(weapon_type: str):
        """Creates weapons based on their type.
        
        Args:
            weapon_type (str): The type of the weapon to be created
        """
        if weapon_type == "Auto_Joker":
            bullet_name = "Joker_Bullet"
            damage = 10
            bullet_speed = 20
            bullet_cooldown = 3000
            max_level = 5
            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            return AutoAimGun(weapon_type, bullet_name,max_level,weapon_stats)
        if weapon_type == "Manual_Gun":
            bullet_name = "Bullet"
            damage = 20
            bullet_cooldown = 500
            bullet_speed = 20
            max_level = 5
            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            return ManualGun(weapon_type, bullet_name,max_level,weapon_stats)
        if weapon_type == "Manual_Joker":
            bullet_name = "Joker_Bullet"
            damage = 50
            bullet_cooldown = 1300
            bullet_speed = 20
            max_level = 5
            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            return ManualGun(weapon_type, bullet_name,max_level,weapon_stats)
        if weapon_type == "The_Mega_Ice":
            bullet_name = "Ice_Bullet"
            damage = 20
            bullet_cooldown = 2705
            bullet_speed = 20
            max_level = 5
            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            return ManualGun(weapon_type, bullet_name,max_level,weapon_stats)
        
        else:
            raise ValueError

