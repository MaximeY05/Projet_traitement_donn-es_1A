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

        nom_complet = f"{row.get('first_name', '')} {row.get('last_name', '')}".strip()
        if not nom_complet:
            nom_complet = "Inconnu"

        return Joueur(
            nom=nom_complet,
            date_naissance=row.get("birthdate"),
            sexe="Inconnu",
            joueur_id=row.get("person_id"),
            autres={idx: row[idx] for idx in row.index if idx not
                    in ["person_id", "birthdate", "first_name", "last_name"]}
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
            "person_id": obj.joueur_id,
            "birthdate": obj.date_naissance,
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
