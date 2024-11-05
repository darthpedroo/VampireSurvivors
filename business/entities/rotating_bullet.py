
from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletSprite


class RotatingBullet (MovableEntity,IBullet):   
    def __init__(self, pos_x, pos_y, dir_x, dir_y, speed: int, health: int, damage_amount: int, asset: str, size, current_state):
        super().__init__(pos_x, pos_y, speed, BulletSprite(pos_x, pos_y, asset, size))
        self._logger.debug("Created %s", self)
        self._health = health
        self._damage_amount = damage_amount
        self.set_direction(dir_x, dir_y)
        self.current_state = current_state
    
    def apply_effect(self, other_entity: MovableEntity):
        return super().apply_effect(other_entity)

    @property

    def health(self) -> int:  # Why does it have health ? :v
        return self._health

    def take_damage(self, amount ):
        self._health -= 0

    def update(self):
        self.current_state.update_state(self)

    @property
    def damage_amount(self):
        return self._damage_amount

    def __str__(self):
        return f"Bullet(pos=({self._pos_x, self._pos_y}), dir=({self.__dir_x, self.__dir_y}))"
