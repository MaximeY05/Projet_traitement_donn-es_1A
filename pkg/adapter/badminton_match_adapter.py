"Adapter pour les matchs de badminton"
from typing import Dict
from datetime import datetime
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class BadmintonMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de badminton"""
    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv en objet Match."""
        score1 = 0
        score2 = 0

        for i in range(1, 4):
            score_game = str(row.get(f"game_{i}_score", "")).strip().lower()

            if i == 3 and score1 != score2:
                break

            if score_game and score_game != "nan":
                try:
                    p1_set, p2_set = map(int, score_game.split("-"))
                    if p1_set > p2_set:
                        score1 += 1
                    else:
                        score2 += 1
                except (ValueError, IndexError):
                    continue

        try:
            date_str = str(row.get('date', '')).split(' ', maxsplit=1)[0]
            match_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except (ValueError, TypeError, IndexError):
            match_date = None

        return Match(
            id=None,
            date=match_date,
            team1=row.get("player_1", "Inconnu"),
            team2=row.get("player_2", "Inconnu"),
            score1=score1,
            score2=score2,
            autres={idx: row[idx] for idx in row.index if idx not in ["date",
                                                                      "player_1", "player_2"]}
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
        dico = {
                "player_1": obj.team1,
                "player_2": obj.team2,
                "date": obj.date
                }
        for key, value in obj.autres.items():
            dico[key] = value
        return dico
