from abc import ABC

class Clickable(ABC):
    
    @abstractmethod
    def click(self):
        """Click on the current clickable"""
        pass
    
    