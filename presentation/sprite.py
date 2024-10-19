"""Module for the Sprite class."""

import pygame

import settings
from presentation.tileset import Tileset


class Sprite(pygame.sprite.Sprite):
    """A class representing a sprite."""

    def __init__(self, image: pygame.Surface, rect: pygame.Rect, *groups):
        self._image: pygame.Surface = image
        self._rect: pygame.Rect = rect
        super().__init__(*groups)
        self.__is_in_damage_countdown = 0
        self.__original_image: pygame.Surface = image

    @property
    def image(self) -> pygame.Surface:
        """The image of the sprite.

        Returns:
            pygame.Surface: The image of the sprite.
        """
        return self._image

    @property
    def rect(self) -> pygame.Rect:
        """The rect of the sprite.

        Returns:
            pygame.Rect: The rect of the sprite. A rect is a rectangle that defines the position and size of the sprite.
        """
        return self._rect

    def update_pos(self, pos_x: float, pos_y: float):
        
        """Update the position of the sprite.

        Args:
            pos_x (float): The x-coordinate of the sprite.
            pos_y (float): The y-coordinate of the sprite.
        """
        
        self._rect.center = (int(pos_x), int(pos_y))

    def __restore_image(self):
        self._image = self.__original_image.copy()

    def __change_color(self, color: tuple[int, int, int]):
        self._image = self.__original_image.copy()  # Make a copy of the original image
        self._image.fill(color, special_flags=pygame.BLEND_MULT)  # Change color
        self._image.set_colorkey((0, 0, 0))  # Set transparency if necessary

    def __decrease_damage_countdown(self):
        self.__is_in_damage_countdown -= 1
        if self.__is_in_damage_countdown <= 0:
            self.__is_in_damage_countdown = 0
            self.__restore_image()

    def take_damage(self):
        """Take damage."""
        self.__change_color((255, 0, 0))
        self.__is_in_damage_countdown = 30

    def update(self, *args, **kwargs):
        """Update the sprite behavior"""
        super().__init__(*args, **kwargs)
        if self.__is_in_damage_countdown > 0:
            self.__decrease_damage_countdown()


