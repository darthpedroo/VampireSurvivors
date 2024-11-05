"""Module for monster's persistence on a JSON"""
import json
from persistence.monsters.monster_dao import MonsterDao
from business.entities.interfaces import IMonster

class MonsterJson(MonsterDao):
    """Handles monster persistence on a JSON file"""

    def __init__(self, json_path: str):
        """
        Initializes the MonsterJson instance with the path to the JSON file.

        Args:
            json_path (str): The path to the JSON file where monsters will be stored.
        """
        self.__json_path = json_path

    def get_monsters(self) -> list:
        """
        Retrieves a list of monsters from the JSON file.

        Returns:
            list: A list of monsters loaded from the JSON file.

        Raises:
            FileNotFoundError: If the specified JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        with open(self.__json_path, "r") as outfile:
            json_data = json.load(outfile)
            return json_data

    def save_monsters(self, monsters: list[IMonster]) -> None:
        """
        Saves the provided monsters to the JSON file.

        Args:
            monsters (list[IMonster]): A list of monsters to save.

        Returns:
            None

        Raises:
            Exception: If an error occurs while writing to the JSON file.
        """
        list_of_monsters_data = []
        
        for monster in monsters:
            json_data = monster.create_monster_json_data()
            list_of_monsters_data.append(json_data)
        
        with open(self.__json_path, "w") as outfile:
            json.dump(list_of_monsters_data, outfile, indent=4)

    def delete_monsters(self) -> None:
        """
        Deletes all monsters from the JSON file by clearing its contents.

        Returns:
            None

        Raises:
            Exception: If an error occurs while trying to write to the JSON file.
        """
        try:
            with open(self.__json_path, "w") as outfile:
                pass 
        except Exception as ex:
            print(f"An error occurred while deleting monsters: {ex}")
