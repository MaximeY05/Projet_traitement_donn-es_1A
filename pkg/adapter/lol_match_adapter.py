"Adapter pour les matchs de League of Legends"
from datetime import datetime
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class LolMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de League of Legends"""
    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """

        winner = str(row.get("winner", ""))
        team_blue = str(row.get("team_blue", ""))

        if winner == team_blue and winner != "nan":
            score1, score2 = 1, 0
        else:
            score1, score2 = 0, 1

        try:
            date_str = str(row["date"]).strip()
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError, KeyError):
            match_date = None

        return Match(
            id=None,
            date=match_date,
            team1=row.get("team_blue"),
            team2=row.get("team_red"),
            score1=score1,
            score2=score2,
            autres={idx: row[idx] for idx in row.index if idx not in
                    ["date", "team_blue", "team_red"]}
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
            "team_blue": obj.team1,
            "team_red": obj.team2
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
