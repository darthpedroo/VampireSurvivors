import json
from persistence.gems.gems_dao import GemsDao
from business.entities.experience_gem import ExperienceGem

class GemsJson(GemsDao):
    """Dao for the Gems

    Args:
        GemsDao (ABC): Abstract Gem Dao
    """
    
    def __init__(self, json_path: str):
        self.__json_path = json_path
        
    def get_gems(self):
        with open(self.__json_path, "r") as outfile:
            json_data = json.load(outfile)
            return json_data
        
    def save_gems(self, gems:[ExperienceGem]):
        
        list_of_gems_data = []
        
        for gem in gems:
            json_data = gem.create_experience_gem_json_data()
            list_of_gems_data.append(json_data)
        
        with open(self.__json_path, "w") as outfile:
            json.dump(list_of_gems_data, outfile, indent=4)
    
    def delete_gems(self):
        try:
            with open(self.__json_path, "w") as outfile:
                pass 
        except Exception as ex:
            print(ex)