"Adapter pour les joueurs de Champions League"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class ChampionleaguePlayerAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les joueurs de Champions League"""
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
            joueur_id=None,
            nom=row["player_name"],
            date_naissance=None,
            sexe="Homme",
            autres={idx: row[idx] for idx in row.index if idx not in ["player_name"]}
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
            "player_name": obj.nom,
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
