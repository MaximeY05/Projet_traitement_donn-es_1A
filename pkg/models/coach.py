"""Implémentation de la classe Coach"""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Coach:
    """
    La classe Coach permet de modéliser un coach

    Atributes
    ----------
    pseudo : str
    name : str
    country_birth : str
    birthdate : str
    role : str
    team : str
    autres : {str: Any}
    """
    pseudo: str
    name: str
    country_birth: str
    birthdate: str
    role: str
    team: str
    autres: dict[str, Any] = field(default_factory=dict)

    def __str__(self) -> str:
        return f"{self.pseudo}"
