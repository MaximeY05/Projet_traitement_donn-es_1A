"Adapter pour les joueurs de Starcraft"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class StarcraftPlayerAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les joueurs de Starcraft"""
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
            nom=row["pseudo"],
            date_naissance=row["birthdate"],
            sexe="Homme",
            autres={idx: row[idx] for idx in row.index if idx not in ["pseudo", "birthdate"]}
            )

    def to_row(self, joueur) -> Dict[str, str]:
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
            "pseudo": joueur.pseudo,
            "birthdate": joueur.date_naissance,
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
