from typing import Dict
from datetime import datetime

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class ChampionleagueMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """

        return Match(
            id=None,
            date=datetime.strptime(row["date"], "%Y-%m-%d").date(),
            team1=row["team_home"],
            team2=row["team_away"],
            score1=row["score_team_home"],
            score2=row["score_team_away"],
            autres={
                idx: row[idx] for idx in row.index
                if idx not in [
                  "date", "team_home", "team_away", "score_team_home", "score_team_away"
                ]
            }
        )

    def to_row(self, match) -> Dict[str, str]:
        dico = {
            "date": match.date,
            "team_home": match.team1,
            "team_away": match.team2,
            "score_team_home": match.score1,
            "score_team_away": match.score2,
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
