"Adapter pour les équipes de basketball"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class BasketballEquipeAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les équipes de basketball"""
    def adapt(self, row) -> Equipe:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Equipe: objet Equipe correspondant aux données
        """
        return Equipe(
            nom=row.get("full_name", "Inconnu"),
            localisation=row.get("city", "Inconnue"),
            autres={idx: row[idx] for idx in row.index if idx not in ["full_name", "city"]}
        )

    def to_row(self, obj) -> Dict[str, str]:
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        obj : Equipe
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {
            "full_name": obj.nom,
            "city": obj.localisation
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
