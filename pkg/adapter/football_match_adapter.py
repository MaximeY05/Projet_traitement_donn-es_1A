"Adapter pour les matchs de football"
from typing import Dict
from datetime import datetime
from pandas import read_csv
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class FootballMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de football"""
    def __init__(self):
        self.equipes_nom = {row["team_api_id"]: row["team_long_name"] for _, row in
                            read_csv("work/football/team.csv",
                            sep=",").iterrows()}

    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """
        
        # 1. Sécurisation de la récupération des IDs et des noms d'équipes
        id_home = row.get("home_team_api_id")
        id_away = row.get("away_team_api_id")
        
        # Utilisation de .get() pour éviter l'erreur KeyError si l'équipe est introuvable
        nom_home = self.equipes_nom.get(id_home, "Équipe Inconnue")
        nom_away = self.equipes_nom.get(id_away, "Équipe Inconnue")

        # 2. Sécurisation de la date avec try/except
        try:
            # On récupère la date, on nettoie, et on gère l'éventuelle heure collée à la date
            date_str = str(row.get("date", "")).split(" ")[0].strip()
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError, IndexError):
            match_date = None

        # 3. Sécurisation des scores
        try:
            score1 = int(row["home_team_goal"])
            score2 = int(row["away_team_goal"])
        except (ValueError, TypeError, KeyError):
            score1 = 0
            score2 = 0

        return Match(
            id=row.get("id"),
            date=match_date,
            team1=nom_home,
            team2=nom_away,
            score1=score1,
            score2=score2,
            autres={idx: row[idx] for idx in row.index if idx not in ["id", "home_team_goal",
                                                                      "away_team_goal"]}
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
            "id": match.id,
            "home_team_goal": match.score1,
            "away_team_goal": match.score2
        }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
