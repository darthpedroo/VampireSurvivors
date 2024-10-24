"""This module contains the Camera class."""

import pygame

import settings


class Camera:
    """A class representing the camera.

    The camera is used to follow the player and scroll the screen.

    Attributes:
        camera_rect (pygame.Rect): The rectangle representing the camera.
        world_width (int): The width of the world.
        world_height (int): The height of the world.
    """

    def __init__(self):
        self.camera_rect = pygame.Rect(0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        self.world_width = settings.WORLD_WIDTH
        self.world_height = settings.WORLD_HEIGHT

    def apply(self, rect):
        """Apply the camera offset to a rectangle.

        Args:
            rect (pygame.Rect): The rectangle to apply the camera offset to.
        """
        return rect.move(-self.camera_rect.left, -self.camera_rect.top)

    def update(self, target_rect):
        """Update the camera position based on the target rectangle.

        Args:
            target_rect (pygame.Rect): The target rectangle to follow.
        """
        # Center the camera on the target
        x = target_rect.centerx - settings.SCREEN_WIDTH // 2
        y = target_rect.centery - settings.SCREEN_HEIGHT // 2

        # Limit scrolling to world boundaries
        x = max(0, min(x, self.world_width - settings.SCREEN_WIDTH))
        y = max(0, min(y, self.world_height - settings.SCREEN_HEIGHT))

        # Update the camera rectangle
        self.camera_rect = pygame.Rect(x, y, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
