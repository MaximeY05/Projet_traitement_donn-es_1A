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
        return dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))

    def get_organized_calendar(self):
        calendrier = {}
        sorted_matches = sorted(self.matches, key=lambda m: str(m.date))
        for match in sorted_matches:
            date_key = str(match.date).replace("-", "/")
            if date_key not in calendrier:
                calendrier[date_key] = []
            calendrier[date_key].append(match)
        return calendrier

    def get_player_by_name(self, nom_joueur):
        """Retourne l'objet Joueur complet ou None s'il n'existe pas."""
        for joueur in self.joueurs:
            if joueur.nom.lower() == nom_joueur.lower():
                return joueur
        return None

    def get_all_players_stats(self):
        return {j.nom: j.autres for j in self.joueurs}

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
        for i in range(min(5, len(tri_match))):
            if tri_match[i].winner() == team:
                streak.append(1)
            elif tri_match[i].winner() is None:
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

    def get_away_winrate(self, team: str) -> float:
        bons_matchs = [match for match in self.matches if team == match.team2]
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
        winrate = ecart_win/wins*100 if wins > 0 else 0.0
        loserate = ecart_lose/lose*100 if lose > 0 else 0.0
        return (winrate, loserate)

    # === STATS SPORT INDIVIDUEL ===
    def get_set_winrate(self, team: str) -> float:
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return 0.0
        nb_sets_win, nb_sets = 0, 0
        for match in bons_matchs:
            if match.team1 == team:
                nb_sets_win += match.score1
                nb_sets += match.score1 + match.score2
            else:
                nb_sets_win += match.score2
                nb_sets += match.score1 + match.score2
        return nb_sets_win/nb_sets

    # === STATS ECHECS ===
    def get_win_higher_elo(self, player: str) -> int:
        obj_joueur = self.get_player_by_name(player)
        if not obj_joueur:
            return 0
        elo = float(obj_joueur.autres["rating_standard"])
        bons_matchs = [match for match in self.matches if player == match.winner()]
        if not bons_matchs:
            return 0
        nb_win = 0
        for match in bons_matchs:
            adversaire_nom = match.team2 if player == match.team1 else match.team1
            adversaire = self.get_player_by_name(adversaire_nom)
            if float(adversaire.autres["rating_standard"]) > elo:
                nb_win += 1
        return nb_win

    def get_suface_winrate(self, player: str) -> {str: float}:
        bons_matchs = [match for match in self.matches if player in [match.team1, match.team2]]
        if not bons_matchs:
            return {"Dur": 0.0, "Terre battue": 0.0, "Gazon": 0.0}
        d, tb, g, d_win, tb_win, g_win = 0, 0, 0, 0, 0, 0
        for match in bons_matchs:
            if match.autres["surface"] == "Hard":
                d += 1
                if match.winner() == player:
                    d_win += 1
            elif match.autres["surface"] == "Clay":
                tb += 1
                if match.winner() == player:
                    tb_win += 1
            else:
                g += 1
                if match.winner() == player:
                    g_win += 1
        t_d = d_win/d*100 if d > 0 else 0.0
        t_tb = tb_win/tb*100 if tb > 0 else 0.0
        t_g = g_win/g*100 if g > 0 else 0.0
        return {"Dur": t_d, "Terre battue": t_tb, "Gazon": t_g}

    def get_average_game_time(self) -> str:
        somme = 0
        for match in self.matches:
            h, min, sec = map(int, str(match.autres["time"]).split(":"))
            somme += 3600*h + 60*min + sec
        sec_moy = somme/len(self.matches)
        avg_min = int(sec_moy // 60)
        avg_sec = int(sec_moy % 60)
        return f"{avg_min:02d}:{avg_sec:02d}"
