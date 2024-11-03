"""Module of the interfaces of the GUI"""

from abc import ABC, abstractmethod

class Clickable(ABC):
    """Clickable interface of the GUI"""

    @abstractmethod
    def is_clicked(self):
        """Click on the current clickable"""

class Drawable(ABC):
    """Drawable interface of the GUI"""

    @abstractmethod
    def draw(self, start_x:int, start_y:int):
        """Adds texto to the component

        Args:
            text (str): Text to add
            screen_offset_y (int): Offset Value for the height 
        """


    @abstractmethod
    def add_text(self, text: str, height_offset: int):
        """Adds texto to the component

        Args:
            text (str): Text to add
            height_offset (int): Offset Value for the height 
        """
