from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.competition import Competition
from pkg.repository.data_repository import DataRepository


class CompetitionService:

    def __init__(self, repository: DataRepository, adapter: BaseAdapter):
        self.repository = repository
        self.competitions = repository.load()

    def create_competition(self, nom, equipes, matchs):
        competition = Competition(nom, equipes, matchs)
    
        self.competitions.append(competition)
        self.repository.save(self.competitions)

        return competition

    def display_competition(self):
        competitions = self.repository.load()
        print(competitions)
