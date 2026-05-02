"Adapter pour les matchs de basketball"
from typing import Dict
from datetime import datetime
from pandas import read_csv
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class BasketballMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de basketball"""
    def __init__(self):
        self.equipes_nom = {row["id"]: row["full_name"] for _, row in
                            read_csv("work/basketball/team.csv", sep=",").iterrows()}

    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """

        # 1. Sécurisation de la récupération des noms
        id_home = row.get("team_id_home")
        id_away = row.get("team_id_away")
        nom_home = self.equipes_nom.get(id_home, "Équipe Inconnue")
        nom_away = self.equipes_nom.get(id_away, "Équipe Inconnue")

        # 2. Sécurisation de la date
        try:
            date_str = str(row.get("game_date", "")).split(" ")[0].strip()
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError, IndexError):
            match_date = None

        # 3. Sécurisation des scores
        try:
            score1 = int(row["pts_home"])
            score2 = int(row["pts_away"])
        except (ValueError, TypeError, KeyError):
            score1 = 0
            score2 = 0

        return Match(
            id=row.get("game_id"),
            date=match_date,
            team1=nom_home,
            team2=nom_away,
            score1=score1,
            score2=score2,
            autres={idx: row[idx] for idx in row.index if idx not 
                    in ["game_id", "game_date", "pts_home", "pts_away"]}
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
            "game_id": match.id,
            "pts_home": match.score1,
            "pts_away": match.score2
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
