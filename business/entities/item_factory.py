"""Module of the Item Factory"""
from business.entities.bullet import Bullet
from business.entities.ice_bullet import IceBullet
from business.stats.stats import BulletStats

class ProjectileFactory:
    """Represents the proyectile factory"""
    @staticmethod
    def create_item(item_name: str, entity_pos_x: int, entity_pos_y: int, dir_x: int, dir_y: int, movement_speed:int, damage:int, cooldown:int): #pylint: disable=line-too-long
        """Creates a projectile item based on the given parameters.

        Args:
            item_name (str): The name of the projectile.
            entity_pos_x (int): The position on the x axis of the proyectile.
            entity_pos_y (int): The position on the y axis of the proyectile.
            dir_x (int): The direction on the x axis of the proyectile.
            dir_y (int): The direction on the y axis of the proyectile.
            movement_speed (int): The speed of the projectile.
            damage (int): The damage of the projectile.
            cooldown (int): The cooldown of the projectile.

        Returns:
            Bullet | IceBullet: An instance of Bullet or IceBullet based on the item name.
        """
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
            return IceBullet(entity_pos_x, entity_pos_y, dir_x, dir_y, health, bullet_stats, asset)
