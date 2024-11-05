#!/usr/bin/env python3
"""Module that runs the game."""

from json import JSONDecodeError
import logging
import pygame
from business.entities.player import Player
from business.world.game_world import GameWorld
from business.world.monster_spawner import MonsterSpawner
from business.world.tile_map import TileMap
from business.stats.stats import PlayerStats
from business.entities.weapon_handler import WeaponHandler
from game import Game
from presentation.display import Display
from presentation.input_handler import InputHandler
from persistence.player.player_json import PlayerJson
from persistence.clock.clock_json import ClockJson
from business.weapons.weapon_factory import WeaponFactory
from business.perks.perk_factory import PerkFactory
from business.perks.perks_handler import PerksHandler

player_json_path = "./data/player.json"
player_json = PlayerJson(player_json_path)

clock_json_path = "./data/clock.json"
clock_json = ClockJson(clock_json_path)

def initialize_player():
    """Initializes and returns the player object with default stats and items."""
    
    try:
        x,y = player_json.get_player_pos()
        max_health = player_json.get_player_stats_from_parameter("max_health")
        movement_speed = player_json.get_player_stats_from_parameter("movement_speed")
        base_damage_multiplier = player_json.get_player_stats_from_parameter("base_damage_multiplier")
        base_attack_speed = player_json.get_player_stats_from_parameter("base_attack_speed")
        regeneration_rate = player_json.get_player_stats_from_parameter("regeneration_rate")
        regeneration_percentage = player_json.get_player_stats_from_parameter("regeneration_percentage")
        xp_multiplier = player_json.get_player_stats_from_parameter("xp_multiplier")
        luck = player_json.get_player_stats_from_parameter("luck")
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
        
        weapons = []
        for item in player_json.get_weapon_handler():
            
            item_name = item["item_name"]
            level = item["level"]
            new_weapon = WeaponFactory.create_weapon(item_name, level)
            weapons.append(new_weapon)

        perks = []
        for perk in player_json.get_perks_handler():
            item_name = perk["item_name"]
            level = perk["level"]
            new_perk = PerkFactory.create_perk(item_name,level)
            perks.append(new_perk)
        
        level = player_json.get_player()["level"]
        experience = player_json.get_player()["experience"]
        weapon_handler = WeaponHandler(weapons)
        perks_handler = PerksHandler(player_stats,perks)
        
        player = Player(x, y,player_stats,weapon_handler,perks_handler,experience,level)
    
    except JSONDecodeError:
        x,y = 500,500
        max_health = 100
        movement_speed = 5
        base_damage_multiplier = 1
        base_attack_speed = 1
        regeneration_rate = 10000
        regeneration_percentage = 10
        xp_multiplier = 1
        luck = 0
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
        weapon_handler = WeaponHandler()
        perks_handler = PerksHandler(player_stats)
        player = Player(x, y,  player_stats,weapon_handler, perks_handler)
        player.add_item("Manual_Gun")
        player.add_item("Sacred Heart")
        player.add_item("The_Mega_Ice")
        

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
    

    player = world.player
    player_json.save_player(player)
    
    clock_json.save_clock(world.clock)

    # Properly quit Pygame
    pygame.quit() # pylint: disable=no-member


if __name__ == "__main__":
    main()
