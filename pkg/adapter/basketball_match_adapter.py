from pandas import read_csv
from typing import Dict
from datetime import datetime

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class BasketballMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()
        self.equipes_nom = {row["id"]: row["full_name"] for _, row in
                            read_csv("work/basketball/team.csv", sep=",").iterrows()}

    def adapt(self, row) -> Match:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """

        id_home, id_away = row["team_id_home"], row["team_id_away"]
        nom_home, nom_away = self.equipes_nom[id_home], self.equipes_nome[id_away]

        return Match(
            id=row["game_id"],
            date=datetime.strptime(row["game_date"], "%Y-%m-%d").date(),
            team1=nom_home,
            team2=nom_away,
            score1=row["pts_home"],
            score2=row["pts_away"],
            autres={idx: row[idx] for idx in row.index if idx not in ["game_id", "game_date",
                                                                      "pts_home", "pts_away"]}
        )

    def to_row(self, match) -> Dict[str, str]:
        dico = {
            "game_id": match.id,
            "pts_home": match.score1,
            "pts_away": match.score2
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
