import unittest
from unittest.mock import MagicMock, patch

from business.entities.interfaces import IDamageable
from business.entities.monster import Monster


class TestMonster(unittest.TestCase):
    def setUp(self):
        self.monster = Monster(5, 5, MagicMock())

    def test_attack(self):
        target_mock = MagicMock(spec=IDamageable)
        target_mock.health = 10

        with patch.object(
            self.monster._Monster__attack_cooldown_handler,  # pylint: disable=W0212
            "is_action_ready",
            return_value=True,
        ):
            self.monster.attack(target_mock)

        target_mock.take_damage.assert_called_once_with(self.monster.damage_amount)

    def test_attack_is_not_called_when_action_is_not_ready(self):
        target_mock = MagicMock(spec=IDamageable)
        target_mock.health = 10

        with patch.object(
            self.monster._Monster__attack_cooldown_handler,  # pylint: disable=W0212
            "is_action_ready",
            return_value=False,
        ):
            self.monster.attack(target_mock)

        target_mock.take_damage.assert_not_called()
