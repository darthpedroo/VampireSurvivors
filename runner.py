#!/usr/bin/env python3
"""Module that runs the game."""

import logging
import pygame
from business.entities.player import Player
from business.world.game_world import GameWorld
from business.world.monster_spawner import MonsterSpawner
from business.world.tile_map import TileMap
from business.stats.stats import PlayerStats
from game import Game
from presentation.display import Display
from presentation.input_handler import InputHandler
from presentation.sprite import PlayerSprite


def initialize_player():
    """Initializes and returns the player object with default stats and items."""
    x, y = 500, 500
    max_health = 100
    movement_speed = 5
    base_damage_multiplier = 1
    base_attack_speed = 1
    regeneration_rate = 10000
    regeneration_percentage = 10
    xp_multiplier = 1
    luck = 1
    player_stats = PlayerStats(
        max_health=max_health,
        movement_speed=movement_speed,
        base_damage_multiplier=base_damage_multiplier,
        base_attack_speed=base_attack_speed,
        regeneration_rate=regeneration_rate,
        regeneration_percentage=regeneration_percentage,
        xp_multiplier=xp_multiplier,
        luck=luck
    )
    player = Player(x, y, PlayerSprite(x, y), player_stats)
    player.add_item("Manual_Gun")
    #player.add_item("Sacred Heart")
    #player.add_item("The_Mega_Ice")
    return player


def initialize_game_world(display):
    """Initializes and returns the game world with a player, spawner, and tile map."""
    monster_spawner = MonsterSpawner()
    tile_map = TileMap()
    player = initialize_player()
    return GameWorld(monster_spawner, tile_map, player, display)


def main():
    """Main function to run the game."""
    # Initialize pygame
    pygame.init() # pylint: disable=no-member

    # Logging configuration
    logging.basicConfig(
        level=logging.INFO,  # Change between INFO, WARNING, or DEBUG as needed
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    # Initialize the game objects
    display = Display()
    world = initialize_game_world(display)
    display.load_world(world)
    input_handler = InputHandler(world)

    # Create a game instance and start it
    game = Game(display, world, input_handler)
    game.run()

    # Properly quit Pygame
    pygame.quit() # pylint: disable=no-member


if __name__ == "__main__":
    main()
