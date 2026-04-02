from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Equipe
from pkg.models.match import Joueur
from pkg.repository.data_repository import DataRepository


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
        self.nom = nom
        self.localisation = localisation
        self.joueurs = None
        self.palmares = None

        equipe = Equipe(
            nom,
            localisation,
            joueurs,
            palmares,
        )
        self.equipes.append(equipe)
        self.repository.save(self.equipes)

        return equipe

    def display_matchs(self):
        matchs = self.repository.load()
        print(matchs)
