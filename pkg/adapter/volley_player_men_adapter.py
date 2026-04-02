from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class VolleyPlayerMenAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Joueur:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """
        nom_complet = row["name"].split()
        name = nom_complet[0]
        surname = nom_complet[1]

        return Joueur(
            nom=name,
            prenom=surname,
            date_naissance=row["birth_date"],
            sexe="Homme",
            id=None
            )

    def to_row(self, joueur) -> Dict[str, str]:
        return {
            "name": joueur.nom + joueur.prenom,
            "birth_date": joueur.date_naissance,
        }
