from datetime import datetime
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class LolMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Match:
        """
        Convertit une ligne provenant du fichier match.csv (lu par pandas)
        en un objet python Match.
        """
        if row["winner"] == row["team_blue"]:
            score1, score2 = 1, 0
        else:
            score1, score2 = 0, 1

        return Match(
            id=None,
            date=datetime.strptime(row["date"], "%Y-%m-%d").date(),
            team1=row["team_blue"],
            team2=row["team_red"],
            score1=score1,
            score2=score2,
            autres={idx: row[idx] for idx in row.index if idx not in ["date", "team_blue",
                                                                      "team_red"]}
        )

    def to_row(self, match: Match) -> Dict[str, any]:
        """
        Convertit un objet Match en dictionnaire compatible avec le format du CSV original.
        """
        dico = {
            "date": match.date,
            "team_blue": match.team1,
            "team_red": match.team2,
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
