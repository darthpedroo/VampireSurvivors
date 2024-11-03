"""Module of the perk handler"""

from business.exceptions import ItemOverflow
from business.entities.item_handler import ItemHandler
from business.perks.perk_factory import PerkFactory
from business.stats.stats import  PlayerStats


class PerksHandler(ItemHandler):
    """Represents the perks handler
    
    Args:
        player_stats: The stats of the player.
        list_of_items (list): The list of item the player has.
        max_items (int): The maximum amount of items the player can have.
    """
    def __init__(self, player_stats, list_of_items=[], max_items=5):
        super().__init__(list_of_items, max_items)

        self.load_perks(player_stats)

    def add_item(self, perk_name: str, player_stats):
        """Adds perk to the list of perks.
        
        Args:
            perk_name (str): The name of the perk.
            player_stats: The stats of the player.
        """
        if len(self._list_of_items) <=self.max_items:
            perk_factory = PerkFactory()
            perk = perk_factory.create_perk(perk_name)
            self._list_of_items.append(perk)
            perk.use()
        else:
            raise ItemOverflow()

    def apply_perk_to_player_stats(self, perk_name: str, player_stats: PlayerStats):
        """Applies the perk to the player stats
        
        Args:
            perk_name (str): The name of the perk
            player_stats (PlayerStats): The stats of the player
        """
        for perk in self._list_of_items:
            if perk.item_name == perk_name: #pylint: disable=no-member
                perk.apply_perk_boosts_to_player(player_stats) #pylint: disable=no-member

    def load_perks(self, player_stats):
        """Loads the perks of the player
        
        Args:
            player_stats (PlayerStats): The stats of the player
        """
        for perk in self._list_of_items:
            perk.use(player_stats) #pylint: disable=no-member
