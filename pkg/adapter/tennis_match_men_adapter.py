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
        """Convertit une ligne de CSV de tennis en objet Match.

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """
        score_raw = str(row["score"])

        if any(case in score_raw.upper() for case in ["W/O", "RET", "DEF", "WALK"]):
            score_final = (0, -1)
        else:
            s1, s2 = 0, 0
            for s in score_raw.strip().split(" "):
                if "-" in s:
                    try:
                        p = s.split("-")
                        v1 = int("".join(filter(str.isdigit, p[0])))
                        v2 = int("".join(filter(str.isdigit, p[1])))
                        if v1 > v2:
                            s1 += 1
                        elif v2 > v1:
                            s2 += 1
                    except (ValueError, IndexError):
                        continue
            score_final = (s1, s2) if s1 >= s2 else (s2, s1)

        try:
            match_date = datetime.strptime(str(row["tourney_date"]).strip(), "%Y%m%d").date()
        except (ValueError, TypeError):
            match_date = None

        def get_name(player_id):
            data = self.joueurs.get(player_id, {})
            return f"{data.get('name_first', 'Inconnu')} {data.get('name_last', '')}".strip()

        return Match(
            id=None,
            date=match_date,
            team1=get_name(row["winner_id"]),
            team2=get_name(row["loser_id"]),
            score1=score_final[0],
            score2=score_final[1],
            autres={idx: row[idx] for idx in row.index if idx != "tourney_date"}
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
