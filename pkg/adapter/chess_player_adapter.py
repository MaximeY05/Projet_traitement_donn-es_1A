from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class ChessPlayerAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Joueur:
        """
        Convertit une ligne de player.csv en objet Player.
        """

        return Joueur(
            id=None,
            nom=row["name"],
            date_naissance=row["birth_year"],
            sexe=row["gender"],
            autres={
                idx: row[idx] for idx in row.index 
                if idx not in ["name", "birth_year", "gender"]
            }
        )

    def to_row(self, joueur: Joueur) -> Dict[str, str]:
        """
        Convertit un objet Player en dictionnaire pour le CSV.
        """
        dico = {
            "name": joueur.nom,
            "birthdate": joueur.date_naissance,
            "gender": joueur.sexe
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
