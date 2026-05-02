"Adapter pour les matchs d'échecs"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class ChessMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs d'échecs"""
    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """

        # 1. Sécurisation des scores avec float() pour gérer les 0.5 des matchs nuls
        try:
            score1 = float(row["score_player_1"])
            score2 = float(row["score_player_2"])
        except (ValueError, TypeError, KeyError):
            score1 = 0.0
            score2 = 0.0

        return Match(
            id=None,
            date=None,
            team1=str(row.get("player_1", "Inconnu")).strip(),
            team2=str(row.get("player_2", "Inconnu")).strip(),
            score1=score1,
            score2=score2,
            autres={
                  idx: row[idx] for idx in row.index
                  if idx not in ["player_1", "player_2", "score_player_1", "score_player_2"]
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
                "score_player_1": match.score1,
                "score_player_2": match.score2,
                }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
