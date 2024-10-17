from business.entities.bullet import Bullet
from business.entities.bullet_guided import BulletGuided

class ProjectileFactory:
    """Factory que crea distintos tipos de weapons  

    Returns:
        _type_: _description_
    """
    @staticmethod
    def create_item(item_name:str, entity_pos_x:int, entity_pos_y:int, item_speed:int, world:"IGameWorld"):
        if item_name == "Bullet":
            return Bullet(entity_pos_x,entity_pos_y,item_speed, world)
        if item_name == "Bullet_Guided":
            return BulletGuided(entity_pos_x,entity_pos_y,item_speed,world)