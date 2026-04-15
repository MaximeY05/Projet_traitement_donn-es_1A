from pandas import read_csv

from typing import Dict
from datetime import datetime
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class ChessMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Match:
        """
        Convertit une ligne de atp_matches_2024.csv en objet TennisMatch.
        """

        return Match(
            id=None,
            date=None,
            team1=row["player_1"],
            team2=row["player_2"],
            score1=row["score_player_1"],
            score2=row["score_player_2"],
            autres={
                  idx: row[idx] for idx in row.index 
                  if idx not in ["player_1", "player_2", "score_player_1", "score_player_2"]
                }
            )

    def to_row(self, match: Match) -> Dict[str, any]:
        """
        Reconvertit l'objet en dictionnaire pour l'export CSV.
        """
        dico = {
                "player_1": match.team1,
                "player_2": match.team2,
                "score_player_1": match.score1,
                "score_player_2": match.score2,
                }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
