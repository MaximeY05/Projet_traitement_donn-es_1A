"Adapter pour les matchs de volley masculins"
from datetime import datetime
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class VolleyMatchMenAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de volley masculin"""
    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """
        # 1. Sécurisation des scores
        try:
            score1 = int(row["set_country_1"])
            score2 = int(row["set_country_2"])
        except (ValueError, TypeError):
            # Si la case est vide ou contient du texte on met 0 par défaut
            score1 = 0
            score2 = 0

        # 2. Sécurisation de la date
        try:
            # On s'assure que c'est bien une chaîne de caractères et on enlève les espaces parasites
            date_str = str(row["date"]).strip()
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            # Si le format n'est pas bon ou que la case est vide, on assigne None
            match_date = None

        return Match(
            id=None,
            date=match_date,
            team1=row["country_code_1"],
            team2=row["country_code_2"],
            score1=score1,
            score2=score2,
            autres={idx: row[idx] for idx in row.index if idx not in
                    ["date", "country_code_1", "country_code_2", "set_country_1", "set_country_2"]}
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
            "country_code_1": match.team1,
            "country_code_2": match.team2,
            "set_country_1": match.score1,
            "set_country_2": match.score2,
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
