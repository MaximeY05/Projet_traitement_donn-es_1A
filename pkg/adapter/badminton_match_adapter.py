"Adapter pour les matchs de badminton"
from typing import Dict
from datetime import datetime
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class BadmintonMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de badminton"""
    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """
        score1 = 0
        score2 = 0

        # --- Gestion du Set 1 ---
        score_game_1 = str(row.get("game_1_score", "")).strip()
        if score_game_1 and score_game_1.lower() != "nan":
            try:
                game1 = score_game_1.split("-")
                if int(game1[0]) > int(game1[1]):
                    score1 += 1
                else:
                    score2 += 1
            except (ValueError, IndexError):
                pass

        # Gestion du Set 2 
        score_game_2 = str(row.get("game_2_score", "")).strip()
        if score_game_2 and score_game_2.lower() != "nan":
            try:
                game2 = score_game_2.split("-")
                if int(game2[0]) > int(game2[1]):
                    score1 += 1
                else:
                    score2 += 1
            except (ValueError, IndexError):
                pass

        # Gestion du Set 3 (Seulement s'il a été joué et s'il y a égalité avant) 
        score_game_3 = str(row.get("game_3_score", "")).strip()
        if score1 == score2 and score_game_3 and score_game_3.lower() != "nan":
            try:
                game3 = score_game_3.split("-")
                if int(game3[0]) > int(game3[1]):
                    score1 += 1
                else:
                    score2 += 1
            except (ValueError, IndexError):
                pass

        try:
            date_str = str(row.get("date", "")).split(" ")[0].strip()
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError, IndexError):
            match_date = None

        return Match(
            id=None,
            date=match_date,
            team1=row.get("player_1", "Inconnu"),
            team2=row.get("player_2", "Inconnu"),
            score1=score1,
            score2=score2,
            autres={
                  idx: row[idx] for idx in row.index
                  if idx not in ["date", "player_1", "player_2"]
                }
            )

    def to_row(self, match: Match) -> Dict[str, any]:
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        match : Match
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {
                "player_1": match.team1,
                "player_2": match.team2,
                "date": match.date
                }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
