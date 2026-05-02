"Adapter pour les joueurs d'échecs"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class ChessPlayerAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les joueurs d'échecs"""
    def adapt(self, row) -> Joueur:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Joueur: objet Joueur correspondant aux données
        """

        # Sécurisation du nom pour éviter les crashs sur les NaN
        nom_joueur = str(row.get("name", "Inconnu")).strip()
        if nom_joueur.lower() == "nan":
            nom_joueur = "Inconnu"

        return Joueur(
            id=None,
            nom=nom_joueur,
            date_naissance=row.get("birth_year"),
            sexe=row.get("gender", "Inconnu"),
            autres={
                idx: row[idx] for idx in row.index
                if idx not in ["name", "birth_year", "gender"]
            }
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
            "birth_year": joueur.date_naissance,
            "gender": joueur.sexe
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
