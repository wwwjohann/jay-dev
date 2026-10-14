from __future__ import annotations

from enum import Enum


class EventSubtype(Enum):
    war = "war"
    murder = "murder"
    old_age = "old_age"
    mass_death = "mass_death"
    murder_reveal = "murder_reveal"
    hidden_murder_reveal = "hidden_murder_reveal"
    failed_murder = "failed_murder"
    accessory = "accessory"
    ceremony = "ceremony"
    transition = "transition"
    mediator = "mediator"

    # CGWAR
    other_clan_birth_reaction = "other_clan_birth_reaction"
    other_clan_death_reaction = "other_clan_death_reaction"
