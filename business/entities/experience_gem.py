"""Module for the ExperienceGem class."""

from business.entities.state_machine.entity import Entity
from business.entities.interfaces import IExperienceGem
from presentation.sprite import ExperienceGemSprite


class ExperienceGem(Entity, IExperienceGem):
    """Represents an experience gem in the game world."""

    def __init__(self, pos_x: float, pos_y: float, amount: int):
        super().__init__(pos_x, pos_y, ExperienceGemSprite(pos_x, pos_y))
        self._logger.debug("Created %s", self)
        self.__amount = amount

    def create_experience_gem_json_data(self):
        experience_gem = {"pos_x": self.pos_x, "pos_y": self.pos_y, "amount": self.amount}
        return experience_gem
    
    @property
    def amount(self) -> int:
        return self.__amount

    def __str__(self):
        return f"ExperienceGem(amount={self.amount}, pos=({self.pos_x}, {self.pos_y}))"
