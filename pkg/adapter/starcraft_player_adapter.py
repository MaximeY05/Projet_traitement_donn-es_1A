from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class StarcraftPlayerAdapter(BaseAdapter):

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
            id=None,
            nom=name,
            prenom=surname,
            date_naissance=row["birthdate"],
            sexe="Homme",
            autres={idx: row[idx] for idx in row.index if idx not in ["name", "birthdate"]}
            )

    def to_row(self, joueur) -> Dict[str, str]:
        dico = {
            "name": joueur.nom + joueur.prenom,
            "birthdate": joueur.date_naissance,
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico


