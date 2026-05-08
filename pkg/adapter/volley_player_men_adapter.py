"Adapter pour les joueurs masculins de volley"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur


class VolleyPlayerMenAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les joueurs masculins de volley"""
    def adapt(self, row) -> Joueur:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row : nos données lues par pandas

        Returns
        -------
        Joueur: objet Joueur correspondant aux données
        """

        return Joueur(
            nom=row["name"],
            date_naissance=row["birth_date"],
            sexe="Homme",
            joueur_id=None,
            autres={idx: row[idx] for idx in row.index if idx not in ["name", "birth_date"]}
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
            "": obj.joueur_id,
            "name": obj.nom,
            "country_code": "",
            "height": "",
            "birth_date": obj.date_naissance,
            "birth_place": "",
            "nickname": ""
        }
        # Partie à adapter selon les noms de colonnes des fichiers csv
        dico["country_code"] = obj.autres["country_code"]
        dico["height"] = obj.autres["height"]
        dico["birth_place"] = obj.autres["birth_place"]
        dico["nickname"] = obj.autres["nickname"]

        for key, value in obj.autres.items():
            dico[key] = value
        return dico
