"Adapter pour les joueurs de football"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class FootballPlayerAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les joueurs de football"""
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
            id=row["player_api_id"],
            nom=row["player_name"],
            date_naissance=row["birthday"],
            sexe="Homme",
            autres={idx: row[idx] for idx in row.index if idx not in
                    ["player_api_id", "player_name", "birthday"]}
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
            "player_api_id": joueur.id,
            "player_name": joueur.nom,
            "birth_date": joueur.date_naissance
        }
        for key, value in joueur.autres.items():
            dico[key] = value
        return dico
