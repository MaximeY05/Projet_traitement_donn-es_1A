from pkg.repository.data_repository import DataRepository
from pkg.services.matchs_service import MatchsService
from pkg.services.joueurs_service import JoueurService
from pkg.services.equipes_service import EquipesService
from pkg.config.dataset_configuration import (
    DatasetConfiguration,
    volleyball_match_men_configuration,
    volleyball_match_women_configuration,
    volleyball_player_men_configuration,
    volleyball_player_women_configuration,
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
    football_equipe_configuration,
    football_player_configuration,
    champion_league_match_configuration,
    champion_league_player_configuration,
    champion_league_team_configuration,
    chess_match_configuration,
    chess_player_configuration,
    cs2_match_configuration,
    cs2_player_configuration,
    cs2_team_configuration,
    badminton_match_configuration,
    badminton_player_configuration,
    starcraft_match_configuration,
    starcraft_player_configuration
    )
from pkg.services.stats_service import StatsService

def main():

    # Pour changer de jeu de données, remplacer la variable ci-dessous
    # par l'une des configurations importées tout en haut !
    configuration: DatasetConfiguration = lol_match_configuration

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


    configuration: DatasetConfiguration = basket_team_configuration
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
    # j = repository.load()[0]
    # dico = configuration.adapter_match.to_row(j)
    # print(dico)
    # print((configuration.adapter_match).to_row(j))
    print(StatsService(matches=None, joueurs=repository.load()).affiche_stat_joueurs())
    # print(StatsService(matches=None, joueurs=repository.load()).affiche_stat_1_joueur(j[0]))
    # print(StatsService(matches=repository.load()).display_calendar())
    # print(StatsService(matches=repository.load(), joueurs=None).affiche_stat_match())
    # print((StatsService(matches=None, joueurs=repository.load()).affiche_stat_1_joueur()))
    # print((StatsService(matches=None, joueurs=repository.load()).affiche_stat_1_joueur()))

    def menu_stats(stats_service):
        print("\n--- MENU STATISTIQUES ---")
        print("1. Voir le classement")
        print("2. Voir le calendrier")
        print("3. Chercher une stat précise sur un joueur")

        choix = input("Votre choix : ")

        if choix == "1":
            classement = stats_service.compute_ranking()
            print("\nCLASSEMENT ACTUEL :")
            for i, (nom, points) in enumerate(classement.items(), 1):
                print(f"{i}. {nom:20} | {points} pts")

        elif choix == "2":
            cal = stats_service.get_organized_calendar()
            for date, matchs in cal.items():
                print(f"\nDate : {date}")
                for m in matchs:
                    print(f"  {m.team1} vs {m.team2}")

        elif choix == "3":
            nom = input("Entrez le nom du joueur : ")
            joueur = stats_service.get_player_by_name(nom)

            if not joueur:
                print("Joueur non trouvé.")
                return

            if not joueur.autres:
                print("Aucune statistique disponible pour ce joueur.")
                return

            # Affichage de la liste des stats disponibles
            stats_dispos = list(joueur.autres.keys())
            print("\nStats disponibles :")
            for i, nom_stat in enumerate(stats_dispos, 1):
                print(f"{i}. {nom_stat}")

            try:
                num = int(input("Choisissez un numéro : "))
                nom_stat_choisie = stats_dispos[num-1]
                valeur = joueur.autres[nom_stat_choisie]
                print(f"\n{nom_stat_choisie} de {joueur.nom} : {valeur}")
            except (ValueError, IndexError):
                print("Choix invalide.")


if __name__ == "__main__":
    main()
