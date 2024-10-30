"""This module contains interfaces for the entities in the game."""

from abc import ABC, abstractmethod

from presentation.sprite import Sprite


class ICanDealDamage(ABC):
    """Interface for entities that can deal damage."""

    @property
    @abstractmethod
    def damage_amount(self) -> int:
        """The amount of damage the entity can deal.

        Returns:
            int: The amount of damage the entity can deal.
        """


class IDamageable(ABC):
    """Interface for entities that can take damage."""

    @property
    @abstractmethod
    def health(self) -> int:
        """The health of the entity.

        Returns:
            int: The health of the entity.
        """

    @abstractmethod
    def take_damage(self, amount: int):
        """Take damage.

        Args:
            amount (int): The amount of damage to take.
        """


class IUpdatable(ABC):
    """Interface for entities that can be updated."""

    @abstractmethod
    def update(self, world):
        """Update the state of the entity."""


class IHasSprite(ABC):
    """Interface for entities that have a sprite."""

    @property
    @abstractmethod
    def sprite(self) -> Sprite:
        """The sprite of the entity.

        Returns:
            Sprite: The sprite of the entity.
        """


class IHasPosition(IHasSprite):
    """Interface for entities that have a position."""

    @property
    @abstractmethod
    def pos_x(self) -> float:
        """The x-coordinate of the entity.

        Returns:
            float: The x-coordinate of the entity.
        """
        pass

    @pos_x.setter
    @abstractmethod
    def pos_x(self, value: float) -> None:
        """Set the x-coordinate of the entity.

        Args:
            value (float): The new x-coordinate of the entity.
        """
        pass

    @property
    @abstractmethod
    def pos_y(self) -> float:
        """The y-coordinate of the entity.

        Returns:
            float: The y-coordinate of the entity.
        """
        pass

    @pos_y.setter
    @abstractmethod
    def pos_y(self, value: float) -> None:
        """Set the y-coordinate of the entity.

        Args:
            value (float): The new y-coordinate of the entity.
        """
        pass


class ICanMove(IHasPosition):
    """Interface for entities that can move."""

    @property
    @abstractmethod
    def speed(self) -> float:
        """The speed of the entity.

        Returns:
            float: The speed of the entity.
        """

    @abstractmethod
    def move(self, direction_x: float, direction_y: float):
        """Move the entity in the given direction based on its speed.

        This method should update the entity's position and sprite.

        Args:
            direction_x (float): The direction in x-coordinate.
            direction_y (float): The direction in y-coordinate.
        """


class IMonster(IUpdatable, ICanMove, IDamageable, ICanDealDamage):
    """Interface for monster entities."""

    @abstractmethod
    def drop_loot(self):
        pass


class IMove(ABC):
    """Interface for the different moves/actions a player can perform. Attack / Heal / Ulti
    """

    @abstractmethod
    def perform_move(self, entity: "Entity"):
        """Hace que la entidad realice el movimiento implementado

        Args:
            entity (Entity): La entidad que realiza el movimiento
        """


class IUpgradable(ABC):
    """Interface for the items that can be upgraded"""

    @abstractmethod
    def upgrade_level(self, level: int):
        """Adds the modification for the Upgradable"""
        pass

    @abstractmethod
    def upgrade_next_level(self):
        """Increases level by one"""
        pass

    @abstractmethod
    def load_upgrades(self):
        pass


class IAttack(IMove):
    def is_attack_critical(self):
        """Checks if the current attack is a critical one 
        """

    def is_cool_down_over(self):
        """Checks if cooldown is over to attack again
        """


class IBullet(IUpdatable, ICanMove, IDamageable, ICanDealDamage):
    """Interface for bullet entities."""

    @abstractmethod
    def apply_affect(self, other_entity: "MovableEntity"):
        """Applies the effect of the bullet"""


class IExperienceGem(IUpdatable, IHasPosition):
    """Interface for experience gem entities."""

    @property
    @abstractmethod
    def amount(self) -> int:
        """The amount of experience the gem gives.

        Returns:
            int: The amount of experience the gem gives.
        """


class IPlayer(IUpdatable, ICanMove, IDamageable, ICanDealDamage):
    """Interface for the player entity."""

    @abstractmethod
    def pickup_gem(self, gem: IExperienceGem):
        """Picks up an experience gem.

        Args:
            gem (IExperienceGem): The experience gem to pick up.
        """

    @property
    @abstractmethod
    def level(self) -> int:
        """The level of the player.

        Returns:
            int: The level of the player.
        """

    @property
    @abstractmethod
    def experience(self) -> int:
        """The experience of the player.

        Returns:
            int: The experience of the player.
        """

    @property
    @abstractmethod
    def experience_to_next_level(self) -> int:
        """The experience required to reach the next level.

        Returns:
            int: The experience required to reach the next level.
        """
