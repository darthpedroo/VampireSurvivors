import unittest
from unittest.mock import patch, MagicMock
from business.entities.monsters.monsterfactory import MonsterFactory
from business.entities.monsters.zombie import Zombie
from business.entities.monsters.spider import Spider
from business.stats.stats import EntityStats
from presentation.sprite import ZombieSprite, SpiderSprite

class TestMonsterFactory(unittest.TestCase):

    @patch("business.entities.monsters.monsterfactory.ClockSingleton")
    def setUp(self, MockClockSingleton):
        self.mock_clock = MockClockSingleton.return_value
        self.mock_clock.get_time.return_value = 5000

    @patch("random.choice", return_value="zombie")
    def test_get_random_monster_returns_zombie(self, mock_choice):
        monster = MonsterFactory.get_random_monster(10, 20)
        self.assertIsInstance(monster, Zombie)
        self.assertEqual(monster._pos_x, 10)
        self.assertEqual(monster._pos_y, 20)
        self.assertEqual(monster.sprite.size, 100)

    @patch("random.choice", return_value="spider")
    def test_get_random_monster_returns_spider(self, mock_choice):
        monster = MonsterFactory.get_random_monster(30, 40)
        self.assertIsInstance(monster, Spider)
        self.assertEqual(monster._pos_x, 30)
        self.assertEqual(monster._pos_y, 40)
        self.assertEqual(monster.sprite.size, 100)

    @patch("business.entities.monsters.monsterfactory.ClockSingleton")
    def test_get_monster_zombie(self, MockClockSingleton):
        MockClockSingleton.return_value.get_time.return_value = 5000
        monster = MonsterFactory.get_monster("zombie", 50, 60)
        self.assertIsInstance(monster, Zombie)
        self.assertEqual(monster._pos_x, 50)
        self.assertEqual(monster._pos_y, 60)
        self.assertEqual(monster.sprite.size, 100)

    @patch("business.entities.monsters.monsterfactory.ClockSingleton")
    def test_get_monster_spider(self, MockClockSingleton):
        MockClockSingleton.return_value.get_time.return_value = 5000
        monster = MonsterFactory.get_monster("spider", 70, 80)
        self.assertIsInstance(monster, Spider)
        self.assertEqual(monster._pos_x, 70)
        self.assertEqual(monster._pos_y, 80)
        self.assertEqual(monster.sprite.size, 100)

    def test_get_monster_invalid_type_raises_error(self):
        with self.assertRaises(ValueError) as context:
            MonsterFactory.get_monster("invalid_monster", 0, 0)
        self.assertEqual(str(context.exception), "Not A Valid Enemy")

if __name__ == "__main__":
    unittest.main()
