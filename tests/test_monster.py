import unittest
import random
import pygame
from unittest.mock import MagicMock
from business.entities.state_machine.entity import MovableEntity
from business.entities.interfaces import IDamageable, IMonster
from business.handlers.cooldown_handler import CooldownHandler
from presentation.sprite import Sprite
from business.stats.stats import EntityStats
from business.entities.monsters.spider import Spider
from business.entities.monsters.zombie import Zombie
from business.entities.experience_gem import ExperienceGem

class TestZombieAndSpider(unittest.TestCase):

    def setUp(self):
        pygame.init()
        pygame.display.set_mode((1, 1))
        self.mock_world = MagicMock()
        self.mock_sprite = MagicMock(spec=Sprite)
        self.mock_stats = MagicMock(spec=EntityStats)
        self.mock_stats.max_health = 100
        self.mock_stats.base_damage_multiplier = 1.5
        self.mock_stats.movement_speed = 5
        self.mock_target = MagicMock(spec=IDamageable)

        self.zombie = Zombie(0, 0, self.mock_sprite, self.mock_stats)
        self.spider = Spider(0, 0, self.mock_sprite, self.mock_stats)

    def test_zombie_attack_within_range(self):
        self.zombie._get_distance_to = MagicMock(return_value=25)
        self.zombie._Zombie__attack_cooldown = MagicMock()
        self.zombie._Zombie__attack_cooldown.is_action_ready.return_value = True

        self.zombie.attack(self.mock_target, 1, 1)
        
        self.mock_target.take_damage.assert_called_once_with(self.zombie.damage_amount)
        self.zombie._Zombie__attack_cooldown.put_on_cooldown.assert_called_once()

    def test_spider_attack_within_range(self):
        self.spider._get_distance_to = MagicMock(return_value=75)
        self.spider._Spider__attack_cooldown = MagicMock()
        self.spider._Spider__attack_cooldown.is_action_ready.return_value = True

        self.spider.attack(self.mock_target)
        
        self.mock_target.take_damage.assert_called_once_with(self.spider.damage_amount)
        self.spider._Spider__attack_cooldown.put_on_cooldown.assert_called_once()

    def test_zombie_update_sets_direction(self):
        self.mock_world.monsters = [self.spider]
        self.zombie.get_direction_towards_the_player = MagicMock(return_value=(1, 0))
        self.zombie.movement_collides_with_entities = MagicMock(return_value=None)
        self.zombie.sprite.change_to_walk_sprite = MagicMock()
        self.zombie.set_direction = MagicMock()

        self.zombie.update(self.mock_world)

        self.zombie.set_direction.assert_called_with(1, 0)
        self.zombie.sprite.change_to_walk_sprite.assert_called_with("right")

    def test_zombie_take_damage(self):
        initial_health = self.zombie.health
        self.zombie.take_damage(20)

        self.assertEqual(self.zombie.health, initial_health - 20)
        self.zombie.sprite.take_damage.assert_called_once()

    def test_spider_drop_loot(self):
        random.randint = MagicMock(return_value=30)
        gem = self.spider.drop_loot(70)

        self.assertIsNotNone(gem)
        self.assertIsInstance(gem, ExperienceGem)

    def test_spider_drop_no_loot(self):
        random.randint = MagicMock(return_value=50)
        gem = self.spider.drop_loot(30)

        self.assertIsNone(gem)

if __name__ == "__main__":
    unittest.main()
