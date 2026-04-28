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
        score1 = int(row["set_country_1"])
        score2 = int(row["set_country_2"])

        return Match(
            id=None,  # ou généré si besoin
            date=datetime.strptime(row["date"], "%Y-%m-%d").date(),
            team1=row["country_1"],
            team2=row["country_2"],
            score1=score1,
            score2=score2,
            autres={idx: row[idx] for idx in row.index if idx not in
                    ["date", "country_1", "country_2", "set_country_1", "set_country_2"]}
        )

    def to_row(self, match) -> Dict[str, str]:
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
            "country_1": match.team1,
            "country_2": match.team2,
            "set_country_1": match.score1,
            "set_country_2": match.score2,
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
