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

    @pos_x.setter
    @abstractmethod
    def pos_x(self, value: float) -> None:
        """Set the x-coordinate of the entity.

        Args:
            value (float): The new x-coordinate of the entity.
        """

    @property
    @abstractmethod
    def pos_y(self) -> float:
        """The y-coordinate of the entity.

        Returns:
            float: The y-coordinate of the entity.
        """

    @pos_y.setter
    @abstractmethod
    def pos_y(self, value: float) -> None:
        """Set the y-coordinate of the entity.

        Args:
            value (float): The new y-coordinate of the entity.
        """


class ICanMove(IHasPosition):
    """Interface for entities that can move."""


class IMonster(IUpdatable, ICanMove, IDamageable, ICanDealDamage):
    """Interface for monster entities."""
    
    
    @property
    def name(self):
        return self._name

    
    
    def drop_loot(self, luck: int):
        try:
            starting_number = 1
            true_luck = 100 - luck
            drop_rate = random.randint(starting_number, true_luck)
        except ValueError:
            drop_rate = 100
        
        if drop_rate <= 40:
            # Esto habría que sacarlo de un json con los datos de cada Gema.
            amount_of_experience = 1
            gem = ExperienceGem(self.pos_x, self.pos_y, amount_of_experience)
            return gem
        return None

    def get_nearest_enemy(self, monster_a: IHasSprite, monster_b: IHasSprite) -> tuple[IHasSprite, IHasSprite]: #pylint: disable=line-too-long
        """Gets the nearest enemy in the map.

        Args:
            monster_a (IHasSprite): The first monster to compare.
            monster_b (IHasSprite): The second monster to compare.

        Returns:
            tuple[IHasSprite, IHasSprite]: The nearest monster.
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
        """Checks for collisions with other entities during movement.

        Args:
            entities (list[ICanMove]): The list of entities to check for collisions.

        Returns:
            list[ICanMove]: A list of colliding entities, or None if no collisions occur.
        """
        extra_hitbox_x = 5
        extra_hitbox_y = 5
        intended_position = self.sprite.rect.move(self._stats.movement_speed,self._stats.movement_speed).inflate(extra_hitbox_x, extra_hitbox_y) #pylint: disable=line-too-long
        colliding_entities = [entity
                              for entity in entities
                              if entity.sprite.rect.colliderect(intended_position)]

        return colliding_entities if colliding_entities else None

    def check_which_entity_is_nearest_to_the_player(self, other_entity: "ImvoableEntity", world: "IGameWorld"): #pylint: disable=line-too-long
        """Checks which entity is nearest to the player.

        Args:
            other_entity (ImvoableEntity): The other entity to compare.
            world (IGameWorld): The game world.

        Returns:
            tuple: A tuple of the nearest entity and the other entity.
        """
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
        """Gets the direction towards the player.

        Args:
            world (IGameWorld): The game world.

        Returns:
            tuple[float, float]: The direction towards the player (direction_x, direction_y).
        """
        direction_x = world.player.pos_x - self.pos_x
        if direction_x != 0:
            direction_x = direction_x // abs(direction_x)

        direction_y = world.player.pos_y - self.pos_y
        if direction_y != 0:
            direction_y = direction_y // abs(direction_y)

        return direction_x, direction_y


class IMove(ABC):
    """Interface for the different moves/actions a player can perform (e.g., Attack, Heal, Ulti)."""

    @abstractmethod
    def perform_move(self, entity: "Entity"):
        """Makes the entity perform the implemented move.

        Args:
            entity (Entity): The entity that performs the move.
        """


class IUpgradable(ABC):
    """Interface for the items that can be upgraded."""

    @abstractmethod
    def upgrade_level(self, level: int):
        """Adds the modification for the upgradable item.

        Args:
            level (int): The level to upgrade.
        """

    @abstractmethod
    def upgrade_next_level(self):
        """Increases the level by one."""

    @abstractmethod
    def load_upgrades(self):
        """Loads the upgrades."""


class UpgradableItem(ABC):
    """Represents an upgradable item."""

    def __init__(self, item_name: str, max_level: int,level:int = 0):
        self.item_name = item_name
        #self._level = "NIGGER"
        self._upgrades = []
        self._max_level = max_level
        #self.load_upgrades(self._level)
    
    @abstractmethod
    def get_sprite(self):
        """Gets the sprite of an item
        """

    def get_upgrade_info_by_level(self, level: int):
        """Gets the upgrade information based on the level.

        Args:
            level (int): The level of the item.

        Returns:
            level_info: The information of the upgrade on a specific level.
        """
        try:
            level_info = self._upgrades[level]["DESCRIPTION"] #ojo
        except IndexError as error:
            print("ERROR CON EL INDEX!", error)
        return level_info

    def load_upgrades(self, upgrades:[dict], level, stats):

        """Loads the upgrades for the current level."""
        for level in range(level+1):
            self.upgrade_level(level, upgrades, stats)

    def upgrade_level(self, level: int, upgrades, stats):
        """Upgrades the item at the specified level.

        Args:
            level (int): The level to upgrade.
            stats: The stats to modify based on the upgrade.
        """
        
        current_upgrade = upgrades[level - 1]  # ojo
        attribute_to_modify = current_upgrade.get('ATTRIBUTE')
        new_value = current_upgrade.get('VALUE')
        if current_upgrade.get('OPERATION') == 'MULTIPLICATION':
            new_value = getattr(stats, attribute_to_modify) * new_value
            setattr(stats, attribute_to_modify, new_value)
        if current_upgrade.get('OPERATION') == 'SUM':
            new_value = getattr(stats, attribute_to_modify) + new_value
            setattr(stats, attribute_to_modify, new_value)
        
        if attribute_to_modify == 'cooldown':
            self._cooldown_handler.update_cooldown_time(new_value)

    def upgrade_next_level(self, upgrades, stats):
        """Upgrades to the next level if the maximum level has not been reached."""
        if self._level < self._max_level:
            self._level += 1
            self.upgrade_level(self._level, upgrades, stats)
        else:
            print("Max level acquired")

    def has_reached_max_level(self):
        """Checks if the item has reached its maximum level.

        Returns:
            bool: True if the maximum level is reached, False otherwise.
        """
        return self._level == self._max_level


class IAttack(IMove):
    """Interface for attack moves."""

    @abstractmethod
    def is_attack_critical(self):
        """Checks if the current attack is a critical one."""

    @abstractmethod
    def is_cool_down_over(self):
        """Checks if cooldown is over to attack again."""


class IBullet(IUpdatable, ICanMove, IDamageable, ICanDealDamage):
    """Interface for bullet entities."""

    @abstractmethod
    def apply_effect(self, other_entity: "MovableEntity"):
        """Applies the effect of the bullet.

        Args:
            other_entity (MovableEntity): The entity affected by the bullet.
        """
    
    @abstractmethod
    def create_bullet_json_data(self):
        """Creates a parser for bullet json data 
        """


class IExperienceGem(IUpdatable, IHasPosition):
    """Interface for experience gem entities."""

    @property
    @abstractmethod
    def amount(self) -> int:
        """The amount of experience the gem provides.

        Returns:
            int: The experience amount of the gem.
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
    def luck(self) -> int:
        """The luck of the player.

        Returns:
            int: The luck of the player.
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
