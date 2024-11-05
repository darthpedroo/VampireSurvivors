import json
from persistence.clock.clock_dao import ClockDao
from business.clock.clock import ClockSingleton

class ClockJson(ClockDao):
    
    def __init__(self, json_path:str):
        self.__json_path = json_path
    
    def get_clock(self):
        with open(self.__json_path, "r") as outfile:
            json_data = json.load(outfile)
            return json_data
    
    def save_clock(self, clock:ClockSingleton):
        json_data = clock.create_clock_json_data()
        with open(self.__json_path , "w") as outfile:
            json.dump(json_data, outfile, indent=4)
    