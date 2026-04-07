from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class BasketballMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Match:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """

        return Match(
            id=None,  # ou généré si besoin
            date=row["game_date"],
            team1=row["team_id_home"],
            team2=row["team_id_away"],
            score1=row["pts_home"],
            score2=row["pts_away"],
        )

    def to_row(self, match) -> Dict[str, str]:
        return {
            "date": match.date,
            "country_code_1": match.team1,
            "country_code_2": match.team2,
            "set_country_1": match.score1,
            "set_country_2": match.score2,
        }

