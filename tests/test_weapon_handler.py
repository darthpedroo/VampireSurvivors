import unittest
from unittest.mock import MagicMock
from business.exceptions import ItemOverflow
from business.entities.weapon_handler import WeaponHandler
from business.weapons.weapon_factory import WeaponFactory
from business.entities.item_handler import ItemHandler

class TestWeaponHandler(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.weapon_handler = WeaponHandler(list_of_items = [], max_items=3)

    def test_add_item_success(self):
        """Prueba agregar un arma cuando hay espacio disponible."""
        self.weapon_handler.add_item("The_Mega_Ice")
        self.assertEqual(len(self.weapon_handler._list_of_items), 1)

    def test_add_item_overflow(self):
        """Prueba agregar un arma que causa desbordamiento."""
        self.weapon_handler.add_item("The_Mega_Ice")
        self.weapon_handler.add_item("Toilet_spinner")
        self.weapon_handler.add_item("Manual_Joker")
        with self.assertRaises(ItemOverflow):
            self.weapon_handler.add_item("Auto_Joker")

    def test_use_every_weapon(self):
        """Prueba el uso de todas las armas."""
        mock_weapon1 = MagicMock()
        mock_weapon2 = MagicMock()
        
        self.weapon_handler._list_of_items = [mock_weapon1, mock_weapon2]
        
        player_pos_x = 10
        player_pos_y = 20
        mock_world = MagicMock()
        current_time = 1000
        player_base_damage_multiplier = 2
        player_base_attack_speed_multiplier = 3
        
        self.weapon_handler.use_every_weapon(player_pos_x, player_pos_y, mock_world, current_time,
                                              player_base_damage_multiplier, player_base_attack_speed_multiplier)
        
        mock_weapon1.use.assert_called_once_with(player_pos_x, player_pos_y, mock_world, current_time,
                                                  player_base_damage_multiplier, player_base_attack_speed_multiplier)
        mock_weapon2.use.assert_called_once_with(player_pos_x, player_pos_y, mock_world, current_time,
                                                  player_base_damage_multiplier, player_base_attack_speed_multiplier)

    def test_create_weapon_handler_json_data(self):
        """Prueba la creación de datos JSON del WeaponHandler."""
        weapon_mock = MagicMock()
        weapon_mock.create_weapon_json_data.return_value = {"name": "Sword"}
        
        self.weapon_handler._list_of_items = [weapon_mock]
        
        expected_output = {
            "list_of_items": [{"name": "Sword"}],
            "max_items": 3
        }
        
        self.assertEqual(self.weapon_handler.create_weapon_handler_json_data(), expected_output)


if __name__ == '__main__':
    unittest.main()
