"""This module contains the Monster class, which represents a monster entity in the game."""

import random
from typing import List

from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IDamageable, IHasPosition, IHasSprite, IMonster
from business.entities.experience_gem import ExperienceGem
from business.handlers.cooldown_handler import CooldownHandler
from business.world.interfaces import IGameWorld
from presentation.sprite import Sprite


class Spider(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, src_x: int, src_y: int, sprite: Sprite):
        super().__init__(src_x, src_y, 1, sprite)
        self.__health: int = 10
        self.__damage = 5
        self.__attack_range = 100
        self.__attack_cooldown = CooldownHandler(2000)
        self._logger.debug("Created %s", self)
        self.__can_move = True

    def attack(self, target: IDamageable):
        """Attacks the target."""
        if not self.__attack_cooldown.is_action_ready():
            return

        target.take_damage(self.damage_amount)
        self.__attack_cooldown.put_on_cooldown()

    @property
    def damage_amount(self):
        return self.__damage

    def update(self, world: IGameWorld):

        direction_x, direction_y = self.get_direction_towards_the_player(world)
        distance_to_player = self._get_distance_to(world.player)
        monsters = [m for m in world.monsters if m != self]

        if distance_to_player < self.__attack_range:
            self.attack(world.player)
        elif self.movement_collides_with_entities(monsters, world) is not None:

            nearest_entity = self.movement_collides_with_entities(
                monsters, world)

            nearest_entity.set_direction(direction_x, direction_y)
            nearest_entity.current_state.update_state(self)

        elif self.movement_collides_with_entities(monsters, world) is None:
            self.set_direction(direction_x, direction_y)
            self.current_state.update_state(self)

    def __str__(self):
        return f"Zombie(hp={self.health}, pos={self.pos_x, self.pos_y})"

    @property
    def health(self) -> int:
        return self.__health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        self.sprite.take_damage()

    def drop_loot(self, luck: int):
        starting_number = 1
        true_luck = 100 - luck
        drop_rate = random.randint(starting_number, true_luck)
        if drop_rate <= 40:
            # Esto habría que sacarlo de un json con los datos de cada Gema.
            amount_of_experience = 2
            gem = ExperienceGem(self.pos_x, self.pos_y, amount_of_experience)
            return gem
        return None
