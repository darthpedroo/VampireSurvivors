"""Module for displaying the game world."""

import pygame

import settings
from business.world.game_world import GameWorld
from presentation.camera import Camera
from presentation.interfaces import IDisplay
from presentation.tileset import Tileset
from presentation.gui.menu_screen import MenuScreen
from presentation.gui.button import Button

class Display(IDisplay):
    """Class for displaying the game world."""

    def __init__(self):
        # Set the window display mode
        self.__screen = pygame.display.set_mode(settings.SCREEN_DIMENSION)
        self.__minutes = 0
        self.__seconds = 0
        self.__frames = 0

        # Set the window title
        pygame.display.set_caption(settings.GAME_TITLE)

        # Initialize the camera
        self.camera = Camera()

        self.__ground_tileset = self.__load_ground_tileset()
        self.__world: GameWorld = None

    def __load_ground_tileset(self):
        return Tileset(
            "./assets/ground_tileset.png", settings.TILE_WIDTH, settings.TILE_HEIGHT, 10, 16
        )

    def __render_ground_tiles(self):
        # Calculate the range of tiles to render based on the camera position
        start_col = max(0, self.camera.camera_rect.left // settings.TILE_WIDTH)
        end_col = min(
            settings.WORLD_COLUMNS, (self.camera.camera_rect.right // settings.TILE_WIDTH) + 1
        )
        start_row = max(0, self.camera.camera_rect.top // settings.TILE_HEIGHT)
        end_row = min(
            settings.WORLD_ROWS, (self.camera.camera_rect.bottom // settings.TILE_HEIGHT) + 1
        )

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                # Get the tile index from the tile map
                tile_index = self.__world.tile_map.get(row, col)
                tile_image = self.__ground_tileset.get_tile(tile_index)

                # Calculate the position on the screen
                x = col * settings.TILE_WIDTH - self.camera.camera_rect.left
                y = row * settings.TILE_HEIGHT - self.camera.camera_rect.top

                self.__screen.blit(tile_image, (x, y))

    def __draw_player_health_bar(self):
        player = self.__world.player

        # Define the health bar dimensions
        bar_width = settings.TILE_WIDTH
        bar_height = 5
        bar_x = player.sprite.rect.centerx - bar_width // 2 - self.camera.camera_rect.left
        bar_y = player.sprite.rect.bottom + 5 - self.camera.camera_rect.top

        # Draw the background bar (red)
        bg_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
        pygame.draw.rect(self.__screen, (255, 0, 0), bg_rect)

        # Draw the health bar (green)
        health_percentage = player.health / 100  # Assuming max health is 100 (code smell?)
        health_width = int(bar_width * health_percentage)
        health_rect = pygame.Rect(bar_x, bar_y, health_width, bar_height)
        pygame.draw.rect(self.__screen, (0, 255, 0), health_rect)

    def __draw_experience_bar(self):
        bar_width = settings.SCREEN_WIDTH - 20
        bar_height = 20
        bar_x = 10
        bar_y = 10

        player = self.__world.player
        experience_percentage = player.experience / player.experience_to_next_level

        bg_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
        pygame.draw.rect(self.__screen, (100, 100, 100), bg_rect)

        exp_width = int(bar_width * experience_percentage)
        exp_rect = pygame.Rect(bar_x, bar_y, exp_width, bar_height)
        pygame.draw.rect(self.__screen, (255, 255, 0), exp_rect)

        font = pygame.font.SysFont(None, 24)
        exp_text = font.render(
            f"{player.experience}/{player.experience_to_next_level} XP",
            True,
            (0, 0, 0)
        )
        text_rect = exp_text.get_rect(center=(settings.SCREEN_WIDTH // 2, bar_y + bar_height // 2))
        self.__screen.blit(exp_text, text_rect)


    def __draw_player(self):
        adjusted_rect = self.camera.apply(self.__world.player.sprite.rect)
        self.__screen.blit(self.__world.player.sprite.image, adjusted_rect)

        self.__draw_player_health_bar()

    def load_world(self, world: GameWorld):
        self.__world = world

    def __draw_mouse_position(self):
        camera_rect = self.camera.camera_rect

        font = pygame.font.SysFont(None, 36)

        position_text = f"camera_rect: ({camera_rect})"
        text_surface = font.render(position_text, True, (255, 255, 255))

        self.__screen.blit(text_surface, (10, 100))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        font = pygame.font.SysFont(None, 36)

        position_text = f"Mouse Position: ({mouse_x + camera_rect[0]}, {mouse_y+camera_rect[1]})"
        text_surface = font.render(position_text, True, (255, 255, 255))

        self.__screen.blit(text_surface, (10, 50))

    def __draw_time(self):
        self.__frames = self.__frames + 1
        if self.__frames == 30:
            self.__seconds = self.__seconds + 1
            self.__frames = 0
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes = self.__minutes + 1
        # Define the font and size
        font = pygame.font.SysFont(None, 36)

        # Render the text for mouse position
        position_text = f"{self.__minutes:02}:{self.__seconds:02}"
        text_surface = font.render(position_text, True, (255, 255, 255))

        # Draw the text on the screen at a fixed position
        self.__screen.blit(text_surface, (300, 10))

    def __draw_monster_health_bar(self, monster):
        # Define the health bar dimensions
        bar_width = settings.TILE_WIDTH
        bar_height = 5
        bar_x = monster.sprite.rect.centerx - bar_width // 2 - self.camera.camera_rect.left
        bar_y = monster.sprite.rect.bottom + 5 - self.camera.camera_rect.top

        # Draw the background bar (red)
        bg_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
        pygame.draw.rect(self.__screen, (255, 0, 0), bg_rect)

        # Draw the health bar (green)
        health_percentage = monster.health / monster._stats.max_health

        health_width = int(bar_width * health_percentage)
        health_rect = pygame.Rect(bar_x, bar_y, health_width, bar_height)
        pygame.draw.rect(self.__screen, (0, 255, 0), health_rect)

    def render_frame(self):
        """Renders frames"""
        # Update the camera to follow the player
        self.camera.update(self.__world.player.sprite.rect)

        # Render the ground tiles
        self.__render_ground_tiles()

        # Draw all the experience gems
        for gem in self.__world.experience_gems:
            if self.camera.camera_rect.colliderect(gem.sprite.rect):
                adjusted_rect = self.camera.apply(gem.sprite.rect)
                self.__screen.blit(gem.sprite.image, adjusted_rect)

        # Draw all monsters
        for monster in self.__world.monsters:
            if self.camera.camera_rect.colliderect(monster.sprite.rect):
                adjusted_rect = self.camera.apply(monster.sprite.rect)
                self.__screen.blit(monster.sprite.image, adjusted_rect)
                self.__draw_monster_health_bar(monster)

        # Draw the bullets
        for bullet in self.__world.bullets:
            if self.camera.camera_rect.colliderect(bullet.sprite.rect):
                adjusted_rect = self.camera.apply(bullet.sprite.rect)
                self.__screen.blit(bullet.sprite.image, adjusted_rect)

        self.__draw_player()
        #self.__draw_mouse_position()
        self.__draw_time()
        self.render_inventory()
        self.__draw_experience_bar()

        if self.__world.paused and not self.__world.upgrading:

            self.render_pause_menu()

        if self.__world.upgrading:
            if len(self.__world.random_weapons_to_choose) == 0:
                self.__world.add_random_items()

            self.render_upgrade_menu(self.__world.random_weapons_to_choose)

        else:
            self.__world.restore_random_weapons()

        pygame.display.flip()


    def render_inventory(self):
        """Renders item inventory"""
        # Fetch the list of player's weapons and perks
        list_of_weapons = self.__world.player.get_player_weapons()
        list_of_perks = self.__world.player.get_player_perks()

        # Set image size and layout parameters
        image_size = 40  # Size of each image
        padding = 10     # Space between images
        columns = 8      # Number of images per row
        x_start, y_start = 10, 70  # Starting position for the weapons grid

        # Render each weapon image in a row/grid format
        for index, weapon_dop in enumerate(list_of_weapons):
            bullet = weapon_dop.bullet_name
            bullet_image_path = f"./assets/bullets/{bullet}.png"

            # Load and resize bullet image
            try:
                bullet_image = pygame.image.load(bullet_image_path)
                bullet_image = pygame.transform.scale(bullet_image, (image_size, image_size))
            except pygame.error: #pylint: disable=no-member
                bullet_image = None  # Handle missing images gracefully

            # Calculate grid position
            col = index % columns
            row = index // columns
            x = x_start + col * (image_size + padding)
            y = y_start + row * (image_size + padding)

            # Blit bullet image if available
            if bullet_image:
                self.__screen.blit(bullet_image, (x, y))

        # Calculate starting y position for perks grid below weapons
        y_start_perks = y_start + ((len(list_of_weapons) + columns - 1)
                                    // columns) * (image_size + padding) + 20

        # Render each perk image in a row/grid format
        for index, perk in enumerate(list_of_perks):
            perk_image_path = f"./assets/perks/{perk.item_name}.png"

            # Load and resize perk image
            try:
                perk_image = pygame.image.load(perk_image_path)
                perk_image = pygame.transform.scale(perk_image, (image_size, image_size))
            except pygame.error: #pylint: disable=no-member
                perk_image = None  # Handle missing images gracefully

            # Calculate grid position
            col = index % columns
            row = index // columns
            x = x_start + col * (image_size + padding)
            y = y_start_perks + row * (image_size + padding)

            # Blit perk image if available
            if perk_image:
                self.__screen.blit(perk_image, (x, y))


    def render_pause_menu(self):
        """Renders the pause menu"""
        menu_width = settings.SCREEN_WIDTH
        menu_height = settings.SCREEN_HEIGHT
        menu_alpha_value = 128
        menu_colour = settings.BG_COLOR
        menu_screen = MenuScreen(menu_width,
                                 menu_height,
                                 menu_alpha_value,
                                 menu_colour,
                                 self.__screen)
        title = "Menu de Pausa"
        screen_offset = 10
        start_x, start_y = 0,0
        menu_screen.draw(start_x,start_y)
        menu_screen.add_text(title,screen_offset)

        quit_button_width = settings.SCREEN_WIDTH
        quit_button_height = 100
        quit_button_colour = settings.BG_COLOR

        text_colour = settings.WHITE_COLOUR
        quit_button = Button(quit_button_width,
                             quit_button_height,
                             quit_button_colour,
                             self.__screen)
        quit_button.add_text("SALIR DEL JUEGO!", 50,text_colour)
        quit_button.draw(0,100)

        resume_button_width = settings.SCREEN_WIDTH
        resume_button_height = 100
        resume_button_colour = settings.BG_COLOR
        text_colour = settings.WHITE_COLOUR

        resume_button = Button(resume_button_width,
                               resume_button_height,
                               resume_button_colour,
                               self.__screen)
        resume_button.add_text("DESPAUSAR JUEGO (o apretar tecla p)!", 50,text_colour)
        resume_button.draw(0,300)

        if quit_button.is_clicked():
            quit()

        if resume_button.is_clicked():
            self.__world.change_paused_state()

    def render_upgrade_menu(self, items:["Weapon"]):
        """Renders upgrade menu"""
        click_counter = 0
        menu_width = settings.SCREEN_WIDTH
        menu_height = settings.SCREEN_HEIGHT
        menu_alpha_value = 128
        menu_colour = settings.BG_COLOR
        menu_screen = MenuScreen(menu_width,
                                 menu_height,
                                 menu_alpha_value,
                                 menu_colour,
                                 self.__screen)
        title = "Elegí tu mejora amigo!"
        screen_offset = 10
        start_x, start_y = 0,0
        menu_screen.draw(start_x,start_y)
        menu_screen.add_text(title,screen_offset)

        list_of_buttons = []
        button_offset = 0
        for item in items:
            item_level = 0
            if self.__world.player.has_item(item.item_name):
                item_level = self.__world.player.get_item_level(item.item_name)

            item_upgrade_detail = item.get_upgrade_info_by_level(item_level)
            button_offset +=150
            item_button_width = settings.SCREEN_WIDTH
            item_button_height = 100
            item_button_colour = settings.BG_COLOR
            item_colour = settings.WHITE_COLOUR
            item_button = Button(item_button_width,
                                item_button_height,
                                item_button_colour,
                                self.__screen)
            item_button.add_text(item.item_name, 20,item_colour)

            text_item_level = str(f"Level: {item_level}")
            item_button.add_text(text_item_level , 70,item_colour)

            text_item_upgrade_detail = str(f"DESCRIPCIÓN:{item_upgrade_detail}")

            item_button.add_text(text_item_upgrade_detail , 90,item_colour)

            item_button.draw(0,100 + button_offset)
            item_button.set_name(item.item_name)
            list_of_buttons.append(item_button)

        for button in list_of_buttons:
            if button.is_clicked() and click_counter == 0:
                click_counter += 1
                if self.__world.player.has_item(button.text):
                    self.__world.set_paused_state(False)
                    self.__world.set_upgrading_state(False)
                    self.__world.player.set_upgrading(False)
                    self.__world.player.upgrade_item_next_level(button.text)
                    break
                else:
                    self.__world.player.add_item(button.text)
                    self.__world.set_upgrading_state(False)
                    self.__world.set_paused_state(False)
