"""This module contains the Shulker class."""

import random

from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IDamageable, IMonster
from business.entities.experience_gem import ExperienceGem
from business.handlers.cooldown_handler import CooldownHandler
from business.world.interfaces import IGameWorld
from business.stats.stats import EntityStats
from presentation.sprite import Sprite


class Shulker(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, src_x: int, src_y: int, sprite: Sprite, stats, shield_value:int=5):
        super().__init__(src_x, src_y, stats, sprite)
        self._name = "shulker"
        self.__health: int = self._stats.max_health
        self.__damage = 5
        self.__attack_range = 100
        self.__attack_cooldown = CooldownHandler(2000)
        self._logger.debug("Created %s", self)

        self.__shield = shield_value
          

    def create_monster_json_data(self):
        monster_data = {"pos_x": self.pos_x, "pos_y": self.pos_y, "name": self.name}
        return monster_data
    
    def attack(self, target: IDamageable):
        """Attacks the target."""
        if not self.__attack_cooldown.is_action_ready():
            return

        target.take_damage(self.__damage * self._stats.base_damage_multiplier)
        self.__attack_cooldown.put_on_cooldown()

    @property
    def damage_amount(self):
        return self.__damage * self._stats.base_damage_multiplier

    def update(self, world: IGameWorld):
        direction_x, direction_y = self.get_direction_towards_the_player(world)
        distance_to_player = self._get_distance_to(world.player)
        monsters = [m for m in world.monsters if m != self]

        if distance_to_player < self.__attack_range:
            self.attack(world.player)
        else:
            colliding_entities = self.movement_collides_with_entities(monsters)
            if colliding_entities:
                for entity in colliding_entities:
                    repulsion_x = entity.pos_x - self.pos_x
                    repulsion_y = entity.pos_y - self.pos_y

                    magnitude = (repulsion_x ** 2 + repulsion_y ** 2) ** 0.5
                    if magnitude != 0:
                        repulsion_x /= magnitude
                        repulsion_y /= magnitude

                    self.set_direction(-repulsion_x, -repulsion_y)
                    self.current_state.update_state(self)

                    entity.set_direction(repulsion_x, repulsion_y)
                    entity.current_state.update_state(entity)
            else:
                self.set_direction(direction_x, direction_y)
                self.current_state.update_state(self)

    def __str__(self):
        return f"Zombie(hp={self.health}, pos={self.pos_x, self.pos_y})"

    @property
    def health(self) -> int:
        return self.__health

    def take_damage(self, amount):
        
        damage_taken  = amount - self.__shield

        if damage_taken < 0:
            damage_taken = 0

        self.__health = max(0, self.__health - damage_taken)
        self.sprite.take_damage()

    def drop_loot(self, luck: int):
        try:
            starting_number = 1
            true_luck = 100 - luck
            drop_rate = random.randint(starting_number, true_luck)
        except ValueError:
            drop_rate = 100
        
        if drop_rate <= 40:
            amount_of_experience = 1
            gem = ExperienceGem(self.pos_x, self.pos_y, amount_of_experience)
            return gem
        return None
