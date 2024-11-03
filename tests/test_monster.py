"""Unit tests for the Zombie monster class."""

import unittest
from unittest.mock import MagicMock, patch

from business.entities.interfaces import IDamageable
from business.entities.monsters.zombie import Zombie


class TestMonster(unittest.TestCase):
    """Tests for the Zombie monster class."""

    def setUp(self):
        """Sets up a Zombie instance for testing."""
        self.monster = Zombie(5, 5, MagicMock())

    def test_attack(self):
        """Tests that the attack method reduces the target's health when action is ready."""
        target_mock = MagicMock(spec=IDamageable)
        target_mock.health = 10

        # Mock the attack cooldown to be ready
        with patch.object(
            self.monster._Monster__attack_cooldown_handler,  # pylint: disable=no-member, protected-access
            "is_action_ready",
            return_value=True,
        ):
            self.monster.attack(target_mock)

        # Verify that take_damage was called with the correct damage amount
        target_mock.take_damage.assert_called_once_with(self.monster.damage_amount)

    def test_attack_is_not_called_when_action_is_not_ready(self):
        """Tests that the attack method does not reduce the target's health when action is not ready."""
        target_mock = MagicMock(spec=IDamageable)
        target_mock.health = 10

        # Mock the attack cooldown to be not ready
        with patch.object(
            self.monster._Monster__attack_cooldown_handler, # pylint: disable=no-member, protected-access
            "is_action_ready",
            return_value=False,
        ):
            self.monster.attack(target_mock)

        # Verify that take_damage was not called
        target_mock.take_damage.assert_not_called()
