from scripts.clan import OtherClan
from scripts.game_structure import game

def get_other_clan(clan_name):
    """
    returns the clan object of given clan name
    """
    for clan in game.clan.all_other_clans:
        if clan.name == clan_name:
            return clan


def change_clan_relations(other_clan: OtherClan, difference, clan = None):
    """
    will change the Clan's relation with other clans according to the difference parameter.
    """
    # CGWAR EDITED
    if not clan:
        clan = game.clan

    other_clan.relations[clan.group_ID] += difference


def change_clan_reputation(difference):
    """
    will change the Clan's reputation with outsider cats according to the difference parameter.
    """
    game.clan.reputation += difference
