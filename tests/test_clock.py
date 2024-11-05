import unittest
from unittest.mock import patch, MagicMock
from business.clock.clock import ClockSingleton

class TestClockSingleton(unittest.TestCase):

    @patch("business.clock.clock.pygame.time.Clock")
    def setUp(self, MockClock):
        ClockSingleton._instance = None
        self.mock_clock = MockClock.return_value
        self.clock_instance = ClockSingleton()

    def test_singleton_instance(self):
        another_instance = ClockSingleton()
        self.assertIs(self.clock_instance, another_instance)

    def test_initial_ms_value(self):
        self.assertEqual(self.clock_instance.get_time(), 0)

    @patch("business.clock.clock.settings.FPS", 60)
    def test_tick_advances_time_when_not_paused(self):
        self.mock_clock.tick.return_value = 16
        tick = self.clock_instance.tick()
        self.assertEqual(tick, 16)
        self.assertEqual(self.clock_instance.get_time(), 16)

    @patch("business.clock.clock.settings.FPS", 60)
    def test_tick_does_not_advance_time_when_paused(self):
        self.clock_instance.set_paused(True)
        self.mock_clock.tick.return_value = 16
        tick = self.clock_instance.tick()
        self.assertEqual(tick, 0)
        self.assertEqual(self.clock_instance.get_time(), 0) 

    def test_set_and_get_time(self):
        self.clock_instance.set_ms(5000)
        self.assertEqual(self.clock_instance.get_time(), 5000)

    def test_create_clock_json_data(self):
        self.clock_instance.set_ms(12345)
        expected_json = {"ms": 12345}
        self.assertEqual(self.clock_instance.create_clock_json_data(), expected_json)

if __name__ == "__main__":
    unittest.main()
