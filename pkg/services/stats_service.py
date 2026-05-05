from datetime import datetime


class StatsService:

    def __init__(self, matches=None, joueurs=None, equipes=None):
        self.matches = matches
        self.joueurs = joueurs
        self.equipes = equipes

    def compute_ranking(self):
        ranking = {}
        for match in self.matches:
            winner = match.winner()
            if winner:
                ranking[winner] = ranking.get(winner, 0) + 3
        return ranking

    def calendrier(self):
        calendrier = {}
        sorted_matches = sorted(self.matches, key=lambda m: m.date)
        for match in sorted_matches:
            d = str(match.date).strip()
            d = d.replace("-", "")
            d = datetime.strptime(d, "%Y%m%d")
            date_key = d.strftime("%Y/%m/%d")
            if date_key not in calendrier:
                calendrier[date_key] = []
            calendrier[date_key].append(match)
        return calendrier

    def display_calendar(self):
        calendrier = self.calendrier()
        for date in calendrier:
            print("Date : " + date)
            for m in calendrier[date]:
                print("  - " + str(m.team1) + " contre " + str(m.team2))

    def affiche_stat_match(self):
        dic = {}
        for match in self.matches:
            dic[f"{match.team1} vs {match.team2} du {match.date}"] = match.autres
        return dic

    def display_stat_joueurs(self):
        dic = {}
        for joueur in self.joueurs:
            dic[joueur.nom] = joueur.date_naissance
        return dic

    def affiche_stat_joueurs(self):
        dic_stat = {}
        for joueur in self.joueurs:
            dic_stat[joueur.nom] = joueur.autres
        return dic_stat

    def affiche_stat_1_joueur(self):
        nom_joueur = input("Entrez le nom du joueur pour voir ses stats :")
        trouve = False
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                print(f"Les statistiques de {nom_joueur} sont : {joueur.autres}")
                trouve = True
        if not trouve:
            print("Joueur non trouvé")
    """
    def affiche_1_stat(self):
        nom_joueur = input("Entrez le nom du joueur pour voir ses stats : ")
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                dico_stats = joueur.autres
        nb_stats = 0
        for cle in dico_stats:
            nb_stats = nb_stats + 1
        if nb_stats == 0:
            print("Pas de statistiques pour ce joueur.")
            return
        print("Voici les stats disponibles :")
        noms_des_stats = []
        numero = 1
        for nom_de_la_stat in dico_stats:
            print(numero, ":", nom_de_la_stat)
            noms_des_stats.append(nom_de_la_stat)
            numero = numero + 1
        choix_str = input("Entrez le numéro de la statistique : ")
        choix_int = int(choix_str)
        if choix_int > 0:
            if choix_int <= nb_stats:
                indice = choix_int - 1
                nom_choisi = noms_des_stats[indice]
                valeur_stat = dico_stats[nom_choisi]
                print(f"La statistique {nom_choisi} du joueur {nom_joueur} est : {valeur_stat}")
            else:
                print("Erreur : Ce numéro est trop grand.")
        else:
            print("Erreur : Veuillez choisir un nombre positif.")
    """

    def affiche_1_stat(self):
        nom_joueur = input("Entrez le nom du joueur pour voir ses stats : ")

        dico_stats = None

        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                dico_stats = joueur.autres
                break  # Si on a trouvé le joueur on arrête de chercher

        if dico_stats is None:
            print("Joueur non trouvé.")
            return

        nb_stats = len(dico_stats)

        if nb_stats == 0:
            print("Pas de statistiques pour ce joueur.")
            return

        print("Voici les stats disponibles :")
        noms_des_stats = []
        numero = 1
        for nom_de_la_stat in dico_stats:
            print(f"{numero} : {nom_de_la_stat}")
            noms_des_stats.append(nom_de_la_stat)
            numero += 1

        choix_str = input("Entrez le numéro de la statistique : ")

        try:
            choix_int = int(choix_str)
            if 0 < choix_int <= nb_stats:
                indice = choix_int - 1
                nom_choisi = noms_des_stats[indice]
                valeur_stat = dico_stats[nom_choisi]
                print(f"La statistique {nom_choisi} du joueur {nom_joueur} est : {valeur_stat}")
            elif choix_int > nb_stats:
                print("Erreur : Ce numéro est trop grand.")
            else:
                print("Erreur : Veuillez choisir un nombre strictement positif.")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

    def get_winrate(self, team: str) -> float:
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return 0.0
        wins = sum(1 for match in bons_matchs if match.winner() == team)
        winrate = wins/len(bons_matchs)*100
        return winrate

    def get_streak(self, team: str) -> [int]:
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return []
        tri_match = sorted(bons_matchs, key=lambda m: m.date, reverse=True)
        streak = []
        for i in min(5, len(tri_match)):
            if tri_match[0].winner() == team:
                streak.append(1)
            elif tri_match[0].winner() is None:
                streak.append(0)
            else:
                streak.append(-1)
        return streak

    def get_clean_win(self, team: str) -> float:
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return 0.0
        nb_clean = 0
        for match in bons_matchs:
            if team == match.team1:
                if match.score2 == 0:
                    nb_clean += 1
            else:
                if match.score1 == 0:
                    nb_clean += 1
        clean_rate = nb_clean/len(bons_matchs)*100
        return clean_rate

    # === STATS SPORT COLLECTIF ===
    def get_home_winrate(self, team: str) -> float:
        bons_matchs = [match for match in self.matches if team == match.team1]
        if not bons_matchs:
            return 0.0
        wins = sum(1 for match in bons_matchs if match.winner() == team)
        winrate = wins/len(bons_matchs)*100
        return winrate

    def get_efficacite_atk(self, team: str) -> float:
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return 0.0
        nb_pts = 0
        for match in bons_matchs:
            if team == match.team1:
                nb_pts += match.score1
            else:
                nb_pts += match.score2
        return nb_pts/len(bons_matchs)*100

    def get_efficacite_def(self, team: str) -> float:
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return 0.0
        nb_pts = 0
        for match in bons_matchs:
            if team == match.team1:
                nb_pts += match.score2
            else:
                nb_pts += match.score1
        return nb_pts/len(bons_matchs)*100

    def get_ecart_pts(self, team: str) -> (float, float):
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return (0.0, 0.0)
        ecart_win, ecart_lose = 0, 0
        for match in bons_matchs:
            if match.winner() == team:
                ecart_win += abs(match.score1 - match.score2)
            else:
                ecart_lose += abs(match.score1 - match.score2)
        wins = sum(1 for match in bons_matchs if match.winner() == team)
        lose = sum(1 for match in bons_matchs if
                   (match.team1 == team and match.winner() == match.team2) or
                   (match.team2 == team and match.winner() == match.team1))
        return (ecart_win/wins*100, ecart_lose/lose*100)
