from datetime import datetime


class StatsService:

    def __init__(self, matches, joueurs):
        self.matches = matches
        self.joueurs = joueurs

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
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                print(f"Les statistiques de {nom_joueur} sont : {joueur.autres}")
                return
            print("Joueur non trouvé")

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

