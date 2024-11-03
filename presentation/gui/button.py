"""Module that defines the buttons of the GUI"""

import pygame
from presentation.gui.interfaces import Clickable, Drawable

class Button(Drawable, Clickable):
    """Class for buttons on the screen"""
    def __init__(self, width: int, height: int, colour, screen, alpha_value: int = 256):
        self.__width = width
        self.__height = height
        self.__alpha_value = alpha_value
        self.__colour = colour
        self.__screen = screen
        self.__surface = pygame.Surface((self.__width, self.__height))
        self.__surface.set_alpha(self.__alpha_value)
        self.__surface.fill(self.__colour)
        self.__rect = self.__surface.get_rect()
        self.text = ""

    def draw(self, start_x: int, start_y: int):
        self.__rect.topleft = (start_x, start_y)
        self.__screen.blit(self.__surface, self.__rect)

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False

    def add_text(self, text: str, height_offset: int, colour=(255, 255, 255)):
        font = pygame.font.Font(None, 36)
        rendered_text = font.render(text, True, colour)
        height_offset = self.__height * height_offset / 100
        text_rect = rendered_text.get_rect(
            center=(self.__width // 2, height_offset))
        self.__surface.blit(rendered_text, text_rect)

    def set_name(self, new_name: str):
        """Sets the name of the text"""
        self.text = new_name
