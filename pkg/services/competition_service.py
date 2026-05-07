"""Implémentation d'une classe permettant la gestion d'une compétition"""
from pkg.models.competition import Competition
from pkg.repository.data_repository import DataRepository


class CompetitionService:
    """Permet la gestion d'une compétition"""
    def __init__(self, repository: DataRepository):
        self.repository = repository
        self.competitions = repository.load()

    def create_competition(self, nom, equipes, matchs):
        """Permet de créer une compétition"""
        competition = Competition(None, nom, equipes, matchs, None)

        self.competitions.append(competition)
        self.repository.save(self.competitions)

        return competition

    def display_competition(self):
        """Permet d'afficher les compétitions"""
        competitions = self.repository.load()
        print(competitions)
