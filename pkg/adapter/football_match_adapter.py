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

        id_home = row.get("home_team_api_id")
        id_away = row.get("away_team_api_id")

        nom_home = self.equipes_nom.get(id_home, "Équipe Inconnue")
        nom_away = self.equipes_nom.get(id_away, "Équipe Inconnue")

        try:
            date_str = str(row.get('date', '')).split(' ', maxsplit=1)[0]
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError, IndexError):
            match_date = None

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
            "id": obj.id,
            "home_team_goal": obj.score1,
            "away_team_goal": obj.score2
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
