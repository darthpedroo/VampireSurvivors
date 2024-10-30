from abc import ABC, abstractmethod

class Clickable(ABC):
    
    @abstractmethod
    def is_clicked(self):
        """Click on the current clickable"""
        pass
    

class Drawable(ABC):
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def add_text(self, text:str, screen_offset_y:int):
        """Adds texto to the component

        Args:
            text (str): Text to add
            screen_offset_y (int): Offset Value for the height 
        """
    
        pass