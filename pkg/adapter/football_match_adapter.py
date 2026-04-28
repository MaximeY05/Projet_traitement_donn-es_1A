from pandas import read_csv
from typing import Dict
from datetime import datetime

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class FootballMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()
        self.equipes_nom = {row["team_api_id"]: row["team_long_name"] for _, row in
                            read_csv("work/football/team.csv",
                            sep=",").iterrows()}

    def adapt(self, row) -> Match:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """
        date = row["date"].split(" ")[0]

        id_home, id_away = row["home_team_api_id"], row["away_team_api_id"]
        nom_home, nom_away = self.equipes_nom[id_home], self.equipes_nom[id_away]

        return Match(
            id=row["id"],
            date=datetime.strptime(date, "%Y-%m-%d").date(),
            team1=nom_home,
            team2=nom_away,
            score1=row["home_team_goal"],
            score2=row["away_team_goal"],
            autres={idx: row[idx] for idx in row.index if idx not in ["id", "home_team_goal",
                                                                      "away_team_goal"]}
        )

    def to_row(self, match) -> Dict[str, str]:
        dico = {
            "id": match.id,
            "home_team_goal": match.score1,
            "away_team_goal": match.score2
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
