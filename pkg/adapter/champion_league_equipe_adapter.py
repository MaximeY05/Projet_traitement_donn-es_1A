"Adapter pour les équipes de Champions League"
from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe


class ChampionleagueEquipeAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les équipes de Champions League"""
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
            nom=row["short_name"],
            localisation=row["city"],
            autres={idx: row[idx] for idx in row.index if idx not in ["short_name", "city"]}
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
            "short_name": obj.nom,
            "city": obj.localisation,
        }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
