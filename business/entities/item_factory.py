from business.entities.bullet import Bullet
from business.entities.ice_bullet import IceBullet


class ProjectileFactory:
    """Factory que crea distintos tipos de weapons  

    Returns:
        _type_: _description_
    """
    @staticmethod
    def create_item(item_name: str, entity_pos_x: int, entity_pos_y: int, dir_x: int, dir_y: int, item_speed: int, weapon_damage_multiplier: float, world: "IGameWorld"):
        if item_name == "Bullet":
            health = 10
            damage = 1 * weapon_damage_multiplier
            asset = "./assets/zombie.png"
            size = 100
            return Bullet(entity_pos_x, entity_pos_y, dir_x, dir_y, item_speed, health, damage, asset, size)
        if item_name == "Joker_Bullet":
            asset = "./assets/joker-dc.png"
            health = 1000
            damage = 1 * weapon_damage_multiplier
            size = 300
            return Bullet(entity_pos_x, entity_pos_y, dir_x, dir_y, item_speed, health, damage, asset, size)
        if item_name == "Ice_Bullet":
            health = 100
            damage = 1 * weapon_damage_multiplier
            asset = "./assets/experience_gems.png"
            size = 50
            return IceBullet(entity_pos_x, entity_pos_y, dir_x, dir_y, item_speed, health, damage, asset, size)
