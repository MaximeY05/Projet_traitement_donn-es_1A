"""Implémentation de la classe Equipe."""


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
        autres: list[str],
        joueurs=None,
        palmares=None
    ):
        self.nom = nom
        self.localisation = localisation
        self.joueurs = joueurs
        self.palmares = palmares
        self.autres = autres

    def __str__(self) -> str:
        """Renvoie le nom de l'équipe."""
        return f"{self.nom}"
