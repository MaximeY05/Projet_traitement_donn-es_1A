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

    def affiche_stat_1_joueur(self, Joueur):
        print(f"Statistiques du joueur {Joueur.nom} : {Joueur.autres}")
