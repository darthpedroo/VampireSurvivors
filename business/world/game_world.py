"""This module contains the implementation of the game world."""

import random
import pygame

from business.entities.interfaces import IBullet, IExperienceGem, IMonster, IPlayer
from business.world.interfaces import IGameWorld, IMonsterSpawner, ITileMap
from business.weapons.weapon_factory import WeaponFactory
from json import JSONDecodeError
from business.perks.perk_factory import PerkFactory
from business.clock.clock import ClockSingleton
from persistence.clock.clock_json import ClockJson

class GameWorld(IGameWorld):
    """Represents the game world."""

    def __init__(self, spawner: IMonsterSpawner, tile_map: ITileMap, player: IPlayer, display: "Display"): #pylint: disable=line-too-long
        # Initialize the player and lists for monsters, bullets and gems
        self.__player: IPlayer = player
        self.__monsters: list[IMonster] = []
        self.__bullets: list[IBullet] = []
        self.__experience_gems: list[IExperienceGem] = []
        self.__clock = self.__initialize_clock()
        self.tile_map: ITileMap = tile_map
        self.__monster_spawner: IMonsterSpawner = spawner
        self.__display = display
        self._paused = False
        self._upgrading = False
        self.random_weapons_to_choose = []


        self.__list_of_items = [
                                {"weapon": "Toilet_spinner"}]
    

    def __initialize_clock(self):
        try:
            clock_json_path = "./data/clock.json"
            clock_json = ClockJson(clock_json_path)
            ms = clock_json.get_clock()
            ClockSingleton(ms).set_ms(ms["ms"])
        except JSONDecodeError:
            ms = 0
        return ClockSingleton(ms)
    
    def load_monster_spawner_json(self):
        self.__monster_spawner.load_monsters(self)
        
    
    def add_random_items(self):
        items = self.__list_of_items.copy()
        count = 0  # Track the number of items added

        while count < 3 and items:
            rnd_weapon = random.choice(items)

            # Check if the randomly chosen item has not reached max level
            if not self.__player.item_reached_max_level(next(iter(rnd_weapon.values()))):

                # Create the item based on its type and add to list
                if rnd_weapon.get("weapon") is not None:
                    chosen_item = WeaponFactory().create_weapon(rnd_weapon["weapon"])
                else:
                    chosen_item = PerkFactory().create_perk(rnd_weapon["perk"])

                self.random_weapons_to_choose.append(chosen_item)
                count += 1  # Increment the count of items added

            # Remove the chosen item from the list to avoid duplicates
            items.remove(rnd_weapon)

        if count < 3:
            print("No more ammo for you, little vater")


    def restore_random_weapons(self):
        self.random_weapons_to_choose = []

    def update_player(self, x_mov: int, y_mov: int):
        if not self._paused:
            current_state = self.__player.current_state
            self.__player.update(self, current_state)
            self.__player.set_direction(x_mov, y_mov)

    def change_player_state(self, new_state):
        """Changes the state of the player
        Args:
            new_state (_type_): _description_
        """
        self.__player.switch_state(new_state)

    def change_paused_state(self):
        if self._paused:
            self._paused = False
            self.__clock.set_paused(False)
        else:
            self._paused = True
            self.__clock.set_paused(True)

    def set_upgrading_state(self, state: bool):
        self._upgrading = state
        self.__clock.set_paused(state)

    def set_paused_state(self, state: bool):
        self._paused = state

    def get_mouse_position(self):
        mouse_pos = pygame.mouse.get_pos()
        return mouse_pos

    def get_camera(self):
        return self.__display.camera

    def update(self):
        if not self._paused:
            self.player.update(self, self.player.current_state)
            for monster in self.monsters:
                monster.update(self)
            for bullet in self.__bullets:
                bullet.update(self)
            
            camera = self.__display.camera
            self.__monster_spawner.update(self,camera)

    def add_monster(self, monster: IMonster):
        self.__monsters.append(monster)

    def remove_monster(self, monster: IMonster):
        self.__monsters.remove(monster)

    def add_experience_gem(self, gem: IExperienceGem):
        self.__experience_gems.append(gem)

    def remove_experience_gem(self, gem: IExperienceGem):
        self.__experience_gems.remove(gem)

    def add_bullet(self, bullet: IBullet):
        self.__bullets.append(bullet)

    def remove_bullet(self, bullet: IBullet):
        try:
            self.__bullets.remove(bullet)
        except ValueError:
            print("No hay bullets :v")

    @property
    def player(self) -> IPlayer:
        return self.__player

    @property
    def monsters(self) -> list[IMonster]:
        return self.__monsters[:]

    @property
    def bullets(self) -> list[IBullet]:
        return self.__bullets[:]

    @property
    def experience_gems(self) -> list[IExperienceGem]:
        return self.__experience_gems[:]

    @property
    def paused(self) -> bool:
        return self._paused

    @property
    def upgrading(self) -> bool:
        return self._upgrading

    @property
    def clock(self):
        return self.__clock