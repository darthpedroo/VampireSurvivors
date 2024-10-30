"""This module contains the Monster class, which represents a monster entity in the game."""

import random
from typing import List

from business.entities.entity import MovableEntity
from business.entities.interfaces import IDamageable, IHasPosition, IHasSprite, IMonster
from business.entities.experience_gem import ExperienceGem
from business.handlers.cooldown_handler import CooldownHandler
from business.world.interfaces import IGameWorld
from presentation.sprite import Sprite


class Zombie(MovableEntity, IMonster):
    """A monster entity in the game."""

    def __init__(self, src_x: int, src_y: int, sprite: Sprite):
        super().__init__(src_x, src_y, 0.5, sprite)
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
        for i, e1 in enumerate(entities):
            if e1.sprite.rect.colliderect(new_position):
                for j, e2 in enumerate(entities):
                    if i != j and e1.sprite.rect.colliderect(e2.sprite.rect):
                        return e1, e2
                    else:
                        new_position = self.sprite.rect.move(
                            dx, dy).inflate(-10, -10)
        return None

    def __get_nearest_enemy(self, monster_a: IHasSprite, monster_b: IHasSprite) -> tuple[IHasSprite, IHasSprite]:

        distance_a = (monster_a.pos_x - self.pos_x) ** 2 + \
            (monster_a.pos_y - self.pos_y) ** 2
        distance_b = (monster_b.pos_x - self.pos_x) ** 2 + \
            (monster_b.pos_y - self.pos_y) ** 2

        if distance_a < distance_b:
            nearest_monster = monster_a
        else:
            nearest_monster = monster_b

        print(
            f"De los monstruos {monster_a} y {monster_b}, {nearest_monster} es el más cercano")

        return nearest_monster

    def update(self, world: IGameWorld):
        direction_x, direction_y = self.__get_direction_towards_the_player(
            world)
        if (direction_x, direction_y) == (0, 0):
            return

        monsters = [m for m in world.monsters if m != self]
        dx, dy = direction_x * self.speed, direction_y * self.speed
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
            if self.__movement_collides_with_entities(dx, dy, monsters) == None:
                self.move(direction_x, direction_y)
                if direction_x > 0:
                    self.sprite.change_to_walk_sprite("right")
                if direction_y > 0:
                    self.sprite.change_to_walk_sprite("down")
                elif direction_y < 0:
                    self.sprite.change_to_walk_sprite("up")
                elif direction_x < 0:
                    self.sprite.change_to_walk_sprite("left")
            else:
                e1, e2 = self.__movement_collides_with_entities(
                    dx, dy, monsters)
                nearest_enemy = self.__get_nearest_enemy(e1, e2,)
                nearest_enemy.move(direction_x, direction_y)
        self.attack(world.player, direction_x, direction_y)

        super().update(world)

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
