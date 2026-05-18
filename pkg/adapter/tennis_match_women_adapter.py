"Adapter pour les matchs de tennis féminins"
from typing import Dict
from datetime import datetime
from pandas import read_csv
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class TennisMatchWomenAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de tennis féminin"""
    def __init__(self):
        self.joueurs = {row["player_id"]: row for _, row in
                        read_csv("work/tennis/wta_players_2024.csv", sep=",").iterrows()}

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

        special_cases = ["W/O", "RET", "DEF", "WALK"]
        if any(case in score_raw.upper() for case in special_cases):
            scorewin = 0
            scorelose = -1
        else:
            score1 = 0
            score2 = 0
            sets = score_raw.strip().split(" ")

            for s in sets:
                if "-" in s:
                    parts = s.split("-")
                    try:
                        s1 = int("".join(filter(str.isdigit, parts[0])))
                        s2 = int("".join(filter(str.isdigit, parts[1][0])))

                        if s1 > s2:
                            score1 += 1
                        elif s2 > s1:
                            score2 += 1
                    except (ValueError, IndexError):
                        continue

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

    def to_row(self, obj: Match) -> Dict[str, any]:
        """Reconvertit l'objet en dictionnaire pour l'export CSV.

        Parameters
        ----------
        obj : Match
            objet à renvoyer

        Returns
        --------
        dict : dictionnaire prêt pour la transition en csv
        """
        dico = {"tourney_date": obj.date}
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
