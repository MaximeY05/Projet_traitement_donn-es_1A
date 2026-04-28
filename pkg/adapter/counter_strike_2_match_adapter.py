import datetime
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class CounterStrike2MatchAdapter(BaseAdapter):

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
            team1=row["team_1"],
            team2=row["team_2"],
            score1=row["score_team_1"],
            score2=row["score_team_2"],
            autres={
                  idx: row[idx] for idx in row.index
                  if idx not in ["date", "team_1", "team_2", "score_team_1", "score_team_2"]
                }
            )

    def to_row(self, match: Match) -> Dict[str, any]:
        """
        Reconvertit l'objet en dictionnaire pour l'export CSV.
        """
        dico = {
                "date": match.date,
                "team_1": match.team1,
                "team_2": match.team2,
                "score_team_1": match.score1,
                "score_team_2": match.score2,
                }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
