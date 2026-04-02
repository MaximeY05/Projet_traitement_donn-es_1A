import re
from typing import Dict, Tuple
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.tennis_match import TennisMatch


class TennisMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> TennisMatch:
        """
        Convertit une ligne de atp_matches_2024.csv en objet TennisMatch.
        """
        score1 = 0
        score2 = 0
        sets = row["score"].split(" ")
        for set in sets:
            scores = set.split("-")
            if int(scores[0][0]) > int(scores[1][0]):
                score1 += 1
            else:
                score2 += 1

        return Match(
            date=row["tourney_date"],
            round=row["round"],
            winner_name=row.get("winner_name", "Unknown"), # Si présent dans le CSV étendu
            loser_name=row.get("loser_name", "Unknown"),
            score_full=row["score"],
            score1=score_1,
            score2=score_2,
            winner_aces=row["w_ace"],
            loser_aces=row["l_ace"],
            minutes=row["minutes"]
        )

    def to_row(self, match: TennisMatch) -> Dict[str, any]:
        """
        Reconvertit l'objet en dictionnaire pour l'export CSV.
        """
        return {
            "tourney_name": match.tourney_name,
            "surface": match.surface,
            "tourney_date": match.date,
            "round": match.round,
            "score": match.score_full,
            "w_ace": match.winner_aces,
            "l_ace": match.loser_aces,
            "minutes": match.minutes
            # Note: score1 et score2 sont dérivés du score_full pour le CSV
        }