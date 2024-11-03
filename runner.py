        #!/usr/bin/env python3
"""Runs the game"""
import logging

import pygame

import settings
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
    """Initializes the player object"""
    x, y = 500, 500
    
    max_health = 100
    movement_speed = 5
    base_damage_multiplier = 1
    base_attack_speed = 1
    regeneration_rate = 10000
    regeneration_percentage = 100
    xp_multiplier = 1
    luck = 1
    player_stats = PlayerStats(max_health, movement_speed, base_damage_multiplier, base_attack_speed, regeneration_rate, regeneration_percentage, xp_multiplier, luck)
    return Player(x, y, PlayerSprite(x, y),player_stats)


def initialize_game_world(display):
    """Initializes the game world"""
    monster_spawner = MonsterSpawner()
    tile_map = TileMap()
    player = initialize_player()
    #player.add_item("Manual_Joker")
    #player.add_item("Manual_Gun")
    #player.add_item("Auto_Joker")
    player.add_item("The_Mega_Ice")
    #player.add_item("Speedy Boots")
    player.add_item("Sacred Heart")

    return GameWorld(monster_spawner, tile_map, player, display)


def main():
    """Main function to run the game"""
    # Initialize pygame
    pygame.init()

    # Logging configuration
    logging.basicConfig(
        level=logging.INFO,  # Change between INFO, WARNING or DEBUG as needed
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
    pygame.quit()


if __name__ == "__main__":
    main()
