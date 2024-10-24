from business.entities.interfaces import IUpgradable

class UpgradableWeapon(IUpgradable):
    def __init__(self):
        self._level = 0
        self._upgrades = []
        self.load_upgrades()

    def load_upgrades(self):
        for level in range(self._level):
            self.upgrade_level(level)

    def upgrade_level(self, level: int):
        current_upgrade = self._upgrades[level]
        attribute_to_modify = current_upgrade.get('ATTRIBUTE')
        new_value = current_upgrade.get('VALUE')
        if current_upgrade.get('OPERATION') == 'MULTIPLICATION':
            new_value = getattr(self, attribute_to_modify) * new_value
            setattr(self, attribute_to_modify, new_value)

    def upgrade_next_level(self):
        self._level += 1
        self.upgrade_level(self._level)
