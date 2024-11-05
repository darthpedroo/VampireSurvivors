import json
from persistence.monsters.monster_dao import MonsterDao
from business.entities.interfaces import IMonster
class MonsterJson(MonsterDao):
    
    def __init__(self, json_path: str):
        self.__json_path = json_path
        
    
    def get_monsters(self):
        with open(self.__json_path, "r") as outfile:
            json_data = json.load(outfile)
            return json_data
    
    def save_monsters(self, monsters:[IMonster]):
        
        list_of_monsters_data = []
        
        for monster in monsters:
            json_data = monster.create_monster_json_data()
            list_of_monsters_data.append(json_data)
        
        with open(self.__json_path, "w") as outfile:
            json.dump(list_of_monsters_data, outfile, indent=4)
    
    def delete_monsters(self):
        try:
            with open(self.__json_path, "w") as outfile:
                pass 
        except Exception as ex:
            print(ex)