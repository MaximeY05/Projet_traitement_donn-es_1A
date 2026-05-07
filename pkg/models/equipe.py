"""Implémentation de la classe Equipe."""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Equipe:
    """
    La classe Equipe permet de modéliser une équipe.

    Atributes
    ----------
    nom : str
    localisation : str
    autres : {str: Any}
    """
    nom: str
    localisation: str
    autres: dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        """Renvoie le nom de l'équipe.

        Returns
        --------
        str : Nom de l'équipe
        """
        return f"{self.nom}"
