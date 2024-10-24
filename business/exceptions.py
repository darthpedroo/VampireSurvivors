"""Module that contains custom exceptions."""


class DeadPlayerException(Exception):
    """Exception raised when the player dies."""

class WeaponOverflow(Exception):
    """Exception raised when you try to add a weapon to the WeaponHandler but it is full"""