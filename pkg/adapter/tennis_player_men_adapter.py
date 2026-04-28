"Adapter pour les joueurs masculins de tennis"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class TennisPlayerMenAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les tennismen"""
    def adapt(self, row) -> Joueur:
        """Converti une ligne provenant d'un fichier csv lu par pandas en objet python

        Args:
            row (_type_): _description_

        Returns:
            Match: _description_
        """
        nom_complet = row["name_first"] + " " + row["name_last"]

        return Joueur(
            id=row["player_id"],
            nom=nom_complet,
            date_naissance=None,
            sexe="Homme",
            autres={idx: row[idx] for idx in row.index if idx not in ["player_id"]}
            )

    def to_row(self, joueur) -> Dict[str, str]:
        """Converti notre objet Joueur en dictionnaire prêt à être remis en csv

        Parameters
        ----------
        joueur : Joueur
            objet Joueur à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {
            "player_id": joueur.id
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
