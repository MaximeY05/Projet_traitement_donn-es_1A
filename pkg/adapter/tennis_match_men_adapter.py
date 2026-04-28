"Adapter pour les matchs de tennis masculins"
from typing import Dict
from datetime import datetime
from pandas import read_csv
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class TennisMatchMenAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de tennis masculin"""
    def __init__(self):
        self.joueurs = {row["player_id"]: row for _, row in
                        read_csv("work/tennis/atp_players_2024.csv", sep=",").iterrows()}

    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """

        score_raw = str(row["score"])

        # 1. Gestion des cas particuliers (Abandon, Forfait, etc.)
        # On regarde si l'un des mots clés est présent n'importe où dans le score
        special_cases = ["W/O", "RET", "DEF", "WALK"]
        if any(case in score_raw.upper() for case in special_cases):
            scorewin = 0
            scorelose = -1
        else:
            score1 = 0
            score2 = 0
            # On nettoie les espaces et on sépare les sets
            sets = score_raw.strip().split(" ")

            for s in sets:
                if "-" in s:
                    # On sépare le score du set (ex: "6-4")
                    parts = s.split("-")
                    try:
                        # On utilise isdigit() pour être sûr, ou on gère l'exception
                        # Note : on prend l'élément complet parts[0], pas juste [0][0]
                        # pour gérer les scores comme 10-8
                        s1 = int("".join(filter(str.isdigit, parts[0])))
                        s2 = int("".join(filter(str.isdigit, parts[1])))

                        if s1 > s2:
                            score1 += 1
                        elif s2 > s1:
                            score2 += 1
                    except (ValueError, IndexError):
                        continue  # Si un set est mal formé, on passe au suivant

            scorewin, scorelose = (score1, score2) if score1 >= score2 else (score2, score1)

        return Match(
            id=None,
            date=datetime.strptime(str(row["tourney_date"]), "%Y%m%d").date(),
            team1=self.joueurs[row["winner_id"]]["name_first"] +
            " " + self.joueurs[row["winner_id"]]["name_last"],
            team2=self.joueurs[row["loser_id"]]["name_first"] +
            " " + self.joueurs[row["loser_id"]]["name_last"],
            score1=scorewin,
            score2=scorelose,
            autres={idx: row[idx] for idx in row.index if idx not in ["tourney_date"]}
        )

    def to_row(self, match: Match) -> Dict[str, any]:
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        match : Match
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {"tourney_date": match.date}
        for key, value in match.autres.items():
            dico[key] = value
        return dico
