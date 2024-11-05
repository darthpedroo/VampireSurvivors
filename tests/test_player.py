import unittest
from unittest.mock import MagicMock
from business.entities.player import Player
from business.stats.stats import PlayerStats
from business.entities.weapon_handler import WeaponHandler
from business.perks.perks_handler import PerksHandler
from business.entities.experience_gem import ExperienceGem

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up test variables."""
        self.player_stats = PlayerStats(max_health=100, base_damage_multiplier=10, xp_multiplier=1, luck=0, regeneration_rate=1, regeneration_percentage=10)
        self.weapon_handler = MagicMock(WeaponHandler)
        self.perks_handler = MagicMock(PerksHandler)
        self.player = Player(pos_x=0, pos_y=0, player_stats=self.player_stats, weapon_handler=self.weapon_handler, perks_handler=self.perks_handler)

    def test_initial_health(self):
        """Test initial health of the player."""
        self.assertEqual(self.player.health, self.player_stats.max_health)

    def test_take_damage(self):
        """Test taking damage reduces health appropriately."""
        self.player.take_damage(30)
        self.assertEqual(self.player.health, 70)
        
        self.player.take_damage(100)
        self.assertEqual(self.player.health, 0)

    def test_pickup_gem(self):
        """Test picking up experience gems."""
        gem = ExperienceGem(1,1,amount=1)
        self.player.pickup_gem(gem)
        self.assertEqual(self.player.experience, 1)

    def test_level_up(self):
        """Test leveling up the player."""
        gem = ExperienceGem(1,1,amount=3)
        self.player.pickup_gem(gem)
        self.assertEqual(self.player.level, 2)
        self.assertEqual(self.player.experience, 1)

    def test_regenerate_health(self):
        """Test health regeneration."""
        self.player.take_damage(50)
        self.assertEqual(self.player.health, 50)

    def test_add_item(self):
        """Test adding an item."""
        self.player.add_item("TestWeapon")
        self.weapon_handler.add_item.assert_called_once_with("TestWeapon")

    def test_has_item(self):
        """Test checking if the player has an item."""
        self.weapon_handler.has_item.return_value = True
        self.assertTrue(self.player.has_item("TestWeapon"))

    def test_upgrading_item(self):
        """Test upgrading an item."""
        self.weapon_handler.upgrade_item_next_level.return_value = True
        success = self.player.upgrade_item_next_level("TestWeapon")
        self.assertTrue(success)

    def tearDown(self):
        """Tear down after each test if needed."""
        pass

if __name__ == "__main__":
    unittest.main()
