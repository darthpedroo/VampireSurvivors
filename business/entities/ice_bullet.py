"""Module for a bullet entity that moves towards a target direction."""

from business.entities.state_machine.movable_entity_moving_state import MovableEntityMovingState
from business.stats.stats import BulletStats
from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IBullet
from business.world.interfaces import IGameWorld
from presentation.sprite import BulletSprite

class IceBullet(MovableEntity, IBullet):
    """A bullet that moves towards a target direction."""

    def __init__(self, pos_x: float, pos_y: float, dir_x: float, dir_y: float, health: int, stats: BulletStats, asset: str, current_state: MovableEntityMovingState = MovableEntityMovingState()): #pylint: disable=line-too-long
        """Initializes an IceBullet instance.

        Args:
            pos_x (float): The initial x-coordinate of the bullet.
            pos_y (float): The initial y-coordinate of the bullet.
            dir_x (float): The x-direction of the bullet's movement.
            dir_y (float): The y-direction of the bullet's movement.
            health (int): The health of the bullet.
            stats (BulletStats): The bullet's stats, including damage and size.
            asset (str): The asset representing the bullet.
            current_state (MovableEntityMovingState, optional): The initial state of the bullet's movement. Defaults to a new instance of MovableEntityMovingState.
        """
        super().__init__(pos_x, pos_y, stats, BulletSprite(pos_x, pos_y, asset, stats.size))
        self._logger.debug("Created %s", self)
        self.__dir_x = dir_x
        self.__dir_y = dir_y
        self._health = health
        self._damage_amount = stats.damage
        self.set_direction(dir_x, dir_y)
        self.current_state = current_state    

    @property
    def health(self) -> int:
        """Gets the health of the bullet.

        Returns:
            int: The current health of the bullet.
        """
        return self._health

    def take_damage(self, amount: int):
        """Reduces the bullet's health by the specified amount.

        Args:
            amount (int): The amount of damage to apply to the bullet.
        """
        self._health -= amount

    def update(self, world: IGameWorld):
        """Updates the state of the bullet in the given world.

        Args:
            world (IGameWorld): The game world where the bullet is present.
        """
        self.current_state.update_state(self)

    @property
    def damage_amount(self) -> int:
        """Gets the damage amount of the bullet.

        Returns:
            int: The damage amount of the bullet.
        """
        return self._damage_amount

    def __str__(self) -> str:
        """Returns a string representation of the bullet.

        Returns:
            str: A string describing the bullet's position and direction.
        """
        return f"Bullet(pos=({self._pos_x, self._pos_y}), dir=({self.__dir_x, self.__dir_y}))"

    def apply_effect(self, other_entity: MovableEntity):
        """Applies an ice effect to another entity.

        Args:
            other_entity (MovableEntity): The entity to which the ice effect will be applied.
        """
        other_entity.apply_ice_effect(100)
