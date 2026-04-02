"""Implémentation de la classe Equipe."""


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
        autres: list[str]
    ):
        self.nom = nom
        self.localisation = localisation
        self.joueurs = None
        self.palmares = None
        self.autres = autres

    def __str__(self) -> str:
        """Renvoie le nom de l'équipe."""
        return f"{self.nom}"
