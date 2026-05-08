from pkg.repository.data_repository import DataRepository
from pkg.config.dataset_configuration import (
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
    # basket_team_configuration,  Pas de stats sur les équipes pour le moment
    lol_match_configuration,
    lol_player_configuration,
    # lol_team_configuration,
    football_match_configuration,
    # football_equipe_configuration,
    football_player_configuration,
    champion_league_match_configuration,
    champion_league_player_configuration,
    # champion_league_team_configuration,
    chess_match_configuration,
    chess_player_configuration,
    cs2_match_configuration,
    cs2_player_configuration,
    # cs2_team_configuration,
    badminton_match_configuration,
    badminton_player_configuration,
    starcraft_match_configuration,
    starcraft_player_configuration
    )
from pkg.services.stats_service import StatsService


def main():
    # --- CHOIX DU SPORT ---
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

    # --- RÉCUPÉRATION DES CONFIGURATIONS ---
    config_m = None
    config_j = None

    if choix_sport == "1":
        config_m, config_j = volleyball_match_men_configuration, volleyball_player_men_configuration
    elif choix_sport == "2":
        config_m, config_j = volleyball_match_women_configuration, \
            volleyball_player_women_configuration
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
        config_m, config_j = champion_league_match_configuration, \
            champion_league_player_configuration
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

    # --- CHARGEMENT DES DONNÉES ---
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

    # --- INITIALISATION DU SERVICE DE STAT ---
    service_stats = StatsService(matches=liste_matchs, joueurs=liste_joueurs)

    # --- FONCTION POUR LE MENU ---
    def menu_stats(stats_service, id_sport):

        # PERMET D'ACCEPTER DES NOMS RENSEIGNES PRESQUE CORRECTS
        def demander_et_valider_nom(message):
            saisie = input(message)
            resultat = stats_service.trouver_vrai_nom(saisie)

            if not resultat:
                print(f" Aucun nom trouvé pour '{saisie}'.")
                return None

            if isinstance(resultat, list):
                print("\n⚠️ Plusieurs correspondances ou suggestions trouvées :")
                for i, sugg in enumerate(resultat, 1):
                    print(f"{i}. {sugg}")
                print("0. Annuler")

                choix_corr = input("Votre choix (numéro) : ")
                if choix_corr.isdigit() and 1 <= int(choix_corr) <= len(resultat):
                    return resultat[int(choix_corr)-1]
                return None

            return resultat
        # ----------------------------------------

        print("\n--- MENU STATISTIQUES ---")
        print("1. Voir le classement global")
        print("2. Voir le calendrier des matchs")
        print("3. Chercher les données brutes d'un joueur")
        print("4. Statistiques Générales (Winrate, Streak, etc.)")
        print("5. Statistiques Spécifiques (Expertise par sport)")

        choix = input("\nVotre choix : ")

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
            nom = demander_et_valider_nom("Entrez le nom du joueur : ")
            if not nom:
                return

            joueur = stats_service.get_player_by_name(nom)
            if not joueur or not joueur.autres:
                print("Aucune donnée brute pour ce joueur.")
                return

            print(f"\nDonnées pour {joueur.nom} :")
            stats_dispos = list(joueur.autres.keys())
            for i, n_stat in enumerate(stats_dispos, 1):
                print(f"{i}. {n_stat}")

            try:
                num = int(input("Choisissez un numéro : "))
                nom_stat = stats_dispos[num-1]
                print(f"\n{nom_stat} : {joueur.autres[nom_stat]}")
            except (ValueError, IndexError):
                print("Choix invalide.")

        elif choix == "4":
            nom = demander_et_valider_nom("Entrez le nom de l'équipe ou du joueur : ")
            if not nom:
                return

            print(f"\n--- STATS GENERALES : {nom} ---")
            print(f"Winrate : {stats_service.get_winrate(nom):.2f}%")
            print(f"Série : {' - '.join(stats_service.get_streak(nom))}")
            print(f"Atq (moy) : {stats_service.get_efficacite_atk(nom):.2f} pts")
            print(f"Def (moy) : {stats_service.get_efficacite_def(nom):.2f} pts")

        elif choix == "5":
            print("\n--- STATS EXPERTES ---")

            if id_sport in ["3", "4"]:  # Tennis
                nom = demander_et_valider_nom("Nom du joueur : ")
                if nom:
                    s = stats_service.get_surface_winrate(nom)
                    print(
                        f"Dur: {s['Dur']:.1f}% | "
                        f"Terre: {s['Terre battue']:.1f}% | "
                        f"Gazon: {s['Gazon']:.1f}%"
                    )

            elif id_sport == "9":  # Échecs
                nom = demander_et_valider_nom("Nom du joueur : ")
                if nom:
                    print(f"Victoires vs Meilleur Elo : {stats_service.get_win_higher_elo(nom)}")

            elif id_sport == "6":  # LoL
                print(f"Temps moyen partie : {stats_service.get_average_game_time()}")
                nom = demander_et_valider_nom("Nom de l'équipe : ")
                if nom:
                    t = stats_service.get_win_average_time(nom)
                    print(f"Winrate (Parties longues) : {t['Plus que moyenne']:.1f}%")

            elif id_sport == "5":  # Basket
                nom = demander_et_valider_nom("Nom de l'équipe : ")
                if nom:
                    print(f"Réussite à 3 pts : {stats_service.get_3pts_efficiency(nom):.2f}%")

    # Appel du menu
    menu_stats(service_stats, choix_sport)
    print()


if __name__ == "__main__":
    main()
