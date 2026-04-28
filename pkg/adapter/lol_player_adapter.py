from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class LolPlayerAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Joueur:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Joueur: objet Joueur correspondant aux données
        """

        return Joueur(
            id=None,
            nom=row["name"],
            date_naissance=row["birthdate"],
            sexe="Homme",
            autres={idx: row[idx] for idx in row.index if idx not in ["name", "birthdate"]}
        )

    def to_row(self, joueur: Joueur) -> Dict[str, str]:
        """
        Convertit un objet Player en dictionnaire pour le CSV.
        """
        dico = {
            "name": joueur.nom,
            "birthdate": joueur.date_naissance
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
