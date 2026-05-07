"Adapter pour les tennismen"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class TennisPlayerMenAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les tennismen"""
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
            joueur_id=row["player_id"],
            nom=nom_complet,
            date_naissance=None,
            sexe="Homme",
            autres={idx: row[idx] for idx in row.index if idx not in ["player_id"]}
            )

    def to_row(self, obj) -> Dict[str, str]:
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        obj : Joueur
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {
            "player_id": obj.joueur_id
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
