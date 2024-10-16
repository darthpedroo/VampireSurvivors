# pylint: disable=C0114,C0115,C0116
import unittest

from business.entities.bullet import Bullet


class TestBullet(unittest.TestCase):
    def setUp(self):
        self.bullet = Bullet(0, 0, 10, 10, 5)

    def test_initial_health(self):
        self.assertEqual(self.bullet.health, 5)

    def test_damage_amount(self):
        self.assertEqual(self.bullet.damage_amount, 5)

    def test_take_damage(self):
        self.bullet.take_damage(2)
        self.assertEqual(self.bullet.health, 3)

    def test_update_position(self):
        x_distance, y_distance = 3, 4

        self.bullet = Bullet(0, 0, x_distance, y_distance, 1)
        self.bullet.update(None)

        x, y = self.bullet.pos_x, self.bullet.pos_y
        self.assertAlmostEqual(x, 0.6)
        self.assertAlmostEqual(y, 0.8)
        self.assertAlmostEqual(x / x_distance, y / y_distance)

    def test_update_position_vertical(self):
        x_distance, y_distance = 0, 10

        self.bullet = Bullet(0, 0, x_distance, y_distance, 1)
        self.bullet.update(None)

        x, y = self.bullet.pos_x, self.bullet.pos_y
        self.assertAlmostEqual(x, 0)
        self.assertAlmostEqual(y, 1)

    def test_update_position_horizontal(self):
        x_distance, y_distance = 10, 0

        self.bullet = Bullet(0, 0, x_distance, y_distance, 1)
        self.bullet.update(None)

        x, y = self.bullet.pos_x, self.bullet.pos_y
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 0)

    def test_update_position_non_zero_src(self):
        src_x, src_y, dst_x, dst_y = 5, 5, 10, 10

        self.bullet = Bullet(src_x, src_y, dst_x, dst_y, 1)
        self.bullet.update(None)

        x, y = self.bullet.pos_x, self.bullet.pos_y
        self.assertAlmostEqual(x, 5.707, 2)
        self.assertAlmostEqual(y, 5.707, 2)


if __name__ == "main":
    unittest.main()
