"""Implémentation de la classe Joueur"""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Joueur:
    """
    La classe Joueur permet de modéliser un joueur

    Atributes
    ----------
    nom : str
    date_naissance : str
    sexe : str
    joueur_id : int
    autres : {str: Any}
    """

    nom: str
    date_naissance: str
    sexe: str
    joueur_id: int
    autres: dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        return f"{self.nom}"
