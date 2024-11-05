import os
import json
import unittest
import tempfile
from unittest.mock import MagicMock
from persistence.bullets.bullets_json import BulletJson  
from business.entities.interfaces import IBullet

class TestBulletJsonIntegration(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        self.bullet_dao = BulletJson(self.test_file.name)

    def tearDown(self):
        self.test_file.close()
        try:
            os.remove(self.test_file.name)
        except OSError as e:
            print(f"Error deleting temp file: {e}")

    def test_bullet_final_mega_integracion(self):
        
        bullet_mock = MagicMock(spec=IBullet)
        bullet_mock.create_bullet_json_data.return_value = {
            "name": "Bullet",
            "pos_x": 100,
            "pos_y": 150,
            "dir_x": 1,
            "dir_y": 0,
            "health": 100,
            "stats": {
                "movement_speed": 10,
                "damage": 5
            }
        }

        self.bullet_dao.save_bullets([bullet_mock])

        with open(self.test_file.name, 'r') as outfile:
            data = json.load(outfile)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0], bullet_mock.create_bullet_json_data.return_value)

        bullets = self.bullet_dao.get_bullets()
        self.assertEqual(len(bullets), 1)
        self.assertEqual(bullets[0], bullet_mock.create_bullet_json_data.return_value)

        self.bullet_dao.delete_bullets()
        with open(self.test_file.name, 'r') as outfile:
            data = outfile.read()
            self.assertEqual(data, '') 

if __name__ == '__main__':
    unittest.main()
