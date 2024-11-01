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

#    @abstractmethod
#    def move(self, direction_x: float, direction_y: float):
#        """Move the entity in the given direction based on its speed.

#        This method should update the entity's position and sprite.

#        Args:
#            direction_x (float): The direction in x-coordinate.
#            direction_y (float): The direction in y-coordinate.
#        """


class IMonster(IUpdatable, ICanMove, IDamageable, ICanDealDamage):
    """Interface for monster entities."""

    @abstractmethod
    def drop_loot(self):
        pass

    def get_nearest_enemy(self, monster_a: IHasSprite, monster_b: IHasSprite) -> tuple[IHasSprite, IHasSprite]:
        """Gets the nearest enemy in the map

        Args:
            monster_a (IHasSprite): 
            monster_b (IHasSprite): 

        Returns:
            tuple[IHasSprite, IHasSprite]:
        """
        distance_a = (monster_a.pos_x - self.pos_x) ** 2 + \
            (monster_a.pos_y - self.pos_y) ** 2
        distance_b = (monster_b.pos_x - self.pos_x) ** 2 + \
            (monster_b.pos_y - self.pos_y) ** 2

        if distance_a < distance_b:
            nearest_monster = monster_a
        else:
            nearest_monster = monster_b

        return nearest_monster

    def movement_collides_with_entities(self, entities: list["ICanMove"]) -> list["ICanMove"]:
        
        extra_hitbox_x = 30
        extra_hitbox_y = 30
        intended_position = self.sprite.rect.move(self.speed, self.speed).inflate(extra_hitbox_x, extra_hitbox_y)
        colliding_entities = [entity for entity in entities if entity.sprite.rect.colliderect(intended_position)]
    
        return colliding_entities if colliding_entities else None

    def check_which_entity_is_nearest_to_the_player(self, other_entity: "ImvoableEntity", world: "IGameWorld"):

        player = world.player

        distance_self_entity = (self.pos_x - player.pos_x,
                                self.pos_y - player.pos_y)
        distance_other_entity = (
            other_entity.pos_x - player.pos_x, other_entity.pos_y - player.pos_y)

        if distance_self_entity < distance_other_entity:
            return (self, other_entity)
        else:
            return (other_entity, self)

    def get_direction_towards_the_player(self, world: "IGameWorld") -> tuple[float, float]:
        """Gets the direction towards the player

        Args:
            world (IGameWorld): 

        Returns:
            tuple[float,float]: direction_x, direction_y
        """
        direction_x = world.player.pos_x - self.pos_x
        if direction_x != 0:
            direction_x = direction_x // abs(direction_x)

        direction_y = world.player.pos_y - self.pos_y
        if direction_y != 0:
            direction_y = direction_y // abs(direction_y)

        return direction_x, direction_y


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
