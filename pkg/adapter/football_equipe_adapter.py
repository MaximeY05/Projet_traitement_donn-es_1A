from pandas import read_csv
from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class FootballEquipeAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()
        df_countries = read_csv("Projet_traitement_donn-es_1A/work/football/country.csv", sep=",")
        pays_dict = df_countries.set_index('id')['name'].to_dict()

        df_matches = read_csv("Projet_traitement_donn-es_1A/work/football/match.csv", sep=",")

        self.team_to_country = {}
        for _, row in df_matches.iterrows():
            country_name = pays_dict[row["country_id"]]
            self.team_to_country[row["home_team_api_id"]] = country_name
            self.team_to_country[row["away_team_api_id"]] = country_name

    def adapt(self, row) -> Equipe:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Equipe: _description_
        """

        team_id = row["team_api_id"]
        pays = self.team_to_country[team_id]

        return Equipe(
            nom=row["full_name"],
            localisation=row["state"],
            joueurs=None,
            palmares=None,
        )

    def to_row(self, equipe) -> Dict[str, str]:
        return {
            "full_name": equipe.nom,
            "state": equipe.localisation,
    
        }

