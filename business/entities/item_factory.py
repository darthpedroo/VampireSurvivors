from business.entities.bullet import Bullet
from business.entities.ice_bullet import IceBullet
from business.stats.stats import WeaponStats, BulletStats


class ProjectileFactory:
    """Factory que crea distintos tipos de weapons  

    Returns:
        _type_: _description_
    """
    @staticmethod
    def create_item(item_name: str, entity_pos_x: int, entity_pos_y: int, dir_x: int, dir_y: int, movement_speed:int, damage:int, cooldown:int):
        if item_name == "Bullet":   
            asset = "./assets/bullets/Bullet.png"
            health = 10
            size = 50
            damage = 1 * damage
            bullet_stats = BulletStats(movement_speed,damage,cooldown,size)
            return Bullet(entity_pos_x, entity_pos_y, dir_x, dir_y, health, bullet_stats, asset)
        if item_name == "Joker_Bullet":
            asset = "./assets/bullets/Joker_Bullet.png"
            health = 1000
            damage = 1 * damage
            size = 50
            bullet_stats = BulletStats(movement_speed,damage,cooldown,size)
            return Bullet(entity_pos_x, entity_pos_y, dir_x, dir_y, health, bullet_stats, asset)
        if item_name == "Ice_Bullet":
            asset = "./assets/bullets/Ice_Bullet.png"
            health = 100
            damage = 0 * damage
            size = 50
            bullet_stats = BulletStats(movement_speed,damage,cooldown,size)
            return Bullet(entity_pos_x, entity_pos_y, dir_x, dir_y, health, bullet_stats, asset)
