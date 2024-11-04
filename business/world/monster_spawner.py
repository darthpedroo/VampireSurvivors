"""This module contains the MonsterSpawner class."""

import logging
import random

import settings
from business.world.interfaces import IGameWorld, IMonsterSpawner
from business.entities.monsters.monsterfactory import MonsterFactory


class MonsterSpawner(IMonsterSpawner):
    """Spawns monsters in the game world."""

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self._max_monsters = 50

    def update(self, world: IGameWorld, camera):
        if len(world.monsters) < self._max_monsters:
            self.spawn_monster(world, camera)

    def spawn_monster(self, world: IGameWorld, camera):
        
        # Get camera bounds
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
