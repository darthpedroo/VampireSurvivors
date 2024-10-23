from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self, bullet_name: str, bullet_speed: int):
        self.__last_shot_time = 0
        self.__base_shoot_cooldown = 100

    @abstractmethod
    def is_cooldown_over(self, current_time):
        pass

    @abstractmethod
    def use(self):
        """Uses the weapon, performs an attack.
        """
        pass

    @abstractmethod
    def aim(self):
        """Gets the direction where the weapon should aim
        """
        pass

    def load_weapon_data(self, weapon_dao):
        """Loads the data of the weapon

        Args:
            weapon_dao (_type_): _description_
        """
        pass
