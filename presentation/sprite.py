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
        self.__sprite_color_damage_countdown = 0
        self.__sprite_color_heal_countdown = 0
        self.__original_image: pygame.Surface = image

    @property
    def sprite_color_countdown(self):
        return self.__sprite_color_countdown

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

    def restore_image(self):
        self._image = self.__original_image.copy()

    def __change_color(self, color: tuple[int, int, int]):
        self._image = self.__original_image.copy()  # Make a copy of the original image
        # Change color
        self._image.fill(color, special_flags=pygame.BLEND_MULT)
        self._image.set_colorkey((0, 0, 0))  # Set transparency if necessary

    def __decrease_damage_countdown(self):
        self.__sprite_color_countdown -= 1
        if self.__sprite_color_countdown == 0:
            self.restore_image()


    def take_damage(self):
        """Take damage."""
        self.__change_color((255, 0, 0))
        self.__sprite_color_countdown = 1


    def heal(self):
        """Healing Animation"""
        self.__sprite_color_countdown = 0
        self.__change_color((0, 255, 200))
        self.__sprite_color_heal_countdown = 300

    def freeze(self, countdown: int=100):
        self.__sprite_color_countdown = 0
        self.__change_color((40, 200, 255))
        self.__sprite_color_countdown = countdown


    def update(self, *args, **kwargs):
        """Update the sprite behavior"""
        super().update(*args, **kwargs)

        if self.__sprite_color_damage_countdown > 0:
            self.__decrease_damage_countdown()


class PlayerSprite(Sprite):
    """A class representing the player sprite."""

    ASSET_WALK_TILESET = "./assets/player/Walk.png"
    ASSET_IDLE_TILESET = "./assets/player/Idle.png"

    WALK_DOWN = [0, 1, 2 , 3]
    WALK_UP = [5, 6, 7 , 8]
    WALK_RIGHT = [10, 11, 12, 13]
    WALK_LEFT = [15, 16, 17, 18]

    IDLE_DOWN = [0, 1]
    IDLE_UP = [3, 4]
    IDLE_RIGHT = [6, 7]
    IDLE_LEFT = [9, 10]

    def __init__(self, pos_x: float, pos_y: float):
        self.__current_idle_index = 0
        self.__current_walk_index = 0
        self.__frame_count = 0
        self.__frame_delay = 6
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = None

        self.walk_tileset = Tileset(self.ASSET_WALK_TILESET, 32, 32, 5, 4)
        self.idle_tileset = Tileset(self.ASSET_IDLE_TILESET, 32, 32, 3, 4)

        self._image = self.idle_tileset.get_tile(0)
        self._image = pygame.transform.scale(self._image, (60, 80))
        self._rect = self._image.get_rect(
            center=(int(self.pos_x), int(self.pos_y)))

        super().__init__(self._image, self._rect)

    def __load_idle_image(self):
        if self.direction == "up":
            index = PlayerSprite.IDLE_UP[self.__current_idle_index]
        if self.direction == "down":
            index = PlayerSprite.IDLE_DOWN[self.__current_idle_index]
        if self.direction == "left":
            index = PlayerSprite.IDLE_DOWN[self.__current_idle_index]
        if self.direction == "right":
            index = PlayerSprite.IDLE_DOWN[self.__current_idle_index]
        
        self._image = self.idle_tileset.get_tile(index)
        self._image = pygame.transform.scale(self._image, (60, 80))
        self._rect = self._image.get_rect(center=(int(self.pos_x), int(self.pos_y)))
        super().__init__(self._image, self._rect)
        self.__current_idle_index = (self.__current_idle_index + 1) % 2

    def change_to_idle_sprite(self, direction: str):
        self.__frame_count += 1
        self.direction = direction

        if self.__frame_count >= self.__frame_delay:
            self.__load_idle_image()
            self.__frame_count = 0

    def __load_walk_image(self):
        if self.direction == "up":
            index = PlayerSprite.WALK_UP[self.__current_walk_index]
        if self.direction == "down":
            index = PlayerSprite.WALK_DOWN[self.__current_walk_index]
        if self.direction == "left":
            index = PlayerSprite.WALK_LEFT[self.__current_walk_index]
        if self.direction == "right":
            index = PlayerSprite.WALK_RIGHT[self.__current_walk_index]

        self._image = self.walk_tileset.get_tile(index)
        self._image = pygame.transform.scale(self._image, (60, 80))
        self._rect = self._image.get_rect(center=(int(self.pos_x), int(self.pos_y)))
        super().__init__(self._image, self._rect)
        self.__current_walk_index = (self.__current_walk_index + 1) % 4

    def change_to_walk_sprite(self, direction: str):
        self.__frame_count += 1
        self.direction = direction

        if self.__frame_count >= self.__frame_delay:
            self.__load_walk_image()
            self.__frame_count = 0

    @property
    def image(self):
        return self._image


