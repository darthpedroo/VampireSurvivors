#!/usr/bin/env python3
"""Runs the game"""
import logging

import pygame

import settings
from business.entities.player import Player
from business.world.game_world import GameWorld
from business.world.monster_spawner import MonsterSpawner
from business.world.tile_map import TileMap
from game import Game
from presentation.display import Display
from presentation.input_handler import InputHandler
from presentation.sprite import PlayerSprite


def initialize_player():
    """Initializes the player object"""
    x, y = 0, 0
    return Player(x, y, PlayerSprite(x, y))


def initialize_game_world():
    """Initializes the game world"""
    monster_spawner = MonsterSpawner()
    tile_map = TileMap()
    player = initialize_player()
    return GameWorld(monster_spawner, tile_map, player)


def main():
    """Main function to run the game"""
    # Initialize pygame
    pygame.init()

    # Logging configuration
    logging.basicConfig(
        level=logging.DEBUG,  # Change between INFO, WARNING or DEBUG as needed
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Initialize the game objects
    display = Display()
    world = initialize_game_world()
    display.load_world(world)
    input_handler = InputHandler(world)

    # Create a game instance and start it
    game = Game(display, world, input_handler)
    game.run()

    # Properly quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
