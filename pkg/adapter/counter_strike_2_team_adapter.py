"Adapter pour les équipes de Counter Strike 2"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class Counterstrike2TeamAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les équipes de Counter Strike 2"""
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
            nom=row["team"],
            localisation=row["location"],
            autres={idx: row[idx] for idx in row.index if idx not in ["team", "location"]}
        )

    def to_row(self, equipe: Equipe) -> Dict[str, str]:
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        equipe : Equipe
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {
            "team": equipe.nom,
            "location": equipe.localisation
        }
        for key, value in equipe.autres.items():
            dico[key] = value
        return dico
