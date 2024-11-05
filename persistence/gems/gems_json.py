import json
from persistence.gems.gems_dao import GemsDao
from business.entities.experience_gem import ExperienceGem

class GemsJson(GemsDao):
    """Dao for the Gems

    Args:
        GemsDao (ABC): Abstract Gem Dao
    """
    
    def __init__(self, json_path: str):
        """
        Initializes the GemsJson instance with the path to the JSON file.

        Args:
            json_path (str): The path to the JSON file where the gems will be stored.
        """
        self.__json_path = json_path
        
    def get_gems(self) -> list:
        """
        Retrieves a list of gems from the JSON file.

        Returns:
            list: A list of gems loaded from the JSON file.

        Raises:
            FileNotFoundError: If the specified JSON file does not exist.
            json.JSONDecodeError: If the JSON data is invalid.
        """
        with open(self.__json_path, "r") as outfile:
            json_data = json.load(outfile)
            return json_data

    def save_gems(self, gems: list[ExperienceGem]) -> None:
        """
        Saves the provided gems to the JSON file.

        Args:
            gems (list[ExperienceGem]): A list of gems to save.

        Returns:
            None

        Raises:
            Exception: If an error occurs while writing to the JSON file.
        """
        list_of_gems_data = []

        for gem in gems:
            json_data = gem.create_experience_gem_json_data()
            list_of_gems_data.append(json_data)

        with open(self.__json_path, "w") as outfile:
            json.dump(list_of_gems_data, outfile, indent=4)

    def delete_gems(self) -> None:
        """
        Deletes all gems from the JSON file by clearing its contents.

        Returns:
            None

        Raises:
            Exception: If an error occurs while trying to write to the JSON file.
        """
        try:
            with open(self.__json_path, "w") as outfile:
                pass
        except Exception as ex:
            print(f"An error occurred while deleting gems: {ex}")
