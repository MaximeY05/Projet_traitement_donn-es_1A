"Adapter pour les joueurs de League of Legends"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class LolPlayerAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les joueurs de League of Legends"""
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
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        joueur : Joueur
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {
            "name": joueur.nom,
            "birthdate": joueur.date_naissance
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
