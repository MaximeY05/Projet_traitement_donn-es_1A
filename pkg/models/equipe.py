"""Implémentation de la classe Equipe."""

# from typing import Any

from .joueur import Joueur


class Equipe:
    """
    La classe Equipe permet de modéliser une équipe.

    Atributes
    ----------
    nom : str
    """

    def __init__(
        self,
        nom: str,
        localisation: str,
        joueurs: list[Joueur],
        palmares: dict[str, int],
        id: int
    ):
        self.nom = nom
        self.localisation = localisation
        self.joueurs = None
        self.palmares = None
        self.id = id
    
    def __str__(self) -> str:
        """Renvoie le nom de l'équipe."""
        return f"{self.__nom}"

    def ajoute_joueur(self, joueur: Joueur):
        (self.joueurs).append(joueur)
