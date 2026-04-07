from pandas import read_csv

from typing import Dict
from datetime import datetime
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class TennisMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()
        self.joueurs = {row["player_id"]: row for _, row in read_csv(self.file, sep=self.sep).iterrows()}

    def adapt(self, row) -> Match:
        """
        Convertit une ligne de atp_matches_2024.csv en objet TennisMatch.
        """
        if row["score"][:len(row["score"]) - 3] in ["W/O", "RET", "DEF"]:
            scorewin = 0
            scorelose = -1
        else:
            score1 = 0
            score2 = 0
            sets = row["score"].split(" ")
            for set in sets:
                scores = set.split("-")
                if int(scores[0][0]) > int(scores[1][0]):
                    score1 += 1
                else:
                    score2 += 1
            if score1 > score2:
                scorewin = score1
                scorelose = score2
            else:
                scorewin = score2
                scorelose = score1

        return Match(
            id=None,
            date=datetime.strptime(row["tourney_date"], "%Y-%m%d").date(),
            team1=self.joueurs[row["winner_id"]]["name_first"] + self.joueurs[row["winner_id"]]["name_last"],
            team2=self.joueurs[row["loser_id"]]["name_first"] + self.joueurs[row["loser_id"]]["name_last"],
            score1=scorewin,
            score2=scorelose,
            autres={idx: row[idx] for idx in row.index if idx not in ["tourney_date"]}
        )

    def to_row(self, match: Match) -> Dict[str, any]:
        """
        Reconvertit l'objet en dictionnaire pour l'export CSV.
        """
        dico = {"tourney_date": match.date}
        for key, value in match.autres.items():
            dico[key] = value
        return dico
