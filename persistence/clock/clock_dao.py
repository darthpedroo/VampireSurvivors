import json
from abc import ABC
from business.clock.clock import ClockSingleton

class ClockDao(ABC):
    


    def get_clock(self):
        pass
    
    def save_clock(self, clock:ClockSingleton):
        pass    

    