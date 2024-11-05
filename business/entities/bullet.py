"""Module for a bullet entity that moves towards a target direction."""

from business.stats.stats import BulletStats
from business.entities.state_machine.movable_entity_moving_state import MovableEntityMovingState
from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletSprite

class Bullet(MovableEntity, IBullet):
    """A bullet that moves towards a target direction."""

    def __init__(self, name: str, pos_x, pos_y, dir_x, dir_y, health: int, stats:BulletStats, asset: str, current_state = MovableEntityMovingState()):
        super().__init__(pos_x, pos_y, stats, BulletSprite(pos_x, pos_y, asset, stats.size))
        self.name = name
        self.__dir_x = dir_x
        self.__dir_y = dir_y
        self.__asset = asset
        self._logger.debug("Created %s", self)
        self._health = health
        self._damage_amount = stats.damage
        self.set_direction(dir_x, dir_y)
        self.current_state = current_state
    
    def create_bullet_json_data(self):
        bullet_data = {"name": self.name, "pos_x": self.pos_x, "pos_y": self.pos_y, "dir_x": self.__dir_x, "dir_y": self.__dir_y, "health":self._health, "stats":self._stats.create_bullets_stats_json_data(), "asset":self.__asset}
        return bullet_data

    @property
    def health(self) -> int:
        return self._health

    def take_damage(self, amount):
        self._health -= amount

    def update(self, _: IGameWorld):
        self.current_state.update_state(self)

    @property
    def damage_amount(self):
        return self._damage_amount

    def __str__(self):
        return f"Bullet(pos=({self._pos_x, self._pos_y}), dir=({self.__dir_x, self.__dir_y}))"

    def apply_effect(self, other_entity: "MovableEntity"):
        return super().apply_effect(other_entity)
