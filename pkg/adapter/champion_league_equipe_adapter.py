from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class Champion_leagueEquipeAdapter(BaseAdapter):

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
            localisation=row["state"],
            joueurs=None,
            palmares=None,
        )

    def to_row(self, equipe) -> Dict[str, str]:
        return {
            "full_name": equipe.nom,
            "state": equipe.localisation,
    
        }

