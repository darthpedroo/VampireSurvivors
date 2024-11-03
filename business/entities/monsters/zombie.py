"""This module contains the Monster class, which represents a monster entity in the game."""

import random
from typing import List

from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IDamageable, IHasPosition, IHasSprite, IMonster
from business.entities.experience_gem import ExperienceGem
from business.handlers.cooldown_handler import CooldownHandler
from business.world.interfaces import IGameWorld
from presentation.sprite import Sprite
from business.entities.state_machine.movable_entity_frozen_state import MovableEntityFrozenState



class Zombie(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, src_x: int, src_y: int, sprite: Sprite, stats):
        super().__init__(src_x, src_y, stats, sprite)
        self.__health: int = 15
        self.__damage = 10
        self.__attack_range = 50
        self.__attack_cooldown = CooldownHandler(1000)
        self.__can_attack = False
        self._logger.debug("Created %s", self)
    
    
    
    def attack(self, target: IDamageable, direction_x: int, direction_y: int):
        """Attacks the target."""
        if not self.__attack_cooldown.is_action_ready():
            return

        if self._get_distance_to(target) < self.__attack_range:
            self.__can_attack = True
            target.take_damage(self.damage_amount)
            self.__attack_cooldown.put_on_cooldown()

    @property
    def damage_amount(self):
        return self.__damage


    def update(self, world: IGameWorld):
        
        direction_x, direction_y = self.get_direction_towards_the_player(world)
        
        monsters = [m for m in world.monsters if m != self]
        dx, dy = direction_x * self._stats.movement_speed, direction_y * self._stats.movement_speed
        
        if self.__can_attack == True:
            if direction_x > 0:
                self.sprite.change_to_attack_sprite("right")
            if direction_y > 0:
                self.sprite.change_to_attack_sprite("down")
            elif direction_y < 0:
                self.sprite.change_to_attack_sprite("up")
            elif direction_x < 0:
                self.sprite.change_to_attack_sprite("left")
        else:
            if self.movement_collides_with_entities(monsters) == None:
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
                #ABSTRAER ESTA LOGICA A LA CLASE MONSTER :V
                
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
        starting_number = 1
        true_luck = 100 - luck
        drop_rate = random.randint(starting_number, true_luck)
        if drop_rate <= 40:
            # Esto habría que sacarlo de un json con los datos de cada Gema.
            amount_of_experience = 2
            gem = ExperienceGem(self.pos_x, self.pos_y, amount_of_experience)
            return gem
        return None
