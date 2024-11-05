"""This module contains the MonsterSpawner class."""

import logging
import random
from json import JSONDecodeError

from business.world.interfaces import IGameWorld, IMonsterSpawner
from business.entities.monsters.monsterfactory import MonsterFactory
from business.handlers.cooldown_handler import CooldownHandler
from business.clock.clock import ClockSingleton
from persistence.monsters.monster_json import MonsterJson


class MonsterSpawner(IMonsterSpawner):
    """Spawns monsters in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__clock = ClockSingleton()
        self._max_monsters = 50
        self._monster_spawn_cooldown = self.__get_spawn_cooldown()
        self.__cooldown_handler = CooldownHandler(self._monster_spawn_cooldown)
        
    def load_monsters(self,world):
        try:
            monster_json_path = "./data/monsters.json"
            monster_json = MonsterJson(monster_json_path).get_monsters()
            
            for monster in monster_json:
                monster_type = monster["name"]
                pos_x = monster["pos_x"]
                pos_y = monster["pos_y"]
                new_monster = MonsterFactory().get_monster(monster_type, pos_x, pos_y)
                world.add_monster(new_monster)
        except JSONDecodeError:
            print("No hay nada en el Json para cargar monstruos !")
        
    def __get_spawn_cooldown(self):
        spawn_time = 500
        time_of_increase = 6000
        spawn_time -= self.__clock.get_time() / time_of_increase
        return spawn_time

    def update(self, world: IGameWorld, camera):
        if len(world.monsters) < self._max_monsters:
            self.spawn_monster(world, camera)

    def spawn_monster(self, world: IGameWorld, camera):
        if self.__cooldown_handler.is_action_ready():
            camera_bounds = {
                'left': camera.camera_rect.left,
                'right': camera.camera_rect.right,
                'top': camera.camera_rect.top,
                'bottom': camera.camera_rect.bottom
            }

            edge_positions = {
                'top': lambda: (random.randint(camera_bounds['left'], camera_bounds['right']), camera_bounds['top']),
                'bottom': lambda: (random.randint(camera_bounds['left'], camera_bounds['right']), camera_bounds['bottom']),
                'left': lambda: (camera_bounds['left'], random.randint(camera_bounds['top'], camera_bounds['bottom'])),
                'right': lambda: (camera_bounds['right'], random.randint(camera_bounds['top'], camera_bounds['bottom']))
            }

            edge = random.choice(list(edge_positions.keys()))
            pos_x, pos_y = edge_positions[edge]()

            monster = MonsterFactory().get_random_monster(pos_x, pos_y)
            world.add_monster(monster)
            self.__logger.debug("Spawning monster at (%d, %d) on the %s edge", pos_x, pos_y, edge)

            self.__cooldown_handler.put_on_cooldown()
