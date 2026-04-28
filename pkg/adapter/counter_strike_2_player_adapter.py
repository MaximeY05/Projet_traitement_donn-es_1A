from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class Counterstrike2PlayerAdapter(BaseAdapter):

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
            id=None,
            nom=row["pseudo"],
            date_naissance=row["birthdate"],
            sexe="Homme",
            autres={idx: row[idx] for idx in row.index if idx not in ["pseudo", "birthdate"]}
            )

    def to_row(self, joueur) -> Dict[str, str]:
        dico = {
            "pseudo": joueur.nom,
            "birthdate": joueur.date_naissance,
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
