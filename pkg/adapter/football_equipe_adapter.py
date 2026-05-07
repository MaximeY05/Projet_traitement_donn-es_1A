"Adapter pour les équipes de football"
from typing import Dict
from pandas import read_csv
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class FootballEquipeAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les équipes de football"""
    def __init__(self):
        df_countries = read_csv("work/football/country.csv", sep=",")
        pays_dict = df_countries.set_index('id')['name'].to_dict()

        df_matches = read_csv("work/football/match.csv", sep=",")

        self.team_to_country = {}
        for _, row in df_matches.iterrows():
            country_name = pays_dict.get(row["country_id"], "Inconnu")
            self.team_to_country[row["home_team_api_id"]] = country_name
            self.team_to_country[row["away_team_api_id"]] = country_name

    def adapt(self, row) -> Equipe:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Equipe: objet Equipe correspondant aux données
        """
        team_id = row["team_api_id"]

        pays = self.team_to_country.get(team_id, "Inconnu")

        return Equipe(
            nom=row["team_long_name"],
            localisation=pays,
            autres={idx: row[idx] for idx in row.index if idx not in ["team_long_name"]}
        )

    def to_row(self, obj) -> Dict[str, str]:
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        obj : Equipe
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {
            "team_long_name": obj.nom
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
