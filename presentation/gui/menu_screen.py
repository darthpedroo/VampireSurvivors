from settings import BG_COLOR
import pygame
from presentation.gui.interfaces import Drawable


class MenuScreen(Drawable):
    def __init__(self, width: int, height: int, alpha_value:int, colour, screen):
        self.__width = width
        self.__height = height
        self.__alpha_value = alpha_value
        self.__colour = colour
        self.__screen = screen
        self.__drawables = []
    
    def draw(self,start_x:int, start_y:int):
        menu = pygame.Surface((self.__width, self.__height))
        menu.set_alpha(self.__alpha_value)
        menu.fill((self.__colour))
        self.__screen.blit(menu, (start_x,start_y))
    
    def add_text(self, text: str, height_offset:int = 10):
        font = pygame.font.Font(None, 36)
        text = font.render(text, True, (255, 255, 255))
        
        height_offset = self.__height * height_offset/100
        
        text_rect = text.get_rect(center=(self.__width // 2, 0 + height_offset ))
        self.__screen.blit(text, text_rect)
