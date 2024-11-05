import unittest
from business.perks.perk import Perk
from business.stats.stats import PerkStats, PlayerStats

class TestPerk(unittest.TestCase):
    def setUp(self):
        self.item_name = "Speedy Boots"
        self.max_level = 3
        self.upgrades = [{"level": 1, "boost": 5}, {"level": 2, "boost": 10}, {"level": 3, "boost": 15}]
        self.perk_stats = PlayerStats()
        self.asset = "./assets/perks/Speedy Boots.png"
        self.perk = Perk(self.item_name, self.max_level, self.upgrades, self.perk_stats, self.asset)

    def test_initialization(self):
        self.assertEqual(self.perk.item_name, self.item_name)
        self.assertEqual(self.perk._level, 1)
        self.assertEqual(self.perk._upgrades, self.upgrades)
        self.assertEqual(self.perk.item_stats, self.perk_stats)
        self.assertEqual(self.perk.sprite, self.asset)

    def test_create_perk_json_data(self):
        expected_data = {
            "item_name": self.item_name,
            "upgrades": self.upgrades,
            "level": 1,
            "perk_stats": self.perk_stats.create_player_stats_json_data()
        }
        self.assertEqual(self.perk.create_perk_json_data(), expected_data)

    def test_get_sprite(self):
        self.assertEqual(self.perk.get_sprite(), self.asset)

    def test_use(self):
        initial_level = self.perk._level + 1
        self.perk.use()
        if self.perk.has_reached_max_level():
            self.assertEqual(self.perk._level, initial_level)
        else:
            self.assertNotEqual(self.perk._level, initial_level)

    def test_apply_perk_boosts_to_player(self):
        player_stats = PlayerStats()
        self.perk.apply_perk_boosts_to_player(player_stats)

if __name__ == "__main__":
    unittest.main()
