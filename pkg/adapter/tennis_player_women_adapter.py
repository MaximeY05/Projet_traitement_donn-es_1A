from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class TennisPlayerWomenAdapter(BaseAdapter):

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
        nom_complet = row["name_first"] + " " + row["name_last"]

        return Joueur(
            id=row["player_id"],
            nom=nom_complet,
            date_naissance=None,
            sexe="Femme",
            autres={idx: row[idx] for idx in row.index if idx not in ["player_id"]}
            )

    def to_row(self, joueur) -> Dict[str, str]:
        dico = {
            "player_id": joueur.id
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
