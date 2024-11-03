from business.exceptions import ItemOverflow
from business.perks.perk import Perk
from business.entities.item_handler import ItemHandler
from business.perks.perk_factory import PerkFactory
from business.stats.stats import  PlayerStats


class PerksHandler(ItemHandler):
    
    def __init__(self, player_stats, list_of_items=[], max_items=5):
        super().__init__(list_of_items, max_items)
        
        self.load_perks(player_stats)
    
    def add_item(self, perk_name: str,player_stats):
        if len(self._list_of_items) <=self.max_items:
            perk_factory = PerkFactory()
            perk = perk_factory.create_perk(perk_name)
            self._list_of_items.append(perk)
            perk.use()
        else:
            raise ItemOverflow()

    def apply_perk_to_player_stats(self, perk_name: str, player_stats:PlayerStats):
        for perk in self._list_of_items:
            if perk.item_name == perk_name:
                perk.apply_perk_boosts_to_player(player_stats)

    def load_perks(self, player_stats):
        for perk in self._list_of_items:
            perk.use(player_stats)