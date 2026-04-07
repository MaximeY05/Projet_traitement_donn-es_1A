from typing import Dict
from datetime import datetime

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class FootballballMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Match:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """
        
        date_vrai = datetime.strptime(row["date"], "%Y-%m-%d").date()

        return Match(
            id=None,  # ou généré si besoin
            date=date_vrai,
            team1=row["home_team_api_id"],
            team2=row["away_team_api_id"],
            score1=row["home_team_goal"],
            score2=row["away_team_goal"],
            autres=None
        )

    def to_row(self, match) -> Dict[str, str]: 
        return {
            "date": match.date,
            "home_team_api_id": match.team1,
            "away_team_api_id": match.team2,
            "home_team_goal": match.score1,
            "away_team_goal": match.score2,
        }

