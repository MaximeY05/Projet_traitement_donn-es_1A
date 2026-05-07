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

        pseudo = str(row.get("pseudo", "Inconnu")).strip()
        if pseudo.lower() == "nan" or not pseudo:
            pseudo = "Inconnu"

        return Joueur(
            joueur_id=None,
            nom=pseudo,
            date_naissance=row.get("birthdate"),
            sexe="Inconnu",
            autres={idx: row[idx] for idx in row.index if idx not in ["pseudo", "birthdate"]}
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
            "pseudo": obj.nom,
            "birthdate": obj.date_naissance,
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
