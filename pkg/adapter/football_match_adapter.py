from pandas import read_csv
from typing import Dict
from datetime import datetime

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class FootballMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()
        self.equipes_nom = {row["team_api_id"]: row["team_long_name"] for _, row in read_csv("Projet_traitement_donn-es_1A/work/football/team.csv", sep=",").iterrows()}

    def adapt(self, row) -> Match:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """
        date = row["date"].split(" ")[0]
        date_vrai = datetime.strptime(date, "%Y-%m-%d").date()

        

        return Match(
            id=row["id"],
            date=date_vrai,
            team1=row["home_team_api_id"],
            team2=row["away_team_api_id"],
            score1=row["home_team_goal"],
            score2=row["away_team_goal"],
            autres=None
        )

    def to_row(self, match) -> Dict[str, str]: 
        dico = {
            "id": match.id
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico

