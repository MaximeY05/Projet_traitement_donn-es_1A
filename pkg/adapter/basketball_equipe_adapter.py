from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class BasketballEquipeAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Equipe:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Equipe: _description_
        """

        return Equipe(
            nom=row["full_name"],
            localisation=row["full_name"],
            joueurs=row["full_name"],
            palmares=row["full_name"],
        )

    def to_row(self, match) -> Dict[str, str]:
        return {
            "date": match.date,
            "country_code_1": match.team1,
            "country_code_2": match.team2,
            "set_country_1": match.score1,
            "set_country_2": match.score2,
        }

