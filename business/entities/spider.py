"""This module contains the Monster class, which represents a monster entity in the game."""

import random
from typing import List

from business.entities.entity import MovableEntity
from business.entities.interfaces import IDamageable, IHasPosition, IHasSprite, IMonster
from business.entities.experience_gem import ExperienceGem
from business.handlers.cooldown_handler import CooldownHandler
from business.world.interfaces import IGameWorld
from presentation.sprite import Sprite


class Spider(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, src_x: int, src_y: int, sprite: Sprite):
        super().__init__(src_x, src_y, 2, sprite)
        self.__health: int = 10
        self.__damage = 10
        self.__attack_range = 150
        self.__attack_cooldown = CooldownHandler(1000)
        self._logger.debug("Created %s", self)
        self.__can_move = True

    def attack(self, target: IDamageable):
        """Attacks the target."""
        if not self.__attack_cooldown.is_action_ready():
            return

        if self._get_distance_to(target) < self.__attack_range:
            self.__can_move = False
            target.take_damage(self.damage_amount)
            self.__attack_cooldown.put_on_cooldown()
        else:
            self.__can_move = True

    @property
    def damage_amount(self):
        return self.__damage

    def __get_direction_towards_the_player(self, world: IGameWorld):
        direction_x = world.player.pos_x - self.pos_x
        if direction_x != 0:
            direction_x = direction_x // abs(direction_x)

        direction_y = world.player.pos_y - self.pos_y
        if direction_y != 0:
            direction_y = direction_y // abs(direction_y)

        return direction_x, direction_y

    def __movement_collides_with_entities(
        self, dx: float, dy: float, entities: List[IHasSprite]
    ) -> bool:
        new_position = self.sprite.rect.move(dx, dy).inflate(-10, -10)
        return any(e.sprite.rect.colliderect(new_position) for e in entities)

    def update(self, world: IGameWorld):
        direction_x, direction_y = self.__get_direction_towards_the_player(world)
        if (direction_x, direction_y) == (0, 0):
            return

        monsters = [m for m in world.monsters if m != self]
        dx, dy = direction_x * self.speed, direction_y * self.speed
        
        if not self.__movement_collides_with_entities(dx, dy, monsters) and self.__can_move:
            self.move(direction_x, direction_y)

        self.attack(world.player)

        super().update(world)

    def __str__(self):
        return f"Zombie(hp={self.health}, pos={self.pos_x, self.pos_y})"

    @property
    def health(self) -> int:
        return self.__health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        self.sprite.take_damage()

    def drop_loot(self, luck:int):
        starting_number = 1
        true_luck = 100 - luck
        drop_rate = random.randint(starting_number, true_luck)
        if drop_rate <= 40:
            amount_of_experience = 2 #Esto habría que sacarlo de un json con los datos de cada Gema.
            gem = ExperienceGem(self.pos_x, self.pos_y, amount_of_experience)
            return gem
        return None
