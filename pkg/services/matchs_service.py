"""Implémentation d'une classe permettant la gestion de matchs"""
from pkg.models.match import Match
from pkg.repository.data_repository import DataRepository


class MatchsService:
    """Permet la gestion de matchs"""
    def __init__(self, repository: DataRepository):
        self.repository = repository
        self.matches = repository.load()

    def create_match(self, date, team1, team2, score1, score2):
        """Permet de créer un match"""
        match = Match(
            id=None,
            date=date,
            team1=team1,
            team2=team2,
            score1=score1,
            score2=score2,
            autres=None
        )

        self.matches.append(match)
        self.repository.save(self.matches)

        return match

    def display_matchs(self):
        """Permet d'afficher les matchs"""
        matchs = self.repository.load()
        print(matchs)
