"""Factory of the weapons"""
from business.weapons.auto_aim_gun import AutoAimGun
from business.weapons.manual_gun import ManualGun
from business.stats.stats import WeaponStats
from business.weapons.no_aim_gun import NoAimGun

class WeaponFactory:
    """Represents the factory of the weapons"""
    @staticmethod
    def create_weapon(weapon_type: str, level:int = 1, p_weapon_stats: WeaponStats = None):
        if weapon_type == "Auto_Joker":
            bullet_name = "Joker_Bullet"
            damage = 10
            bullet_speed = 20
            bullet_cooldown = 3000
            max_level = 5
            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            if p_weapon_stats is not None:
                weapon_stats = p_weapon_stats
            return AutoAimGun(weapon_type, bullet_name,max_level,weapon_stats,level)
        if weapon_type == "Manual_Gun":
            bullet_name = "Bullet"
            damage = 20
            bullet_cooldown = 500
            bullet_speed = 20
            max_level = 5
            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            if p_weapon_stats is not None:
                weapon_stats = p_weapon_stats
            return ManualGun(weapon_type, bullet_name,max_level,weapon_stats,level)
        if weapon_type == "Manual_Joker":
            bullet_name = "Joker_Bullet"
            damage = 50
            bullet_cooldown = 1300
            bullet_speed = 20
            max_level = 5
            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            if p_weapon_stats is not None:
                weapon_stats = p_weapon_stats
            return ManualGun(weapon_type, bullet_name,max_level,weapon_stats,level)
        if weapon_type == "The_Mega_Ice":
            bullet_name = "Ice_Bullet"
            damage = 20
            bullet_cooldown = 2705
            bullet_speed = 20
            max_level = 5
            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            if p_weapon_stats is not None:
                weapon_stats = p_weapon_stats
            return ManualGun(weapon_type, bullet_name,max_level,weapon_stats,level)
        if weapon_type =="Toilet_spinner":
            bullet_name = "Rotating_Bullet"
            damage = 8
            bullet_cooldown=0
            bullet_speed = 1
            max_level = 5

            weapon_stats = WeaponStats(damage, bullet_speed, bullet_cooldown)
            if p_weapon_stats is not None:
                weapon_stats = p_weapon_stats
            return NoAimGun(weapon_type, bullet_name, max_level,weapon_stats,level)
        else:
            raise ValueError
