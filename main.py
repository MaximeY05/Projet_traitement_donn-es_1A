"""
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

    # MatchsService(
    #    adapter=configuration.adapter_match, repository=repository
    # ).display_matchs()
    MatchsService(
         repository=repository
    ).display_matchs()

    
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
    

    print()
    # j = repository.load()[0]
    # dico = configuration.adapter_match.to_row(j)
    # print(dico)
    # print((configuration.adapter_match).to_row(j))
    # print(StatsService(matches=None, joueurs=repository.load()).affiche_stat_joueurs())
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

    menu_stats(# a completer  )

if __name__ == "__main__":
    main()

"""










"""
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
    # --- ÉTAPE 1 : CHOIX DU SPORT ---
    print("--- BIENVENUE DANS VOTRE GESTIONNAIRE DE STATS SPORTIVES ---")
    print("Quel sport souhaitez-vous consulter ?")
    print("1.  Volleyball Masculin")
    print("2.  Volleyball Féminin")
    print("3.  Tennis Masculin (ATP)")
    print("4.  Tennis Féminin (WTA)")
    print("5.  Basketball (NBA)")
    print("6.  League of Legends")
    print("7.  Football")
    print("8.  Champions League")
    print("9.  Échecs")
    print("10. Counter-Strike 2")
    print("11. Badminton")
    print("12. Starcraft 2")
    
    choix_sport = input("\nEntrez le numéro du sport : ")

    # --- ÉTAPE 2 : RÉCUPÉRATION DES CONFIGURATIONS ---
    config_m = None
    config_j = None

    if choix_sport == "1":
        config_m, config_j = volleyball_match_men_configuration, volleyball_player_men_configuration
    elif choix_sport == "2":
        config_m, config_j = volleyball_match_women_configuration, volleyball_player_women_configuration
    elif choix_sport == "3":
        config_m, config_j = tennis_match_men_configuration, tennis_player_men_configuration
    elif choix_sport == "4":
        config_m, config_j = tennis_match_women_configuration, tennis_player_women_configuration
    elif choix_sport == "5":
        config_m, config_j = basket_match_configuration, basket_player_configuration
    elif choix_sport == "6":
        config_m, config_j = lol_match_configuration, lol_player_configuration
    elif choix_sport == "7":
        config_m, config_j = football_match_configuration, football_player_configuration
    elif choix_sport == "8":
        config_m, config_j = champion_league_match_configuration, champion_league_player_configuration
    elif choix_sport == "9":
        config_m, config_j = chess_match_configuration, chess_player_configuration
    elif choix_sport == "10":
        config_m, config_j = cs2_match_configuration, cs2_player_configuration
    elif choix_sport == "11":
        config_m, config_j = badminton_match_configuration, badminton_player_configuration
    elif choix_sport == "12":
        config_m, config_j = starcraft_match_configuration, starcraft_player_configuration
    else:
        print("Erreur : Choix invalide.")
        return

    # --- ÉTAPE 3 : CHARGEMENT DES DONNÉES ---
    # Chargement des matchs
    repo_m = DataRepository(
        file=config_m.dataset_path_match,
        adapter=config_m.adapter_match,
        sep=config_m.dataset_sep_match,
    )
    liste_matchs = repo_m.load()

    # Chargement des joueurs
    repo_j = DataRepository(
        file=config_j.dataset_path_match,
        adapter=config_j.adapter_match,
        sep=config_j.dataset_sep_match,
    )
    liste_joueurs = repo_j.load()

    # --- ÉTAPE 4 : INITIALISATION DU SERVICE ---
    service_stats = StatsService(matches=liste_matchs, joueurs=liste_joueurs)

    # --- ÉTAPE 5 : FONCTION MENU_STATS (Noms originaux conservés) ---
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
                    print(f"  {m.team1} {m.score1} - {m.score2} {m.team2}")

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

    # Appel du menu
    menu_stats(service_stats)



if __name__ == "__main__":
    main()
"""





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
    # --- ÉTAPE 1 : CHOIX DU SPORT ---
    print("--- BIENVENUE DANS VOTRE GESTIONNAIRE DE STATS SPORTIVES ---")
    print("Quel sport souhaitez-vous consulter ?")
    print("1.  Volleyball Masculin")
    print("2.  Volleyball Féminin")
    print("3.  Tennis Masculin (ATP)")
    print("4.  Tennis Féminin (WTA)")
    print("5.  Basketball (NBA)")
    print("6.  League of Legends")
    print("7.  Football")
    print("8.  Champions League")
    print("9.  Échecs")
    print("10. Counter-Strike 2")
    print("11. Badminton")
    print("12. Starcraft 2")
    
    choix_sport = input("\nEntrez le numéro du sport : ")

    # --- ÉTAPE 2 : RÉCUPÉRATION DES CONFIGURATIONS ---
    config_m = None
    config_j = None

    if choix_sport == "1":
        config_m, config_j = volleyball_match_men_configuration, volleyball_player_men_configuration
    elif choix_sport == "2":
        config_m, config_j = volleyball_match_women_configuration, volleyball_player_women_configuration
    elif choix_sport == "3":
        config_m, config_j = tennis_match_men_configuration, tennis_player_men_configuration
    elif choix_sport == "4":
        config_m, config_j = tennis_match_women_configuration, tennis_player_women_configuration
    elif choix_sport == "5":
        config_m, config_j = basket_match_configuration, basket_player_configuration
    elif choix_sport == "6":
        config_m, config_j = lol_match_configuration, lol_player_configuration
    elif choix_sport == "7":
        config_m, config_j = football_match_configuration, football_player_configuration
    elif choix_sport == "8":
        config_m, config_j = champion_league_match_configuration, champion_league_player_configuration
    elif choix_sport == "9":
        config_m, config_j = chess_match_configuration, chess_player_configuration
    elif choix_sport == "10":
        config_m, config_j = cs2_match_configuration, cs2_player_configuration
    elif choix_sport == "11":
        config_m, config_j = badminton_match_configuration, badminton_player_configuration
    elif choix_sport == "12":
        config_m, config_j = starcraft_match_configuration, starcraft_player_configuration
    else:
        print("Erreur : Choix invalide.")
        return

    # --- ÉTAPE 3 : CHARGEMENT DES DONNÉES ---
    repo_m = DataRepository(
        file=config_m.dataset_path_match,
        adapter=config_m.adapter_match,
        sep=config_m.dataset_sep_match,
    )
    liste_matchs = repo_m.load()

    repo_j = DataRepository(
        file=config_j.dataset_path_match,
        adapter=config_j.adapter_match,
        sep=config_j.dataset_sep_match,
    )
    liste_joueurs = repo_j.load()

    # --- ÉTAPE 4 : INITIALISATION DU SERVICE ---
    service_stats = StatsService(matches=liste_matchs, joueurs=liste_joueurs)

    # --- ÉTAPE 5 : FONCTION MENU_STATS ADAPTÉE ---
    def menu_stats(stats_service, id_sport):
        print("\n--- MENU STATISTIQUES ---")
        print("1. Voir le classement global")
        print("2. Voir le calendrier des matchs")
        print("3. Chercher les données brutes d'un joueur")
        print("4. Statistiques Générales (Performances d'une équipe/joueur)")
        print("5. Statistiques Spécifiques (Adaptées au sport choisi)")

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
                    print(f"  {m.team1} {m.score1} - {m.score2} {m.team2}")

        elif choix == "3":
            nom = input("Entrez le nom du joueur : ")
            joueur = stats_service.get_player_by_name(nom)

            if not joueur:
                print("Joueur non trouvé.")
                return

            if not joueur.autres:
                print("Aucune statistique disponible pour ce joueur.")
                return

            stats_dispos = list(joueur.autres.keys())
            print("\nDonnées brutes disponibles :")
            for i, nom_stat in enumerate(stats_dispos, 1):
                print(f"{i}. {nom_stat}")

            try:
                num = int(input("Choisissez un numéro : "))
                nom_stat_choisie = stats_dispos[num-1]
                valeur = joueur.autres[nom_stat_choisie]
                print(f"\n{nom_stat_choisie} de {joueur.nom} : {valeur}")
            except (ValueError, IndexError):
                print("Choix invalide.")

        elif choix == "4":
            nom = input("Entrez le nom de l'équipe ou du joueur : ")
            print(f"\n--- STATS GENERALES POUR : {nom} ---")
            print(f"Winrate global : {stats_service.get_winrate(nom):.2f}%")
            serie_formatee = " - ".join(stats_service.get_streak(nom))
            print(f"Série (5 derniers matchs) : {serie_formatee}")
            print(f"Victoires 'Clean' (adversaire à 0) : {stats_service.get_clean_win(nom):.2f}%")
            print(f"Efficacité Attaque (pts moyens marqués) : {stats_service.get_efficacite_atk(nom):.2f}")
            print(f"Efficacité Défense (pts moyens encaissés) : {stats_service.get_efficacite_def(nom):.2f}")

            ecarts = stats_service.get_ecart_pts(nom)
            print(f"Écart moyen lors d'une victoire : {ecarts['Ecart_victoire']:.2f} pts")
            print(f"Écart moyen lors d'une défaite : {ecarts['Ecart_defaite']:.2f} pts")

        elif choix == "5":
            print(f"\n--- STATS SPECIFIQUES AU SPORT ---")

            # --- TENNIS ---
            if id_sport in ["3", "4"]:
                nom = input("Entrez le nom du joueur : ")
                surfaces = stats_service.get_surface_winrate(nom)
                print(f"Winrate sur Dur : {surfaces.get('Dur', 0):.2f}%")
                print(f"Winrate sur Terre Battue : {surfaces.get('Terre battue', 0):.2f}%")
                print(f"Winrate sur Gazon : {surfaces.get('Gazon', 0):.2f}%")
            
            # --- ECHECS ---
            elif id_sport == "9": 
                nom = input("Entrez le nom du joueur : ")
                exploits = stats_service.get_win_higher_elo(nom)
                print(f"Victoires contre des joueurs mieux classés (Elo supérieur) : {exploits}")
            
            # --- LEAGUE OF LEGENDS ---
            elif id_sport == "6": 
                print(f"Temps moyen d'une partie dans le tournoi : {stats_service.get_average_game_time()}")
                nom = input("Entrez le nom de l'équipe pour croiser avec le temps : ")
                temps_winrate = stats_service.get_win_average_time(nom)
                print(f"Winrate si la partie dure + longtemps que la moyenne : {temps_winrate['Plus que moyenne']:.2f}%")
                print(f"Winrate si la partie est + rapide que la moyenne : {temps_winrate['Moins que moyenne']:.2f}%")
            
            # --- BASKETBALL ---
            elif id_sport == "5": 
                nom = input("Entrez le nom de l'équipe : ")
                print(f"Efficacité moyenne à 3 points : {stats_service.get_3pts_efficiency(nom):.2f}%")
            
            else:
                print("Aucune statistique experte n'a été codée pour ce sport particulier pour le moment.")

    # Appel du menu en passant le service ET le sport sélectionné
    menu_stats(service_stats, choix_sport)

    # --- LIGNES COMMENTÉES CONSERVÉES ---
    """
    # MatchsService(repository=repo_m, adapter=config_m.adapter_match).display_matchs()
    # JoueurService(adapter=config_j.adapter_match, repository=repo_j).display_joueurs()
    # EquipesService(adapter=config_m.adapter_match, repository=repo_m).display_equipes()
    """

if __name__ == "__main__":
    main()