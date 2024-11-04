from persistence.monsters.monster_dao import MonsterDao

class MonsterJson(MonsterDao):
    
    def __init__(self, json_path: str):
        self.__json_path = json_path
        
    
    def get_player(self):
        return super().get_player()
    
    def save_player(self):
        return super().save_player()