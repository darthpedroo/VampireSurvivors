"""Module of the perks of the game."""

from business.entities.interfaces import UpgradableItem
from business.stats.stats import PlayerStats

class Perk(UpgradableItem):
    """Represents a perk.
    
    Args:
        item_name: The name of the perk.
        max_level: The maximum level of the perk.
        upgrades (list[dict]): The list of the upgrades of the perk.
        perk_stats (PlayerStats): The stats of the perk.
        asset: The asset of the perk.
    """
    def __init__(self, item_name, max_level, upgrades: list[dict], perk_stats: PlayerStats, asset):
        super().__init__(item_name, max_level)
        self._upgrades = upgrades
        self.item_stats = perk_stats
        self.asset = asset

    def use(self):
        """Upgrades the perk."""
        self.upgrade_level(self._level, self.item_stats)

    def apply_perk_boosts_to_player(self,player_stats:PlayerStats):
        """Applies the boosts of the perk to the player.
        
        Args:
            player_stats (PlayerStats): The stats of the player.
        """
        self.upgrade_level(self._level, player_stats)
