from typing import Dict

from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class BasketballEquipeAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

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
            nom=row["full_name"],
            localisation=row["city"],
            joueurs=None,
            palmares=None,
            autres={idx: row[idx] for idx in row.index if idx not in ["full_name", "city"]}
        )

    def to_row(self, equipe) -> Dict[str, str]:
        dico = {
            "full_name": equipe.nom,
            "city": equipe.localisation
        }
        for key, value in equipe.autres.items():
            dico[key] = value
        return dico
