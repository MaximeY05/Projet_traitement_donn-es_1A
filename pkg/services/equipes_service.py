"""Implémentation d'une classe permettant la gestion d'équipes"""
from pkg.models.equipe import Equipe
from pkg.repository.data_repository import DataRepository


class EquipesService:
    """Permet la gestion d'équipes"""
    def __init__(self, repository: DataRepository):
        self.repository = repository
        self.equipes = repository.load()

    def create_equipe(
        self,
        nom: str,
        localisation: str
    ):
        """Permet de créer une équipe"""
        equipe = Equipe(
            nom,
            localisation,
            None
        )
        self.equipes.append(equipe)
        self.repository.save(self.equipes)

        return equipe

    def display_equipes(self):
        """Permet d'afficher les équipes"""
        equipes = self.repository.load()
        print(equipes)
