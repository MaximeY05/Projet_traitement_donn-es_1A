"Adapter pour les matchs de volley féminins"
from datetime import datetime
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class VolleyMatchWomenAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de volley féminin"""
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
            score1 = int(row["set_country_1"])
            score2 = int(row["set_country_2"])
        except (ValueError, TypeError):
            score1 = 0
            score2 = 0

        try:
            date_str = str(row["date"]).strip()
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            match_date = None

        return Match(
            id=None,
            date=match_date,
            team1=row["country_1"],
            team2=row["country_2"],
            score1=score1,
            score2=score2,
            autres={idx: row[idx] for idx in row.index if idx not in
                    ["date", "country_1", "country_2", "set_country_1", "set_country_2"]}
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
            "country_1": obj.team1,
            "country_2": obj.team2,
            "set_country_1": obj.score1,
            "set_country_2": obj.score2,
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
