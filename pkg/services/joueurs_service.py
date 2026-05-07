"""Implémentation d'une classe permettant la gestion de joueurs"""
from pkg.models.joueur import Joueur
from pkg.repository.data_repository import DataRepository


class JoueurService:
    """Permet la gestion de joueurs"""
    def __init__(self, repository: DataRepository):
        self.repository = repository
        self.joueurs = repository.load()

    def create_joueur(
        self,
        nom: str,
        date_naissance: str,
        sexe: str,
            ):
        """Permet de créer un joueur"""
        joueur = Joueur(
            nom,
            date_naissance,
            sexe,
            None,
            None
        )
        self.joueurs.append(joueur)
        self.repository.save(self.joueurs)

        return joueur

    def display_joueurs(self):
        """Permet d'afficher les joueurs"""
        joueurs = self.repository.load()
        print(joueurs)
