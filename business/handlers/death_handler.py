"""Module that contains the DeathHandler class."""

import settings
from business.entities.experience_gem import ExperienceGem
from business.exceptions import DeadPlayerException
from business.world.interfaces import IGameWorld


class DeathHandler:
    """Class that handles entity deaths."""

    @staticmethod
    def __is_entity_within_world_boundaries(entity):
        return (
            30 <= entity.pos_x <= (settings.WORLD_WIDTH - 30) and 30 <= entity.pos_y <= (settings.WORLD_HEIGHT - 30)
        )

    @staticmethod
    def check_deaths(world: IGameWorld):
        player = world.player
        """Check if any entities have died and remove them from the game world.

        Args:
            world (IGameWorld): The game world to check for dead entities.
        """
        for bullet in world.bullets:
            if bullet.health <= 0:
                world.remove_bullet(bullet)
            if not DeathHandler.__is_entity_within_world_boundaries(bullet):
                world.remove_bullet(bullet)
        


        for monster in world.monsters:
            if monster.health <=0:
                world.remove_monster(monster)
                
                gem = monster.drop_loot(player.luck)
                if gem is not None:
                    world.add_experience_gem(gem)
            

        if player.health <= 0:
            raise DeadPlayerException

        if not DeathHandler.__is_entity_within_world_boundaries(player):
            player.pos_x = max(30, min(player.pos_x, settings.WORLD_WIDTH - 30))
            player.pos_y = max(30, min(player.pos_y, settings.WORLD_HEIGHT - 30))
            