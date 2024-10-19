"""This module contains the InputHandler class, which handles user input for the game."""

import pygame

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
            self.__world.player.sprite.change_to_walk_sprite("up")
            self.__world.player.move(0, -1)
            is_moving = True
        if keys[pygame.K_s]:
            self.__direction = "down"
            self.__world.player.sprite.change_to_walk_sprite("down")
            self.__world.player.move(0, 1)
            is_moving = True
        if keys[pygame.K_a]:
            self.__direction = "left"
            self.__world.player.sprite.change_to_walk_sprite("left")
            self.__world.player.move(-1, 0)
            is_moving = True
        if keys[pygame.K_d]:
            self.__direction = "right"
            self.__world.player.sprite.change_to_walk_sprite("right")
            self.__world.player.move(1, 0)
            is_moving = True

        if is_moving == False:
            if self.__direction == "up":
                self.__world.player.sprite.change_to_idle_sprite("up")
            if self.__direction == "down":
                self.__world.player.sprite.change_to_idle_sprite("down")
            if self.__direction == "left":
                self.__world.player.sprite.change_to_idle_sprite("left")
            if self.__direction == "right":
                self.__world.player.sprite.change_to_idle_sprite("right")
        

    def process_input(self):
        keys = pygame.key.get_pressed()
        self.__example_method(keys)

