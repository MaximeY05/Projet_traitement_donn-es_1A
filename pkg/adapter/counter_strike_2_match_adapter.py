"Adapter pour les matchs de Counter Strike 2"
from datetime import datetime
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class CounterStrike2MatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de Counter Strike 2"""
    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """

        # 1. Sécurisation de la date
        try:
            date_str = str(row.get("date", "")).strip()
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            match_date = None

        # 2. Sécurisation des scores
        try:
            score1 = int(row["score_team_1"])
            score2 = int(row["score_team_2"])
        except (ValueError, TypeError, KeyError):
            score1 = 0
            score2 = 0

        return Match(
            id=None,
            date=match_date,
            team1=row.get("team_1", "Inconnu"),
            team2=row.get("team_2", "Inconnu"),
            score1=score1,
            score2=score2,
            autres={
                  idx: row[idx] for idx in row.index
                  if idx not in ["date", "team_1", "team_2", "score_team_1", "score_team_2"]
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
                "date": match.date,
                "team_1": match.team1,
                "team_2": match.team2,
                "score_team_1": match.score1,
                "score_team_2": match.score2,
                }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
