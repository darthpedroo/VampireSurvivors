"""Module that defines the Game class."""

import logging
import pygame
import settings
from business.exceptions import DeadPlayerException
from business.handlers.colission_handler import CollisionHandler
from business.handlers.death_handler import DeathHandler
from business.world.interfaces import IGameWorld
from business.clock.clock import ClockSingleton
from presentation.interfaces import IDisplay, IInputHandler


class Game:
    """
    Main game class.

    This is the game entrypoint.
    """

    def __init__(self, display: IDisplay, game_world: IGameWorld, input_handler: IInputHandler):
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__clock = ClockSingleton()
        self.__display = display
        self.__world = game_world
        self.__input_handler = input_handler
        self.__running = True

    def __process_game_events(self):
        """Process events like quit and key press."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__logger.debug("QUIT event detected")
                self.__running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if not self.__world.upgrading:
                        self.__world.change_paused_state()

    def run(self):
        """Starts the game loop."""
        self.__logger.debug("Starting the game loop.")
        while self.__running:
            try:
                self.__process_game_events()
                self.__input_handler.process_input()
                self.__world.update()
                CollisionHandler.handle_collisions(self.__world)
                DeathHandler.check_deaths(self.__world)
                self.__display.render_frame()
                self.__clock.tick()
            except DeadPlayerException:
                self.__running = False
