from pkg.repository.data_repository import DataRepository
from pkg.services.matchs_service import MatchsService
from pkg.services.joueurs_service import JoueurService
from pkg.config.dataset_configuration import (
    DatasetConfiguration,
    volleyball_player_men_configuration,
    tennis_player_men_configuration,
    tennis_match_men_configuration,
    #tennis_match_women_configuration
    )
from pkg.services.stats_service import StatsService

def main():
    
    configuration: DatasetConfiguration = tennis_match_men_configuration

    repository = DataRepository(
        file=configuration.dataset_path_match,
        adapter=configuration.adapter_match,
        sep=configuration.dataset_sep_match,
    )
    
    MatchsService(
        adapter=configuration.adapter_match, repository=repository
    ).display_matchs()
    """
    
    configuration: DatasetConfiguration = tennis_player_men_configuration
    repository = DataRepository(
        file=configuration.dataset_path_match,
        adapter=configuration.adapter_match,
        sep=configuration.dataset_sep_match,
    )
    
    JoueurService(
        adapter=configuration.adapter_match, repository=repository
    ).display_joueurs()
    """
    #print(StatsService(matches=None, joueurs=repository.load()).affiche_stat_joueurs())
    #print(StatsService(matches=None, joueurs=repository.load()).affiche_stat_1_joueur(j[0]))
    # print(StatsService(matches=repository.load()).display_calendar())
    print(StatsService(matches=repository.load(), joueurs=None).affiche_stat_match())


if __name__ == "__main__":
    main()
