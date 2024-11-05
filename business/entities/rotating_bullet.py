"""Module for a rotating bullet."""
from business.stats.stats import BulletStats
from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletSprite


class RotatingBullet(MovableEntity,IBullet):
    def __init__(self, name:str, pos_x: float, pos_y: float, dir_x: float, dir_y: float, health: int, stats: BulletStats, asset: str, current_state):
        super().__init__(pos_x, pos_y, stats, BulletSprite(pos_x, pos_y, asset, stats.size))
        self._logger.debug("Created %s", self)
        self.name = name
        self.__asset = asset
        self.__dir_x = dir_x
        self.__dir_y = dir_y
        self._health = health
        self._damage_amount = stats.damage
        self.set_direction(dir_x, dir_y)
        self.current_state = current_state

    def create_bullet_json_data(self):
        bullet_data = {"name": self.name, "pos_x": self.pos_x, "pos_y": self.pos_y, "dir_x": self.__dir_x, "dir_y": self.__dir_y, "health":self._health, "stats":self._stats.create_bullets_stats_json_data(), "asset":self.__asset}
        return bullet_data
    
    def apply_effect(self, other_entity: MovableEntity):
        return super().apply_effect(other_entity)

    @property

    def health(self) -> int:
        return self._health

    def take_damage(self, amount):
        self._health -= 0

    def update(self, world: IGameWorld):
        """Updates the state of the bullet in the given world.

        Args:
            world (IGameWorld): The game world where the bullet is present.
        """
        self.current_state.update_state(self)

    @property
    def damage_amount(self):
        return self._damage_amount

    def __str__(self):
        return f"Bullet(pos=({self._pos_x, self._pos_y}), dir=({self.__dir_x, self.__dir_y}))"
