import json
from persistence.player.player_dao import PlayerDao
from business.entities.player import Player


class PlayerJson(PlayerDao):
    
    def __init__(self, json_path: str):
        self.__json_path = json_path

    def save_player(self, player:Player):
        json_data = player.create_player_json_data()
        with open(self.__json_path , "w") as outfile:
            json.dump(json_data, outfile, indent=4)
    
    def get_player_attribute_from_paramater(self, player_attribute:str):
        player_data = self.get_player()
        return player_data[player_attribute]
    
    def get_player_stats_from_parameter(self, stat:str):
        with open(self.__json_path, "r") as outfile:
            try:            
                player_data = json.load(outfile)
                return player_data["player_stats"][stat]
            except TypeError:
                return None

    def get_perks_handler(self):
        return self.get_player_attribute_from_paramater("perks_handler")["list_of_items"]

    def get_weapon_handler(self):
        return self.get_player_attribute_from_paramater("weapon_handler")["list_of_items"]
        
    def get_player(self):
        with open(self.__json_path, "r") as outfile:
            player_data = json.load(outfile)
            return player_data
    
    def get_player_pos(self):
        with open(self.__json_path, "r") as outfile:
            player_data = json.load(outfile)
            pos_x = player_data["pos_x"]
            pos_y = player_data["pos_y"]
            return pos_x,pos_y
    
    
        