"""Module that defines the buttons of the GUI"""

import pygame
import random
from presentation.gui.interfaces import Clickable, Drawable

class Text():
    def __init__(self, text:str, height_offset:int,colour):
        self.text = text
        self.height_offset = height_offset
        self.colour = colour
    
    

class Button(Drawable, Clickable):
    """Class for buttons on the screen"""
    def __init__(self, width: int, height: int, colour, texts:[Text], sprite_path:str, screen, x_pos, y_pos,alpha_value: int = 256,):
        self.__width = width
        self.__height = height
        self.__alpha_value = alpha_value
        self.__colour = colour
        self.__screen = screen
        self.__surface = pygame.Surface((self.__width, self.__height))
        self.__surface.set_alpha(self.__alpha_value)
        self.__surface.fill(self.__colour)
        self.__rect = self.__surface.get_rect()
        self.__texts = texts
        self.__sprite_path = sprite_path
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = ""
    
    

    def draw(self, start_x: int, start_y: int):
        for text in self.__texts:
            self.add_text(text)
        self.__rect.topleft = (start_x, start_y)
        self.__screen.blit(self.__surface, self.__rect)
        self.add_image()

    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.__rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        return self.__rect.collidepoint(mouse_pos)
    
    def add_image(self):
        """Loads and draws an image at a specific position within the button."""
        if self.__sprite_path:
            item_image = pygame.image.load(self.__sprite_path)
            item_image = pygame.transform.scale(item_image, (30, 30))  
            image_x = self.__rect.x + 10  
            image_y = self.__rect.y + 10
            self.__screen.blit(item_image, (image_x, image_y))
    
    def add_text(self, text:Text,size:int=36, center:bool=False):
        
        font = pygame.font.Font(None, size)
        rendered_text = font.render(str(text.text), True, text.colour)
        
        height_offset = self.__height * text.height_offset / 100
        
        text_rect = rendered_text.get_rect()
        
        if center:
            text_rect.center = (self.__width // 2, height_offset)
        else:
            text_rect.topleft = (self.__width // 2 - text_rect.width // 2, height_offset)

        self.__surface.blit(rendered_text, text_rect)

    def change_colour(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        self.__colour = (r,g,b)
        self.__surface.fill(self.__colour)

    def get_colour(self):
        return self.__colour
    
    def set_name(self, new_name: str):
        """Sets the name of the text"""
        self.text = new_name
