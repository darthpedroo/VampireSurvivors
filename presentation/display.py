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

        # Set the window title
        pygame.display.set_caption(settings.GAME_TITLE)

        # Initialize the camera
        self.camera = Camera()

        self.__ground_tileset = self.__load_ground_tileset()
        self.__world: GameWorld = None

    def __load_ground_tileset(self):
        return Tileset(
            "./assets/ground_tileset.png", settings.TILE_WIDTH, settings.TILE_HEIGHT, 2, 3
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
        # Get the player's health
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

    def __draw_player(self):
        adjusted_rect = self.camera.apply(self.__world.player.sprite.rect)
        self.__screen.blit(self.__world.player.sprite.image, adjusted_rect)

        self.__draw_player_health_bar()

        # Draw the experience text
        font = pygame.font.SysFont(None, 48)
        experience_text = font.render(
            f"XP: {self.__world.player.experience}/{self.__world.player.experience_to_next_level}",
            True,
            (255, 255, 255),
        )
        self.__screen.blit(experience_text, (10, 10))

    def load_world(self, world: GameWorld):
        self.__world = world
    
    def __draw_mouse_position(self):
        
        
        camera_rect = self.camera.camera_rect

        # Define the font and size
        font = pygame.font.SysFont(None, 36)

        # Render the text for mouse position
        position_text = f"camera_rect: ({camera_rect})"
        text_surface = font.render(position_text, True, (255, 255, 255))

        # Draw the text on the screen at a fixed position
        self.__screen.blit(text_surface, (10, 100))
        
        
        
        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Define the font and size
        font = pygame.font.SysFont(None, 36)

        # Render the text for mouse position
        position_text = f"Mouse Position: ({mouse_x + camera_rect[0]}, {mouse_y+camera_rect[1]})"
        text_surface = font.render(position_text, True, (255, 255, 255))

        # Draw the text on the screen at a fixed position
        self.__screen.blit(text_surface, (10, 50))

    def render_frame(self):
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

        # Draw the bullets
        for bullet in self.__world.bullets:
            if self.camera.camera_rect.colliderect(bullet.sprite.rect):
                adjusted_rect = self.camera.apply(bullet.sprite.rect)
                self.__screen.blit(bullet.sprite.image, adjusted_rect)

        # Draw the player
        self.__draw_player()
        self.__draw_mouse_position()
        
        if self.__world.paused and not self.__world.upgrading:
            
            self.render_pause_menu()

        if self.__world.upgrading:
            if len(self.__world._random_weapons_to_choose) == 0:
                self.__world.add_random_weapons()

            self.render_upgrade_menu(self.__world._random_weapons_to_choose)
        
        else:
            self.__world.restore_random_weapons()

        pygame.display.flip()

    
        
        
    def render_pause_menu(self):
        menu_width = settings.SCREEN_WIDTH
        menu_height = settings.SCREEN_HEIGHT
        menu_alpha_value = 128
        menu_colour = settings.BG_COLOR
        menu_screen = MenuScreen(menu_width,menu_height, menu_alpha_value, menu_colour, self.__screen)
        title = "Menu de Pausa"
        screen_offset = 10
        start_x, start_y = 0,0
        menu_screen.draw(start_x,start_y)
        menu_screen.add_text(title,screen_offset)
        
        quit_button_width = settings.SCREEN_WIDTH
        quit_button_height = 100
        quit_button_colour = settings.BG_COLOR
        
        text_colour = settings.WHITE_COLOUR
        quit_button = Button(quit_button_width, quit_button_height, quit_button_colour, self.__screen)
        quit_button.add_text("SALIR DEL JUEGO!", 50,text_colour)
        quit_button.draw(0,100)
        
        resume_button_width = settings.SCREEN_WIDTH
        resume_button_height = 100
        resume_button_colour = settings.BG_COLOR
        text_colour = settings.WHITE_COLOUR
        
        resume_button = Button(resume_button_width, resume_button_height, resume_button_colour, self.__screen)
        resume_button.add_text("DESPAUSAR JUEGO (o apretar tecla p)!", 50,text_colour)
        resume_button.draw(0,300)

        if quit_button.is_clicked():
            quit()
            
        if resume_button.is_clicked():
            self.__world.change_paused_state()

    
    def render_upgrade_menu(self, weapons:["Weapon"]):
        click_counter = 0
        menu_width = settings.SCREEN_WIDTH
        menu_height = settings.SCREEN_HEIGHT
        menu_alpha_value = 128
        menu_colour = settings.BG_COLOR
        menu_screen = MenuScreen(menu_width,menu_height, menu_alpha_value, menu_colour, self.__screen)
        title = "Elegí tu mejora amigo!"
        screen_offset = 10
        start_x, start_y = 0,0
        menu_screen.draw(start_x,start_y)
        menu_screen.add_text(title,screen_offset)
        
        list_of_buttons = []
        button_offset = 0
        for weapon in weapons:
            
            weapon_level = 0
            if self.__world.player.has_weapon(weapon.weapon_name):
                weapon_level = self.__world.player.get_weapon_level(weapon.weapon_name)            
            
            weapon_upgrade_detail = weapon.get_upgrade_info_by_level(weapon_level)
            button_offset +=150
            weapon_button_width = settings.SCREEN_WIDTH
            weapon_button_height = 100
            weapon_button_colour = settings.BG_COLOR
            weapon_colour = settings.WHITE_COLOUR
            weapon_button = Button(weapon_button_width, weapon_button_height, weapon_button_colour, self.__screen)
            weapon_button.add_text(weapon.weapon_name, 20,weapon_colour)
            
            text_weapon_level = str(f"Level: {weapon_level}")
            weapon_button.add_text(text_weapon_level , 70,weapon_colour)
            
            text_weapon_upgrade_detail = str(f"DESCRIPCIÓN:{weapon_upgrade_detail}")
            
            weapon_button.add_text(text_weapon_upgrade_detail , 90,weapon_colour)
            
            weapon_button.draw(0,100 + button_offset)
            weapon_button.set_name(weapon.weapon_name)
            list_of_buttons.append(weapon_button)
        
        for button in list_of_buttons:
            if button.is_clicked() and click_counter == 0:
                click_counter += 1
                if self.__world.player.has_weapon(button.text):
                    self.__world.set_paused_state(False)
                    self.__world.set_upgrading_state(False)
                    self.__world.player.set_upgrading(False)                
                    self.__world.player.upgrade_weapon_next_level(button.text)
                    break
                else:
                    self.__world.player.add_weapon(button.text, self.__world)
                