"""Implémentation d'une classe Compétition"""
from dataclasses import dataclass, field
from typing import Any
from pkg.models.equipe import Equipe
from pkg.models.match import Match


@dataclass
class Competition:
    """Représente une compétition"""
    id: int
    nom: str
    equipes: list[Equipe]
    matchs: list[Match]
    autres: dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        return f"{self.nom}"
