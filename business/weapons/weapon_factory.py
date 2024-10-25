from business.weapons.auto_aim_gun import AutoAimGun
from business.weapons.manual_gun import ManualGun
class WeaponFactory:
    @staticmethod
    def create_weapon(weapon_type: str):
        if weapon_type == "Auto_Joker":
            bullet_name = "Joker_Bullet"
            bullet_cooldown = 5000
            bullet_speed = 10
            return AutoAimGun(weapon_type, bullet_name, bullet_cooldown, bullet_speed)
        if weapon_type == "Manual_Gun":
            bullet_name = "Bullet"
            bullet_cooldown = 500
            bullet_speed = 10
            return ManualGun(weapon_type, bullet_name, bullet_cooldown, bullet_speed)
        if weapon_type == "Manual_Joker":
            bullet_name = "Joker_Bullet"
            bullet_cooldown = 2000
            bullet_speed = 10
            return ManualGun(weapon_type, bullet_name, bullet_cooldown, bullet_speed)
