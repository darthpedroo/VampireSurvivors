from business.entities.bullet import Bullet
from business.entities.bullet_guided import BulletGuided


class ProjectileFactory:
    """Factory que crea distintos tipos de weapons  

    Returns:
        _type_: _description_
    """
    @staticmethod
    def create_item(item_name: str, entity_pos_x: int, entity_pos_y: int, dir_x: int, dir_y: int, item_speed: int, weapon_damage_multiplier:float, world: "IGameWorld"):
        if item_name == "Bullet":
            health = 10
            damage = 1 * weapon_damage_multiplier
            return Bullet(entity_pos_x, entity_pos_y, dir_x, dir_y, item_speed,health,damage, world)
        if item_name == "Joker_Bullet":
            health = 1000
            damage = 1 * weapon_damage_multiplier
            return BulletGuided(entity_pos_x, entity_pos_y, dir_x, dir_y, item_speed, health, damage, world)
