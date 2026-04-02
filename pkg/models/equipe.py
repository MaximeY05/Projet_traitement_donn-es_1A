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
    ):
        self.nom = nom
        self.localisation = localisation
        self.joueurs = None
        self.palmares = None

    def __str__(self) -> str:
        """Renvoie le nom de l'équipe."""
        return f"{self.nom}"

    def ajoute_joueur(self, joueur: Joueur):
        (self.joueurs).append(joueur)

    def ajoute_palmares(self, recompense: str, nombre: int):
        (self.palmares)[recompense] = nombre
