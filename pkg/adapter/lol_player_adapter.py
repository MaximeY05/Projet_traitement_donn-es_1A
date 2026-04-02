from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.player import Player


class LolPlayerAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Player:
        """
        Convertit une ligne de player.csv en objet Player.
        """
        return Player(
            pseudo=row["pseudo"],
            name=row["name"],
            country_birth=row["country_of_birth"],
            birthdate=row["birthdate"],
            role=row["role"],
            team=row["team"]
        )

    def to_row(self, player: Player) -> Dict[str, str]:
        """
        Convertit un objet Player en dictionnaire pour le CSV.
        """
        return {
            "pseudo": player.pseudo,
            "name": player.name,
            "country_of_birth": player.country_birth,
            "birthdate": player.birthdate,
            "role": player.role,
            "team": player.team
        }