class ZombieSprite(Sprite):
    """A class representing the zombie sprite."""

    ASSET_WALK_UP = [
        "./assets/zombie/Zombie_Walk_Up_1.png",
        "./assets/zombie/Zombie_Walk_Up_2.png",
        "./assets/zombie/Zombie_Walk_Up_3.png",
        "./assets/zombie/Zombie_Walk_Up_4.png"
    ]

    ASSET_WALK_DOWN = [
        "./assets/zombie/Zombie_Walk_Down_1.png",
        "./assets/zombie/Zombie_Walk_Down_2.png",
        "./assets/zombie/Zombie_Walk_Down_3.png",
        "./assets/zombie/Zombie_Walk_Down_4.png"
    ]

    ASSET_WALK_RIGHT = [
        "./assets/zombie/Zombie_Walk_Right_1.png",
        "./assets/zombie/Zombie_Walk_Right_2.png",
        "./assets/zombie/Zombie_Walk_Right_3.png",
        "./assets/zombie/Zombie_Walk_Right_4.png"
    ]

    ASSET_WALK_LEFT = [
        "./assets/zombie/Zombie_Walk_Left_1.png",
        "./assets/zombie/Zombie_Walk_Left_2.png",
        "./assets/zombie/Zombie_Walk_Left_3.png",
        "./assets/zombie/Zombie_Walk_Left_4.png"
    ]

    ASSET_ATTACK_UP = [
        "./assets/zombie/Zombie_Attack_Up_1.png",
        "./assets/zombie/Zombie_Attack_Up_2.png",
        "./assets/zombie/Zombie_Attack_Up_3.png",
        "./assets/zombie/Zombie_Attack_Up_4.png"
    ]

    ASSET_ATTACK_DOWN = [
        "./assets/zombie/Zombie_Attack_Down_1.png",
        "./assets/zombie/Zombie_Attack_Down_2.png",
        "./assets/zombie/Zombie_Attack_Down_3.png",
        "./assets/zombie/Zombie_Attack_Down_4.png"
    ]

    ASSET_ATTACK_RIGHT = [
        "./assets/zombie/Zombie_Attack_Right_1.png",
        "./assets/zombie/Zombie_Attack_Right_2.png",
        "./assets/zombie/Zombie_Attack_Right_3.png",
        "./assets/zombie/Zombie_Attack_Right_4.png"
    ]

    ASSET_ATTACK_LEFT = [
        "./assets/zombie/Zombie_Attack_Left_1.png",
        "./assets/zombie/Zombie_Attack_Left_2.png",
        "./assets/zombie/Zombie_Attack_Left_3.png",
        "./assets/zombie/Zombie_Attack_Left_4.png"
    ]

    def __init__(self, pos_x: float, pos_y: float):
        self.__current_walk_index = 0
        self.__current_attack_index = 0
        self.__frame_count = 0
        self.__frame_delay = 10
        self.__attack_frame_delay = 8
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = None

        self._image = pygame.image.load(
            ZombieSprite.ASSET_WALK_UP[0]).convert_alpha()
        self._image = pygame.transform.scale(self._image, (60, 75))

        self._rect = self._image.get_rect(
            center=(int(self.pos_x), int(self.pos_y)))

        super().__init__(self._image, self._rect)

    def __load_walk_image(self, direction_assets: list):
        image_path = direction_assets[self.__current_walk_index]
        image: pygame.Surface = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, (60, 75))
        self._image = image
        super().__init__(self._image, self._rect)
        self.__current_walk_index = (self.__current_walk_index + 1) % 4

    def __load_attack_image(self, direction_assets: list):
        image_path = direction_assets[self.__current_attack_index]
        image: pygame.Surface = pygame.image.load(image_path).convert_alpha()
        image = pygame.transform.scale(image, (60, 75))
        self._image = image
        super().__init__(self._image, self._rect)
        self.__current_attack_index = (self.__current_attack_index + 1) % 4

    def change_to_walk_sprite(self, direction: str):
        self.__frame_count += 1
        self.direction = direction

        if self.__frame_count >= self.__frame_delay:
            if direction == "up":
                self.__load_walk_image(ZombieSprite.ASSET_WALK_UP)
            if direction == "down":
                self.__load_walk_image(ZombieSprite.ASSET_WALK_DOWN)
            if direction == "left":
                self.__load_walk_image(ZombieSprite.ASSET_WALK_LEFT)
            if direction == "right":
                self.__load_walk_image(ZombieSprite.ASSET_WALK_RIGHT)
            self.__frame_count = 0

    def change_to_attack_sprite(self, direction: str):
        self.__frame_count += 1
        self.direction = direction

        if self.__frame_count >= self.__attack_frame_delay:
            if direction == "up":
                self.__load_attack_image(ZombieSprite.ASSET_ATTACK_UP)
            if direction == "down":
                self.__load_attack_image(ZombieSprite.ASSET_ATTACK_DOWN)
            if direction == "left":
                self.__load_attack_image(ZombieSprite.ASSET_ATTACK_LEFT)
            if direction == "right":
                self.__load_attack_image(ZombieSprite.ASSET_ATTACK_RIGHT)
            self.__frame_count = 0


class SpiderSprite(Sprite):
    """A class representing the monster sprite."""

    ASSET = "./assets/spider.png"

    def __init__(self, pos_x: float, pos_y: float):
        image: pygame.Surface = pygame.image.load(
            SpiderSprite.ASSET).convert_alpha()
        image = pygame.transform.scale(image, settings.TILE_DIMENSION)
        rect: pygame.rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)


class BulletSprite(Sprite):
    """A class representing the bullet sprite."""
    # ASSET = "./assets/joker-dc.png"

    # Default size is now 100
    def __init__(self, pos_x: float, pos_y: float, asset: str, size: int = 100):
        self.asset = asset
        # Create a surface for the bullet sprite with the specified size
        image: pygame.Surface = pygame.image.load(
            self.asset).convert_alpha()

        # Scale the image to the desired size
        image = pygame.transform.scale(
            image, (size, size))  # Scale to size x size

        # Position the bullet at the given coordinates
        rect: pygame.rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)


class ExperienceGemSprite(Sprite):
    """A class representing the experience gem sprite."""

    ASSET = "./assets/experience_gems.png"

    def __init__(self, pos_x: float, pos_y: float):
        tileset = Tileset(
            self.ASSET, settings.TILE_WIDTH, settings.TILE_HEIGHT, 2, 2
        )
        image: pygame.Surface = tileset.get_tile(0)
        rect: pygame.Rect = image.get_rect(center=(int(pos_x), int(pos_y)))

        super().__init__(image, rect)
