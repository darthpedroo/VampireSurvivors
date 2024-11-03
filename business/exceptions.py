"""Module that contains custom exceptions."""


class DeadPlayerException(Exception):
    """Exception raised when the player dies."""

class ItemOverflow(Exception):
    """Exception raised when you try to add an Item to ItemHandler but it is full"""