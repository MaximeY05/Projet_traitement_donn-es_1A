from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.equipe import Equipe
from pkg.models.joueur import Joueur
from pkg.repository.data_repository import DataRepository

# A TESTER


class EquipesService:

    def __init__(self, repository: DataRepository, adapter: BaseAdapter):
        self.repository = repository
        self.equipes = repository.load()

    def create_equipe(
        self,
        nom: str,
        localisation: str,
        joueurs: list[Joueur],
        palmares: dict[str, int],
    ):

        equipe = Equipe(
            nom,
            localisation,
            joueurs,
            palmares,
            None
        )
        self.equipes.append(equipe)
        self.repository.save(self.equipes)

        return equipe

    def display_equipes(self):
        equipes = self.repository.load()
        print(equipes)