class PlayerSprite(Sprite):
    """A class representing the player sprite."""

    ASSET_IDLE_UP = [
        "./assets/Idle_Up_1.png",
        "./assets/Idle_Up_2.png"
    ]
    
    ASSET_IDLE_DOWN = [
        "./assets/Idle_Down_1.png",
        "./assets/Idle_Down_2.png"
    ]
    
    ASSET_IDLE_RIGHT = [
        "./assets/Idle_Right_1.png",
        "./assets/Idle_Right_2.png"
    ]
    
    ASSET_IDLE_LEFT = [
        "./assets/Idle_Left_1.png",
        "./assets/Idle_Left_2.png"
    ]
    
    ASSET_WALK_UP = [
        "./assets/Walk_Up_1.png",
        "./assets/Walk_Up_2.png",
        "./assets/Walk_Up_3.png",
        "./assets/Walk_Up_4.png"
    ]
    
    ASSET_WALK_DOWN = [
        "./assets/Walk_Down_1.png",
        "./assets/Walk_Down_2.png",
        "./assets/Walk_Down_3.png",
        "./assets/Walk_Down_4.png"
    ]

    ASSET_WALK_RIGHT = [
        "./assets/Walk_Right_1.png",
        "./assets/Walk_Right_2.png",
        "./assets/Walk_Right_3.png",
        "./assets/Walk_Right_4.png"
    ]
    
    ASSET_WALK_LEFT = [
        "./assets/Walk_Left_1.png",
        "./assets/Walk_Left_2.png",
        "./assets/Walk_Left_3.png",
        "./assets/Walk_Left_4.png"
    ]

    def __init__(self, pos_x: float, pos_y: float):
        self.__current_idle_index = 0
        self.__current_walk_index = 0
        self.__frame_count = 0
        self.__frame_delay = 10
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        self._image = pygame.image.load(PlayerSprite.ASSET_IDLE_UP[0]).convert_alpha()
        self._image = pygame.transform.scale(self._image, settings.TILE_DIMENSION)
        
        self._rect = self._image.get_rect(center=(int(self.pos_x), int(self.pos_y)))
        
        super().__init__(self._image, self._rect)


    def __load_idle_image(self, direction_assets: list):
        image_path = direction_assets[self.__current_idle_index]
        image: pygame.Surface = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, settings.TILE_DIMENSION)
        self._image = image
        super().__init__(self._image, self._rect)

    def change_to_idle_up_sprite(self):
        self.__frame_count += 1

        if self.__frame_count >= self.__frame_delay:
            self.__current_idle_index = (self.__current_idle_index + 1) % 2
            self.__load_idle_image(PlayerSprite.ASSET_IDLE_UP)
            self.__frame_count = 0 

    def change_to_idle_down_sprite(self):
        self.__frame_count += 1

        if self.__frame_count >= self.__frame_delay:
            self.__current_idle_index = (self.__current_idle_index + 1) % 2
            self.__load_idle_image(PlayerSprite.ASSET_IDLE_DOWN)
            self.__frame_count = 0 

    def change_to_idle_right_sprite(self):
        self.__frame_count += 1

        if self.__frame_count >= self.__frame_delay:
            self.__current_idle_index = (self.__current_idle_index + 1) % 2
            self.__load_idle_image(PlayerSprite.ASSET_IDLE_RIGHT)
            self.__frame_count = 0 

    def change_to_idle_left_sprite(self):
        self.__frame_count += 1

        if self.__frame_count >= self.__frame_delay:
            self.__current_idle_index = (self.__current_idle_index + 1) % 2
            self.__load_idle_image(PlayerSprite.ASSET_IDLE_LEFT)
            self.__frame_count = 0 

    def __load_walk_image(self, direction_assets: list):
        image_path = direction_assets[self.__current_walk_index]
        
        image: pygame.Surface = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, settings.TILE_DIMENSION)
        self._image = image
        super().__init__(self._image, self._rect)
        self.__current_walk_index = (self.__current_walk_index + 1) % 4

    def change_to_walk_up_sprite(self):
        self.__frame_count += 1

        if self.__frame_count >= self.__frame_delay:
            self.__load_walk_image(PlayerSprite.ASSET_WALK_UP)
            self.__frame_count = 0 

    def change_to_walk_down_sprite(self):
        self.__frame_count += 1

        if self.__frame_count >= self.__frame_delay:
            self.__load_walk_image(PlayerSprite.ASSET_WALK_DOWN)
            self.__frame_count = 0

    def change_to_walk_right_sprite(self):
        self.__frame_count += 1

        if self.__frame_count >= self.__frame_delay:
            self.__load_walk_image(PlayerSprite.ASSET_WALK_RIGHT)
            self.__frame_count = 0

    def change_to_walk_left_sprite(self):
        self.__frame_count += 1

        if self.__frame_count >= self.__frame_delay:
            self.__load_walk_image(PlayerSprite.ASSET_WALK_LEFT)
            self.__frame_count = 0

    @property
    def image(self):
        return self._image

class MonsterSprite(Sprite):
    """A class representing the monster sprite."""

    ASSET = "./assets/monster.png"

    def __init__(self, pos_x: float, pos_y: float):
        image: pygame.Surface = pygame.image.load(MonsterSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, settings.TILE_DIMENSION)
        rect: pygame.rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)


class BulletSprite(Sprite):
    """A class representing the bullet sprite."""
    ASSET = "./assets/joker-dc.png"
    
    def __init__(self, pos_x: float, pos_y: float, size: int = 100):  # Default size is now 100
        # Create a surface for the bullet sprite with the specified size
        image: pygame.Surface = pygame.image.load(BulletSprite.ASSET).convert_alpha()
        
        # Scale the image to the desired size
        image = pygame.transform.scale(image, (size, size))  # Scale to size x size
        
        rect: pygame.rect = image.get_rect(center=(int(pos_x), int(pos_y)))  # Position the bullet at the given coordinates

        super().__init__(image, rect)


class BulletGuidedSprite(Sprite):
    def __init__(self, pos_x: float, pos_y: float, size: int = 20):  # Default size is now 100 (10x bigger)
        # Create a surface for the bullet sprite with the new size
        image = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)  # Double the size for width and height
        pygame.draw.circle(image, (255, 0, 0), (size, size), size // 2)  # Draw circle with 10x the size
        rect = image.get_rect(center=(int(pos_x), int(pos_y)))  # Position the bullet at the given coordinates

        super().__init__(image, rect)
    



class ExperienceGemSprite(Sprite):
    """A class representing the experience gem sprite."""

    ASSET = "./assets/experience_gems.png"

    def __init__(self, pos_x: float, pos_y: float):
        tileset = Tileset(
            self.ASSET, settings.TILE_HEIGHT, settings.TILE_HEIGHT, 2, 2
        )
        image: pygame.Surface = tileset.get_tile(0)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)
