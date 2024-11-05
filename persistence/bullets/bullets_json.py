"""Module for bullet's persistence on a JSON"""
import json
from persistence.bullets.bullets_dao import BulletDao
from business.entities.interfaces import IBullet

class BulletJson(BulletDao):
    """Represents bullet's persistence on a JSON"""

    def __init__(self, json_path: str):
        """
        Initializes the BulletJson instance with the path to the JSON file.

        Args:
            json_path (str): The path to the JSON file where bullets will be stored.
        """
        self.__json_path = json_path

    def get_bullets(self) -> list:
        """
        Retrieves a list of bullets from the JSON file.

        Returns:
            list: A list of bullets loaded from the JSON file.

        Raises:
            FileNotFoundError: If the specified JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        with open(self.__json_path, "r") as outfile:
            json_data = json.load(outfile)
            return json_data

    def save_bullets(self, bullets: list[IBullet]) -> None:
        """
        Saves the provided bullets to the JSON file.

        Args:
            bullets (list[IBullet]): A list of bullets to save.

        Returns:
            None

        Raises:
            UnboundLocalError: If there are no bullets to save (if bullets is empty).
            Exception: If an error occurs while writing to the JSON file.
        """
        list_of_bullets_data = []

        try:
            for bullet in bullets:           
                json_data = bullet.create_bullet_json_data()
                list_of_bullets_data.append(json_data)

            with open(self.__json_path, "w") as outfile:
                json.dump(list_of_bullets_data, outfile, indent=4)
        except UnboundLocalError:
            print("There are no Bullets to save!")
        except Exception as ex:
            print(f"An error occurred while saving bullets: {ex}")

    def delete_bullets(self) -> None:
        """
        Deletes all bullets from the JSON file by clearing its contents.

        Returns:
            None

        Raises:
            Exception: If an error occurs while trying to write to the JSON file.
        """
        try:
            with open(self.__json_path, "w") as outfile:
                pass 
        except Exception as ex:
            print(f"An error occurred while deleting bullets: {ex}")
