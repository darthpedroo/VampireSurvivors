        initial_health = self.spider.health
        damage_amount = 20
        self.spider.take_damage(damage_amount)
        
        # Verificar que se reduce la salud al tomar daño
        self.assertEqual(self.spider.health, initial_health - damage_amount)
        self.sprite_mock.take_damage.assert_called_once()

    def test_update_attacks_when_in_range(self):
        world_mock = MagicMock()
        world_mock.player = MagicMock()
        self.spider._get_distance_to = MagicMock(return_value=50)  # Dentro del rango de ataque
        self.spider.attack = MagicMock()
        
        self.spider.update(world_mock)
        
        # Verificar que se llama a `attack` cuando el jugador está dentro del rango de ataque
        self.spider.attack.assert_called_once_with(world_mock.player)

    def test_update_moves_towards_player_when_out_of_range(self):
        world_mock = MagicMock()
        world_mock.player = MagicMock()
        self.spider._get_distance_to = MagicMock(return_value=150)  # Fuera del rango de ataque
        self.spider.set_direction = MagicMock()
        self.spider.current_state.update_state = MagicMock()

        # Dirección simulada hacia el jugador
        direction_x, direction_y = 1, 0
        self.spider.get_direction_towards_the_player = MagicMock(return_value=(direction_x, direction_y))
        
        self.spider.update(world_mock)
        
        # Verificar que la araña se mueve hacia el jugador
        self.spider.set_direction.assert_called_once_with(direction_x, direction_y)
        self.spider.current_state.update_state.assert_called_once_with(self.spider)

    def test_update_avoids_collisions_with_other_monsters(self):
        world_mock = MagicMock()
        monster_mock = MagicMock()
        world_mock.monsters = [monster_mock]
        
        # Definir valor de retorno para _get_distance_to y mockear colisiones
        self.spider._get_distance_to = MagicMock(return_value=150)
        self.spider.movement_collides_with_entities = MagicMock(return_value=[monster_mock])
        self.spider.set_direction = MagicMock()
        
        self.spider.update(world_mock)

        # Aquí puedes agregar verificaciones específicas para las interacciones de colisión

        
