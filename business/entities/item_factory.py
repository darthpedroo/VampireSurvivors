"""Module of the Item Factory"""
from business.entities.bullet import Bullet
from business.entities.ice_bullet import IceBullet
from business.stats.stats import BulletStats
from business.entities.rotating_bullet import RotatingBullet
from business.entities.state_machine.movable_entity_rotate_state import RotatingState
class BulletFactory:
    """Represents the proyectile factory"""
    @staticmethod
    def create_item(item_name: str, entity_pos_x: int=0, entity_pos_y: int=0, dir_x: int=0, dir_y: int=0, p_health=None, movement_speed:int=1, damage:int=1, cooldown:int=1): #pylint: disable=line-too-long
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
            if p_health is  None:
                health = 100
            else:
                health = p_health
            size = 50
            damage = 0.4 * damage
            bullet_stats = BulletStats(movement_speed,damage,cooldown,size)
            return Bullet(item_name, entity_pos_x, entity_pos_y, dir_x, dir_y, health, bullet_stats, asset)
        if item_name == "Joker_Bullet":
            asset = "./assets/bullets/Joker_Bullet.png"
            if p_health is  None:
                health = 1000
            else:
                health = p_health
            damage = 1 * damage
            size = 50
            bullet_stats = BulletStats(movement_speed,damage,cooldown,size)
            return Bullet(item_name,entity_pos_x, entity_pos_y, dir_x, dir_y, health, bullet_stats, asset)
        if item_name == "Ice_Bullet":
            asset = "./assets/bullets/Ice_Bullet.png"
            if p_health is  None:
                health = 100
            else:
                health = p_health
            damage = 0 * damage
            size = 50
            bullet_stats = BulletStats(movement_speed,damage,cooldown,size)
            return IceBullet(item_name,entity_pos_x, entity_pos_y, dir_x, dir_y, health, bullet_stats, asset)
        if item_name == "Rotating_Bullet" :
            asset = "./assets/bullets/Rotating_Bullet.png"
            health = 1.1
            damage = 0.5 * damage
            size = 50
            bullet_stats = BulletStats(movement_speed,damage,cooldown,size)
            current_state = RotatingState()
            return RotatingBullet(item_name,entity_pos_x, entity_pos_y, dir_x, dir_y, health, bullet_stats, asset, current_state)
