from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.competition import Competition
from pkg.repository.data_repository import DataRepository


class CompetitionService:

    def __init__(self, repository: DataRepository, adapter: BaseAdapter):
        self.repository = repository
        self.competitions = repository.load()

    # 🔹 CREATE
    def create_competition(self, nom, equipe, match, sport):
        competition = Competition(
            nom = nom
            equipes = equipes
            matchs = matchs
        )
    


        self.matches.append(competition)
        self.repository.save(self.competitions)

        return competition

    def display_competition(self):
        compeitions = self.repository.load()
        print(competitions)
