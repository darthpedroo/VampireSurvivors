import unittest
from unittest.mock import MagicMock
from business.entities.interfaces import IBullet, IExperienceGem, IHasSprite, IMonster, IPlayer
from business.world.interfaces import IGameWorld
from business.handlers.colission_handler import CollisionHandler


class TestCollisionHandler(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para cada prueba."""
        self.player = MagicMock(spec=IPlayer)
        self.gem = MagicMock(spec=IExperienceGem)
        self.bullet = MagicMock(spec=IBullet)
        self.monster = MagicMock(spec=IMonster)
        self.world = MagicMock(spec=IGameWorld)

        self.world.bullets = [self.bullet]
        self.world.monsters = [self.monster]
        self.world.experience_gems = [self.gem]

    def test_collides_with_success(self):
        """Prueba de colisión exitosa entre dos entidades."""
        self.player.sprite.rect.colliderect = MagicMock(return_value=True)
        self.gem.sprite.rect.colliderect = MagicMock(return_value=True)

        result = CollisionHandler._CollisionHandler__collides_with(self.player, self.gem)
        
        self.assertTrue(result)

    def test_handle_bullets_collision(self):
        """Prueba el manejo de colisiones entre balas y monstruos."""
        self.bullet.damage_amount = 10
        self.bullet.sprite.rect.colliderect = MagicMock(return_value=True)

        CollisionHandler._CollisionHandler__handle_bullets([self.bullet], [self.monster])
        
        self.monster.take_damage.assert_called_once_with(10)
        self.bullet.take_damage.assert_called_once_with(10)

    def test_handle_gems_collision(self):
        """Prueba el manejo de colisiones entre gemas y el jugador."""
        self.player.sprite.rect.colliderect = MagicMock(return_value=True)
        
        CollisionHandler._CollisionHandler__handle_gems([self.gem], self.player, self.world)
        
        self.player.pickup_gem.assert_called_once_with(self.gem)
        self.world.remove_experience_gem.assert_called_once_with(self.gem)

    def test_handle_collisions(self):
        """Prueba el manejo de colisiones en el mundo."""
        self.player.sprite.rect.colliderect = MagicMock(return_value=True)
        self.bullet.sprite.rect.colliderect = MagicMock(return_value=True)
        self.monster.sprite.rect.colliderect = MagicMock(return_value=True)

        CollisionHandler.handle_collisions(self.world)
        
        self.assertTrue(self.world.bullets)
        self.assertTrue(self.world.monsters)
        self.assertTrue(self.world.experience_gems)

        self.bullet.sprite.rect.colliderect.assert_called()


if __name__ == '__main__':
    unittest.main()
