from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class Counterstrike2TeamAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Equipe:
        """
        Convertit une ligne de team.csv en objet Equipe.
        """
        return Equipe(
            nom=row["team"],
            localisation=row["location"],
            autres={idx: row[idx] for idx in row.index if idx not in ["team", "location"]}
        )

    def to_row(self, equipe: Equipe) -> Dict[str, str]:
        """
        Convertit un objet Equipe en dictionnaire pour le CSV.
        """
        dico = {
            "team": equipe.nom,
            "location": equipe.localisation
        }
        for key, value in equipe.autres.items():
            dico[key] = value
        return dico
