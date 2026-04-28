from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class BasketballPlayerAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Joueur:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """
        nom_complet = row["last_name"] + " " + row["first_name"]

        return Joueur(
            nom=nom_complet,
            date_naissance=row["birthdate"],
            sexe="Homme",
            id=row["person_id"],
            autres={idx: row[idx] for idx in row.index if idx not in ["person_id", "birthdate"]}
            )

    def to_row(self, joueur) -> Dict[str, str]:
        dico = {
            "person_id": joueur.id,
            "birthdate": joueur.date_naissance,
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
