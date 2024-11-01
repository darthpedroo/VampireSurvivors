from business.weapons.auto_aim_gun import AutoAimGun
from business.weapons.manual_gun import ManualGun


class WeaponFactory:
    @staticmethod
    def create_weapon(weapon_type: str):
        if weapon_type == "Auto_Joker":
            bullet_name = "Joker_Bullet"
            bullet_cooldown = 10000
            bullet_speed = 20
            return AutoAimGun(weapon_type, bullet_name, bullet_cooldown, bullet_speed)
        if weapon_type == "Manual_Gun":
            bullet_name = "Bullet"
            bullet_cooldown = 200
            bullet_speed = 20
            return ManualGun(weapon_type, bullet_name, bullet_cooldown, bullet_speed)
        if weapon_type == "Manual_Joker":
            bullet_name = "Joker_Bullet"
            bullet_cooldown = 1300
            bullet_speed = 20
            return ManualGun(weapon_type, bullet_name, bullet_cooldown, bullet_speed)
        if weapon_type == "The_Mega_Ice":
            bullet_name = "Ice_Bullet"
            bullet_cooldown = 2705
            bullet_speed = 20
            return ManualGun(weapon_type, bullet_name, bullet_cooldown, bullet_speed)
