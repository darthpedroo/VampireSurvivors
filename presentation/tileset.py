"""This module contains the Tileset class."""

import pygame


class Tileset:
    """A class representing a tileset."""

    def __init__(self, filename, tile_width, tile_height, columns, rows):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tiles = []

        image = pygame.image.load(filename).convert_alpha()
        image = pygame.transform.scale(image, (columns * tile_width, rows * tile_height))
        image_width, image_height = image.get_size()

        for y in range(0, image_height, tile_height):
            for x in range(0, image_width, tile_width):
                rect = pygame.Rect(x, y, tile_width, tile_height)
                tile_image = image.subsurface(rect)
                self.tiles.append(tile_image)

    def get_tile(self, index):
        """Get a tile by index."""
        return self.tiles[index]
