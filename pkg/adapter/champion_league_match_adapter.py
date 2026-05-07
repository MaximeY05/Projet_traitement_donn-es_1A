"Adapter pour les matchs de Champions League"
from typing import Dict
from datetime import datetime
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class ChampionleagueMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de Champions League"""
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
            date_str = str(row.get("date", "")).strip()
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            match_date = None

        try:
            score1 = int(row["score_team_home"])
            score2 = int(row["score_team_away"])
        except (ValueError, TypeError, KeyError):
            score1 = 0
            score2 = 0

        return Match(
            id=None,
            date=match_date,
            team1=row.get("team_home", "Inconnu"),
            team2=row.get("team_away", "Inconnu"),
            score1=score1,
            score2=score2,
            autres={
                idx: row[idx] for idx in row.index
                if idx not in [
                  "date", "team_home", "team_away", "score_team_home", "score_team_away"
                ]
            }
        )

    def to_row(self, obj) -> Dict[str, str]:
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
            "team_home": obj.team1,
            "team_away": obj.team2,
            "score_team_home": obj.score1,
            "score_team_away": obj.score2,
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
