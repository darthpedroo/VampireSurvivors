"""Module that contains the TileMap class."""

import random
import settings
from business.world.interfaces import ITileMap


class TileMap(ITileMap):
    """Class that represents the tile map of the game world."""

    def __init__(self):
        self.map_data = self.__generate_tile_map()

    def __generate_tile_map(self):
        # Crear un array 2D de tile indices
        tile_map = [[0 for _ in range(settings.WORLD_COLUMNS)] for _ in range(settings.WORLD_ROWS)]

        for row in range(settings.WORLD_ROWS):
            for col in range(settings.WORLD_COLUMNS):
                # Esquinas
                if (row == 0 and col == 0):  # Superior izquierda
                    tile_map[row][col] = 0
                elif (row == 0 and col == settings.WORLD_COLUMNS - 1):  # Superior derecha
                    tile_map[row][col] = 2
                elif (row == settings.WORLD_ROWS - 1 and col == 0):  # Inferior izquierda
                    tile_map[row][col] = 20
                elif (row == settings.WORLD_ROWS - 1 and
                      col == settings.WORLD_COLUMNS - 1):  # Inferior derecha
                    tile_map[row][col] = 22

                # Bordes
                elif row == 0:  # Parte superior
                    tile_map[row][col] = 1
                elif col == 0:  # Parte izquierda
                    tile_map[row][col] = 10
                elif col == settings.WORLD_COLUMNS - 1:  # Parte derecha
                    tile_map[row][col] = 12
                elif row == settings.WORLD_ROWS - 1:  # Parte inferior
                    tile_map[row][col] = 21

                # Interior
                else:
                    random_tile = random.randint(1,10)
                    if random_tile > 2:
                        tile_map[row][col] = 11
                    else:
                        tile_map[row][col] = 15

        return tile_map



    def get(self, row, col) -> int:
        """Get the tile index at a specific row and column"""
        return self.map_data[row][col]
