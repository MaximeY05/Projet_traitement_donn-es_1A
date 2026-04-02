from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.team import Team


class LolTeamAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Team:
        """
        Convertit une ligne de team.csv en objet Team.
        """
        return Team(
            name=row["team"],
            abbreviation=row["team_abbreviation"],
            location=row["location"],
            region=row["region"]
        )

    def to_row(self, team: Team) -> Dict[str, str]:
        """
        Convertit un objet Team en dictionnaire pour le CSV.
        """
        return {
            "team": team.name,
            "team_abbreviation": team.abbreviation,
            "location": team.location,
            "region": team.region
        }
