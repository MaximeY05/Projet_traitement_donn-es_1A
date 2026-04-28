from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.coach import Coach


class LolCoachAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Coach:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Coach: objet Coach correspondant aux données
        """

        return Coach(
            pseudo=row["pseudo"],
            name=row["name"],
            country_birth=row["country_of_birth"],
            birthdate=row["birthdate"],
            role=row["role"],
            team=row["team"]
        )

    def to_row(self, coach) -> Dict[str, str]:
        return {
            "pseudo": coach.pseudo,
            "name": coach.name,
            "country_of_birth": coach.country_birth,
            "birthdate": coach.birthdate,
            "role": coach.role,
            "team": coach.team
        }
