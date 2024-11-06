"""This module contains the InputHandler class, which handles user input for the game."""

import pygame

from business.entities.state_machine.movable_entity_idle_state import MovableEntityIdleState
from business.world.game_world import GameWorld
from presentation.interfaces import IInputHandler

class InputHandler(IInputHandler):
    """Handles user input for the game."""

    def __init__(self, world: GameWorld):
        self.__world = world
        self.__direction = None

    def __example_method(self, keys):
        is_moving = False
        if keys[pygame.K_w]: 
            self.__direction = "up"
            x_dir = 0
            y_dir = -1
            self.__world.update_player(x_dir,y_dir)
            is_moving = True

        if keys[pygame.K_s]: 
            self.__direction = "down"
            x_dir = 0
            y_dir = 1
            self.__world.update_player(x_dir,y_dir)
            is_moving = True

        if keys[pygame.K_a]: 
            self.__direction = "left"
            x_dir = -1
            y_dir = 0
            self.__world.update_player(x_dir,y_dir)
            is_moving = True

        if keys[pygame.K_d]: 
            self.__direction = "right"
            x_dir = 1
            y_dir = 0
            self.__world.update_player(x_dir,y_dir)
            is_moving = True
        
        if keys[pygame.K_r]:
            self.__world.player.ultimate(self.__world)

        if is_moving is False and self.__world.paused is False:
            new_state = MovableEntityIdleState()
            self.__world.change_player_state(new_state)

            if self.__direction == "up":
                self.__world.player.sprite.change_to_idle_sprite("up")
            if self.__direction == "down":
                self.__world.player.sprite.change_to_idle_sprite("down")
            if self.__direction == "left":
                self.__world.player.sprite.change_to_idle_sprite("left")
            if self.__direction == "right":
                self.__world.player.sprite.change_to_idle_sprite("right")

        elif is_moving:
            self.__world.player.sprite.change_to_walk_sprite(self.__direction)

    def process_input(self):
        if self.__world._paused is False:
            keys = pygame.key.get_pressed()
            self.__example_method(keys)
