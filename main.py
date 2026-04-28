from pkg.repository.data_repository import DataRepository
from pkg.services.matchs_service import MatchsService
from pkg.services.joueurs_service import JoueurService
from pkg.services.equipes_service import EquipesService
from pkg.config.dataset_configuration import (
    DatasetConfiguration,
    volleyball_player_men_configuration,
    tennis_player_men_configuration,
    tennis_player_women_configuration,
    tennis_match_men_configuration,
    tennis_match_women_configuration,
    basket_match_configuration,
    basket_player_configuration,
    basket_team_configuration,
    lol_match_configuration,
    lol_player_configuration,
    lol_team_configuration,
    football_match_configuration,
    football_equipe_configuration
    )
from pkg.services.stats_service import StatsService

def main():
    
    configuration: DatasetConfiguration = football_match_configuration

    repository = DataRepository(
        file=configuration.dataset_path_match,
        adapter=configuration.adapter_match,
        sep=configuration.dataset_sep_match,
    )
    
    MatchsService(
        adapter=configuration.adapter_match, repository=repository
    ).display_matchs()
    
    """
    configuration: DatasetConfiguration = lol_player_configuration
    repository = DataRepository(
        file=configuration.dataset_path_match,
        adapter=configuration.adapter_match,
        sep=configuration.dataset_sep_match,
    )
    JoueurService(
        adapter=configuration.adapter_match, repository=repository
    ).display_joueurs()

    
    configuration: DatasetConfiguration = lol_team_configuration
    repository = DataRepository(
        file=configuration.dataset_path_match,
        adapter=configuration.adapter_match,
        sep=configuration.dataset_sep_match,
    )
    
    EquipesService(
        adapter=configuration.adapter_match, repository=repository
    ).display_equipes()
    """

    print()
    #j = repository.load()[0]
    #dico = configuration.adapter_match.to_row(j)
    #print(dico)
    #print((configuration.adapter_match).to_row(j))
    # print(StatsService(matches=None, joueurs=repository.load()).affiche_stat_joueurs())
    #print(StatsService(matches=None, joueurs=repository.load()).affiche_stat_1_joueur(j[0]))
    # print(StatsService(matches=repository.load()).display_calendar())
    #print(StatsService(matches=repository.load(), joueurs=None).affiche_stat_match())
    #print((StatsService(matches=None, joueurs=repository.load()).affiche_stat_1_joueur()))
    #print((StatsService(matches=None, joueurs=repository.load()).affiche_stat_1_joueur()))

if __name__ == "__main__":
    main()
