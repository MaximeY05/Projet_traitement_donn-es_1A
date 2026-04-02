from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class FBasketballPlayerAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Joueur:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """

        return Joueur(
            nom=row["last_name"],
            prenom=row["first_name"],
            date_naissance=row["birthdate"],
            sexe="Homme",
            id=row["person_id"]
            )

    def to_row(self, joueur) -> Dict[str, str]:
        return {
            "name": joueur.nom + joueur.prenom,
            "birth_date": joueur.date_naissance,
        }
