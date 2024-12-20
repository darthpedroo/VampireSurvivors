"""This module contains the Zombie class."""

import random

from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IDamageable, IMonster
from business.entities.experience_gem import ExperienceGem
from business.handlers.cooldown_handler import CooldownHandler
from business.world.interfaces import IGameWorld
from presentation.sprite import Sprite
from business.stats.stats import EntityStats



class Zombie(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, src_x: int, src_y: int, sprite: Sprite, stats:EntityStats):
        super().__init__(src_x, src_y, stats, sprite)
        self._name = "zombie"
        self.__health: int = self._stats.max_health
        self.__damage = 10 
        self.__attack_range = 50
        self.__attack_cooldown = CooldownHandler(1000)
        self.__can_attack = False
        self._logger.debug("Created %s", self)

    def create_monster_json_data(self):
        monster_data = {"pos_x": self.pos_x, "pos_y": self.pos_y, "name": self.name}
        return monster_data

    @property
    def damage_amount(self):
        return self.__damage * self._stats.base_damage_multiplier

    def attack(self, target: IDamageable, direction_x: int, direction_y: int):
        """Attacks the target."""

        can_attack = False

        number = random.randint(0,100)
        if self._stats.precision >= number:
            can_attack = True
        

        if not self.__attack_cooldown.is_action_ready():
            return

        if self._get_distance_to(target) < self.__attack_range:
            if can_attack:
                self.__can_attack = True
                target.take_damage(self.damage_amount)
                self.__attack_cooldown.put_on_cooldown()
            else:
                self.__attack_cooldown.put_on_cooldown()
                print("EL ZOMBIE NO PUDO ATACAR PORQUE NO TUVO PRECISION!")
        else:
            self.__can_attack = False

    @property
    def attack_cooldown(self):
        return self.__attack_cooldown
    
    @property
    def damage(self):
        return self.__damage

    def update(self, world: IGameWorld):
        direction_x, direction_y = self.get_direction_towards_the_player(world)

        monsters = [m for m in world.monsters if m != self]

        if self.__can_attack is True:
            if direction_x > 0:
                self.sprite.change_to_attack_sprite("right")
            if direction_y > 0:
                self.sprite.change_to_attack_sprite("down")
            elif direction_y < 0:
                self.sprite.change_to_attack_sprite("up")
            elif direction_x < 0:
                self.sprite.change_to_attack_sprite("left")
        else:
            if self.movement_collides_with_entities(monsters) is None:
                self.set_direction(direction_x, direction_y)
                if direction_x > 0:
                    self.sprite.change_to_walk_sprite("right")
                if direction_y > 0:
                    self.sprite.change_to_walk_sprite("down")
                elif direction_y < 0:
                    self.sprite.change_to_walk_sprite("up")
                elif direction_x < 0:
                    self.sprite.change_to_walk_sprite("left")
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

        self.current_state.update_state(self)
        self.attack(world.player, direction_x, direction_y)

    def __str__(self):
        return f"Zombie(hp={self.health}, pos={self.pos_x, self.pos_y})"

    @property
    def health(self) -> int:
        return self.__health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
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
