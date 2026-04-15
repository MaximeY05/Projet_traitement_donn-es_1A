from pandas import read_csv

from typing import Dict
from datetime import datetime
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class BadmintonMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Match:
        """
        Convertit une ligne de atp_matches_2024.csv en objet TennisMatch.
        """
        date_vrai = datetime.strptime(row["date"], "%Y-%m-%d").date()

        score1 = 0
        score2 = 0
        
        game1 = row["game_1_score"].split("-")
        if int(game1[0][0]) > int(game1[1][0]):
            score1 += 1
        else:
            score2 += 1
        
        game2 = row["game_2_score"].split("-")
        if int(game2[0][0]) > int(game2[1][0]):
            score1 += 1
        else:
            score2 += 1
        
        game3 = row["game_3_score"].split("-")
        if int(game3[0][0]) > int(game3[1][0]):
            score1 += 1
        else:
            score2 += 1

        return Match(
            id=None,
            date=date_vrai,
            team1=row["player_1"],
            team2=row["player_2"],
            score1=row["score1"],
            score2=row["score2"],
            autres={
                  idx: row[idx] for idx in row.index 
                  if idx not in ["player_1", "player_2", "game_1_score", "game_2_score"]
                }
            )

    def to_row(self, match: Match) -> Dict[str, any]:
        """
        Reconvertit l'objet en dictionnaire pour l'export CSV.
        """
        dico = {
                "player_1": match.team1,
                "player_2": match.team2,
                "game_1_score": match.score1,
                "game_2_score": match.score2,
                }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
