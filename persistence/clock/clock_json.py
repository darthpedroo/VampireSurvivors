"""Module for clock's persistence on a JSON"""
import json
from persistence.clock.clock_dao import ClockDao
from business.clock.clock import ClockSingleton

class ClockJson(ClockDao):
    """Represents clock's persistence on a JSON"""

    def __init__(self, json_path: str):
        """
        Initializes the ClockJson instance with the path to the JSON file.

        Args:
            json_path (str): The path to the JSON file where the clock will be stored.
        """
        self.__json_path = json_path

    def get_clock(self) -> dict:
        """
        Retrieves the clock data from the JSON file.

        Returns:
            dict: The clock data loaded from the JSON file.

        Raises:
            FileNotFoundError: If the specified JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        with open(self.__json_path, "r") as outfile:
            json_data = json.load(outfile)
            return json_data

    def save_clock(self, clock: ClockSingleton) -> None:
        """
        Saves the provided clock data to the JSON file.

        Args:
            clock (ClockSingleton): The clock instance to save.

        Returns:
            None

        Raises:
            Exception: If an error occurs while writing to the JSON file.
        """
        json_data = clock.create_clock_json_data()
        with open(self.__json_path, "w") as outfile:
            json.dump(json_data, outfile, indent=4)

    def delete_clock(self) -> None:
        """
        Deletes the clock data from the JSON file by clearing its contents.

        Returns:
            None

        Raises:
            Exception: If an error occurs while trying to write to the JSON file.
        """
        try:
            with open(self.__json_path, "w") as outfile:
                pass 
        except Exception as ex:
            print(f"An error occurred while deleting the clock data: {ex}")
