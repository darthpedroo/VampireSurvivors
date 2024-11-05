"""Module for player's persistence on a JSON"""
import json
from persistence.player.player_dao import PlayerDao
from business.entities.player import Player


class PlayerJson(PlayerDao):
    """Handles player persistence on a JSON file."""

    def __init__(self, json_path: str):
        """
        Initializes the PlayerJson instance with the path to the JSON file.

        Args:
            json_path (str): The path to the JSON file where the player data will be stored.
        """
        self.__json_path = json_path

    def save_player(self, player: Player) -> None:
        """
        Saves the provided player data to the JSON file.

        Args:
            player (Player): The player instance to save.

        Returns:
            None

        Raises:
            Exception: If an error occurs while writing to the JSON file.
        """
        json_data = player.create_player_json_data()
        with open(self.__json_path, "w") as outfile:
            json.dump(json_data, outfile, indent=4)
    
    def delete_player(self) -> None:
        """
        Deletes the player data from the JSON file by clearing its contents.

        Returns:
            None

        Raises:
            Exception: If an error occurs while trying to write to the JSON file.
        """
        try:
            with open(self.__json_path, "w") as outfile:
                pass 
        except Exception as ex:
            print(f"An error occurred while deleting player data: {ex}")

    def get_player_attribute_from_paramater(self, player_attribute: str):
        """
        Retrieves a specific attribute from the player data.

        Args:
            player_attribute (str): The attribute key to retrieve from the player data.

        Returns:
            Any: The value of the specified attribute from the player data.

        Raises:
            KeyError: If the specified attribute is not found.
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        player_data = self.get_player()
        return player_data[player_attribute]
    
    def get_player_stats_from_parameter(self, stat: str):
        """
        Retrieves a specific stat from the player's stats.

        Args:
            stat (str): The stat key to retrieve from the player's stats.

        Returns:
            Any: The value of the specified stat, or None if the stat is not found.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        with open(self.__json_path, "r") as outfile:
            try:            
                player_data = json.load(outfile)
                return player_data["player_stats"][stat]
            except TypeError:
                return None

    def get_perks_handler(self) -> list:
        """
        Retrieves the player's list of perks from the perks handler.

        Returns:
            list: A list of items in the player's perks handler.

        Raises:
            KeyError: If the perks handler is not found in the player data.
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        return self.get_player_attribute_from_paramater("perks_handler")["list_of_items"]

    def get_weapon_handler(self) -> list:
        """
        Retrieves the player's list of weapons from the weapon handler.

        Returns:
            list: A list of items in the player's weapon handler.

        Raises:
            KeyError: If the weapon handler is not found in the player data.
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        return self.get_player_attribute_from_paramater("weapon_handler")["list_of_items"]
        
    def get_player(self) -> dict:
        """
        Retrieves the full player data from the JSON file.

        Returns:
            dict: The full player data.

        Raises:
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        with open(self.__json_path, "r") as outfile:
            player_data = json.load(outfile)
            return player_data
    
    def get_player_pos(self) -> tuple:
        """
        Retrieves the player's position coordinates from the player data.

        Returns:
            tuple: A tuple containing the x and y coordinates (pos_x, pos_y) of the player.

        Raises:
            KeyError: If position coordinates are not found in the player data.
            FileNotFoundError: If the JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        with open(self.__json_path, "r") as outfile:
            player_data = json.load(outfile)
            pos_x = player_data["pos_x"]
            pos_y = player_data["pos_y"]
            return pos_x, pos_y
