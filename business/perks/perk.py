from abc import ABC
from business.entities.interfaces import UpgradableItem
from business.stats.stats import PerkStats, PlayerStats

class Perk(UpgradableItem):
    def __init__(self, item_name, max_level, upgrades: list[dict], perk_stats:PlayerStats, asset):
        super().__init__(item_name, max_level)
        self._upgrades = upgrades
        self.item_stats = perk_stats
        self.asset = asset
    
    def use(self):
        self.upgrade_level(self._level, self.item_stats)

    def apply_perk_boosts_to_player(self,player_stats:PlayerStats):
        self.upgrade_level(self._level, player_stats)

