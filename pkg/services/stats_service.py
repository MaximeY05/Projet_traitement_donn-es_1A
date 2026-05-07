"""Implémentation d'une classe permettant la gestion de statistiques sur nos données"""


class StatsService:
    """Permet la gestion de statistiques sur nos données"""
    def __init__(self, matches=None, joueurs=None, equipes=None):
        self.matches = matches
        self.joueurs = joueurs
        self.equipes = equipes

    # === STATS GENERALES ===
    def compute_ranking(self) -> dict:
        """Fournit un classement

        Returns
        --------
        dict : Représente le classement
        """
        ranking = {}
        for match in self.matches:
            winner = match.winner()
            if winner:
                ranking[winner] = ranking.get(winner, 0) + 3
        return dict(sorted(ranking.items(), key=lambda item: item[1], reverse=True))

    def get_organized_calendar(self):
        """Permet d'avoir un calendrier"""
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
        """Donne toutes les stats d'un joueur"""
        return {j.nom: j.autres for j in self.joueurs}

    def get_all_match_stats(self):
        """Donne toutes les stats d'un match"""
        return {(m.team1, m.team2): m.autres for m in self.matches}

    def get_winrate(self, team: str) -> float:
        """Donne le pourcentage de victoire d'une équipe"""
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return 0.0
        wins = sum(1 for match in bons_matchs if match.winner() == team)
        winrate = wins/len(bons_matchs)*100
        return winrate

    def get_streak(self, team: str) -> [int]:
        """Donne le résultat des 5 derniers matchs pour l'équipe team"""
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
        """Donne le pourcentage de victoire sans que l'adversaire n'ait de points"""
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
        """Donne le pourcentage de victoire à domicile"""
        bons_matchs = [match for match in self.matches if team == match.team1]
        if not bons_matchs:
            return 0.0
        wins = sum(1 for match in bons_matchs if match.winner() == team)
        winrate = wins/len(bons_matchs)*100
        return winrate

    def get_away_winrate(self, team: str) -> float:
        """Donne le pourcentage de victoires à l'extérieur"""
        bons_matchs = [match for match in self.matches if team == match.team2]
        if not bons_matchs:
            return 0.0
        wins = sum(1 for match in bons_matchs if match.winner() == team)
        winrate = wins/len(bons_matchs)*100
        return winrate

    def get_efficacite_atk(self, team: str) -> float:
        """Donne le nombre moyen de points marqués dans les matchs"""
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
        """Donne le nombre moyen de points encaissés dans les matchs"""
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

    def get_ecart_pts(self, team: str) -> {str: float}:
        """Donne les moyennes des nombres de points d'écart avec l'adversaire
        lors des victoires et défaites"""
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return {"Ecart_victoire": 0.0, "Ecart_defaite": 0.0}
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
        return {"Ecart_victoire": winrate, "Ecart_defaite": loserate}

    # === STATS SPORT INDIVIDUEL ===
    def get_set_winrate(self, team: str) -> float:
        """Donne le pourcentage de victoire de sets"""
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
        return nb_sets_win/nb_sets*100

    # === STATS ECHECS ===
    def get_win_higher_elo(self, player: str) -> int:
        """Donne le nombre de victoires contre des joueurs ayant un meilleur elo"""
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

    # === STATS TENNIS ===
    def get_surface_winrate(self, player: str) -> {str: float}:
        """Donne le pourcentage de victoire selon la surface"""
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

    # === STATS LOL ===
    def get_average_game_time(self) -> str:
        """Donne le temps moyen d'une partie de LOL"""
        somme = 0
        for match in self.matches:
            h, minu, sec = map(int, str(match.autres["time"]).split(":"))
            somme += 3600*h + 60*minu + sec
        sec_moy = somme/len(self.matches)
        avg_min = int(sec_moy // 60)
        avg_sec = int(sec_moy % 60)
        return f"{avg_min:02d}:{avg_sec:02d}"

    def get_win_average_time(self, team: str) -> {str: float}:
        """Donne le pourcentage de victoire lorsque la partie a un temps supérieur ou
        inférieur au temps moyen"""
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return {"Plus que moyenne": 0.0, "Moins que moyenne": 0.0}
        nb_win_over, nb_game_over, nb_win_under, nb_game_under = 0, 0, 0, 0
        minu, sec = map(int, self.get_average_game_time().split(":"))
        avg_sec = 60*minu + sec
        for match in bons_matchs:
            h, minu, sec = map(int, str(match.autres["time"]).split(":"))
            match_sec = 3600*h + 60*minu + sec
            if match_sec > avg_sec:
                nb_game_over += 1
                if match.winner() == team:
                    nb_win_over += 1
            else:
                nb_game_under += 1
                if match.winner() == team:
                    nb_win_under += 1
        t_over = nb_win_over/nb_game_over*100 if nb_game_over > 0 else 0.0
        t_under = nb_win_under/nb_game_under*100 if nb_game_under > 0 else 0.0
        return {"Plus que moyenne": t_over, "Moins que moyenne": t_under}

    # === STATS BASKET ===
    def get_3pts_efficiency(self, team: str) -> float:
        """Donne le pourcentage de réussite moyen d'une équipe à 3 points"""
        bons_matchs = [match for match in self.matches if team in [match.team1, match.team2]]
        if not bons_matchs:
            return 0.0
        s_pct = 0
        matches = 0
        for match in bons_matchs:
            if team == match.team1 and "fg3_pct_home" in match.autres:
                s_pct += float(match.autres["fg3_pct_home"])
                matches += 1
            elif team == match.team2 and "fg3_pct_away" in match.autres:
                s_pct += float(match.autres["fg3_pct_away"])
                matches += 1
        return s_pct/matches*100
