import unittest
from unittest.mock import MagicMock, create_autospec
from business.entities.item_handler import ItemHandler
from business.entities.interfaces import UpgradableItem

class TestableItemHandler(ItemHandler):
    def add_item(self, item: UpgradableItem) -> None:
        self.list_of_items.append(item)

class TestItemHandler(unittest.TestCase):

    def setUp(self):
        self.item1 = create_autospec(UpgradableItem)
        self.item1.item_name = "Sword"
        self.item1._level = 1
        self.item1._max_level = 5
        self.item1.has_reached_max_level = MagicMock(return_value=False)
        self.item1.upgrade_next_level = MagicMock()
        self.item1._upgrades = MagicMock()

        self.item2 = create_autospec(UpgradableItem)
        self.item2.item_name = "Shield"
        self.item2._level = 5
        self.item2._max_level = 5
        self.item2.has_reached_max_level = MagicMock(return_value=True)
        self.item2._upgrades = MagicMock()

        self.handler = TestableItemHandler(list_of_items=[self.item1, self.item2])

    def test_get_all_items(self):
        items = self.handler.get_all_items()
        self.assertEqual(len(items), 2)
        self.assertIn(self.item1, items)
        self.assertIn(self.item2, items)

    def test_has_item(self):
        self.assertTrue(self.handler.has_item("Sword"))
        self.assertFalse(self.handler.has_item("Axe"))

    def test_get_item_level(self):
        level = self.handler.get_item_level("Sword")
        self.assertEqual(level, 1)
        with self.assertRaises(ValueError):
            self.handler.get_item_level("Axe")

if __name__ == "__main__":
    unittest.main()
