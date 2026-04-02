from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.competition import Competition
from pkg.repository.data_repository import DataRepository


class CompetitionService:

    def __init__(self, repository: DataRepository, adapter: BaseAdapter):
        self.repository = repository
        self.matches = repository.load()

    # 🔹 CREATE
    def create_competition(self, nom, equipe, match, sport):
        competition = Match(
            date=date,
            team1=team1,
            team2=team2,
            score1=score1,
            score2=score2,
        )

        self.matches.append(match)
        self.repository.save(self.matches)

        return match

    def display_matchs(self):
        matchs = self.repository.load()
        print(matchs)
