import math
from business.weapons.weapon import Weapon
from business.world.interfaces import IGameWorld
from business.entities.item_factory import ProjectileFactory


class ManualGun(Weapon):
    def __init__(self, bullet_name: str, bullet_cooldown: int, bullet_speed: int):
        self.__last_shot_time = 0
        self.__base_shoot_cooldown = bullet_cooldown
        self.__bullet_name = bullet_name
        self.__speed = bullet_speed

    def set_last_shot_time(self, new_time):
        self.__last_shot_time = new_time

    def is_cooldown_over(self, current_time):
        return current_time - self.__last_shot_time >= self.__base_shoot_cooldown

    def aim(self, world: IGameWorld, player_pos_x: int, player_pos_y: int):
        mouse_pos_x, mouse_pos_y = world.get_mouse_position()
        camera_x = world.get_camera().camera_rect[0]
        camera_y = world.get_camera().camera_rect[1]
        dir_x, dir_y = self.__calculate_direction(
            (mouse_pos_x + camera_x) - player_pos_x, (mouse_pos_y + camera_y) - player_pos_y)
        return dir_x, dir_y

    def __calculate_direction(self, dx, dy):
        distance = math.hypot(dx, dy)
        if distance != 0:
            return dx / distance, dy / distance
        return 0, 0

    def use(self, player_pos_x: int, player_pos_y: int, world: IGameWorld, current_time):
        projectile_factory = ProjectileFactory()
        bullet_direction_x, bullet_direction_y = self.aim(
            world, player_pos_x, player_pos_y)
        projectile = projectile_factory.create_item(
            self.__bullet_name, player_pos_x, player_pos_y, bullet_direction_x, bullet_direction_y, self.__speed, world)
        if self.is_cooldown_over(current_time):
            world.add_bullet(projectile)
            self.__last_shot_time = current_time

    def upgrade_next_level(self):
        pass
