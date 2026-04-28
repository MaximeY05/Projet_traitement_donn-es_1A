from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class VolleyPlayerMenAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Joueur:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row : nos données lues par pandas

        Returns
        -------
        Joueur: objet Joueur correspondant aux données
        """

        return Joueur(
            nom=row["name"],
            date_naissance=row["birth_date"],
            sexe="Homme",
            id=None,
            autres={idx: row[idx] for idx in row.index if idx not in ["name", "birth_date"]}
            )

    def to_row(self, joueur) -> Dict[str, str]:
        dico = {
            "name": joueur.nom,
            "birth_date": joueur.date_naissance,
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
