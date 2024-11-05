"""Module of the perks of the game."""

from business.entities.interfaces import UpgradableItem, IHasSprite
from business.stats.stats import PerkStats,PlayerStats
from presentation.sprite import Sprite


class Perk(UpgradableItem):
    """Represents a perk.
    
    Args:
        item_name: The name of the perk.
        max_level: The maximum level of the perk.
        upgrades (list[dict]): The list of the upgrades of the perk.
        perk_stats (PlayerStats): The stats of the perk.
        asset: The asset of the perk.
    """
    def __init__(self, item_name, max_level, upgrades: list[dict], perk_stats: PlayerStats, asset:str,level=1):
        super().__init__(item_name, max_level)
        self._level = level
        self._upgrades = upgrades
        self.item_stats = perk_stats
        self.sprite = asset
        
        self.load_upgrades(self._upgrades,self._level,self.item_stats)
        
    
    def create_perk_json_data(self):
        perk_data = {"item_name": self.item_name, "upgrades": self._upgrades, "level": self._level, "perk_stats": self.item_stats.create_player_stats_json_data()}
        return perk_data
    
    def get_sprite(self):
        return self.sprite
    
    def use(self):
        """Upgrades the perk."""
        self.upgrade_level(self._level, self._upgrades, self.item_stats)

    def apply_perk_boosts_to_player(self,player_stats:PlayerStats):
        """Applies the boosts of the perk to the player.
        
        Args:
            player_stats (PlayerStats): The stats of the player.
        """
        self.upgrade_level(self._level, self._upgrades, player_stats)
