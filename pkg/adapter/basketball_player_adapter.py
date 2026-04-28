"Adapter pour les joueurs de basketball"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class BasketballPlayerAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les joueurs de basketball"""
    def adapt(self, row) -> Joueur:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Joueur: objet Joueur correspondant aux données
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
            "person_id": joueur.id,
            "birthdate": joueur.date_naissance,
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
