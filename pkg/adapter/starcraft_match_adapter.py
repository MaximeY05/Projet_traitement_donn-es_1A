"Adapter pour les matchs de Starcraft"
from typing import Dict
from datetime import datetime
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class StarcraftMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de Starcraft"""
    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """

        try:
            date_str = str(row.get('date', '')).split(' ', maxsplit=1)[0]
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError, IndexError):
            match_date = None

        try:
            score1 = int(row["score_player_1"])
            score2 = int(row["score_player_2"])
        except (ValueError, TypeError, KeyError):
            score1 = 0
            score2 = 0

        return Match(
            id=None,
            date=match_date,
            team1=row.get("player_1", "Inconnu"),
            team2=row.get("player_2", "Inconnu"),
            score1=score1,
            score2=score2,
            autres={
                  idx: row[idx] for idx in row.index
                  if idx not in ["date", "player_1", "player_2", "score_player_1", "score_player_2"]
                }
            )

    def to_row(self, obj: Match) -> Dict[str, any]:
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        obj : Match
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {
                "date": obj.date,
                "player_1": obj.team1,
                "player_2": obj.team2,
                "score_player_1": obj.score1,
                "score_player_2": obj.score2,
                }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
