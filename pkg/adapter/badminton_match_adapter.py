"Adapter pour les matchs de badminton"
from typing import Dict
from datetime import datetime
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class BadmintonMatchAdapter(BaseAdapter):
    """Classe implémentant l'adapter pour les matchs de badminton"""
    def adapt(self, row) -> Match:
        """Convertit une ligne provenant d'un fichier csv lu par pandas en objet python

        Parameters
        ----------
        row: nos données lues par pandas

        Returns
        -------
        Match: objet Match correspondant aux données
        """

        score1 = 0
        score2 = 0

        game1 = row["game_1_score"].split("-")
        if int(game1[0][0]) > int(game1[1][0]):
            score1 += 1
        else:
            score2 += 1

        game2 = row["game_2_score"].split("-")
        if int(game2[0][0]) > int(game2[1][0]):
            score1 += 1
        else:
            score2 += 1

        if score1 == score2:
            game3 = row["game_3_score"].split("-")
            if int(game3[0][0]) > int(game3[1][0]):
                score1 += 1
            else:
                score2 += 1

        return Match(
            id=None,
            date=datetime.strptime(row["date"], "%Y-%m-%d").date(),
            team1=row["player_1"],
            team2=row["player_2"],
            score1=score1,
            score2=score2,
            autres={
                  idx: row[idx] for idx in row.index
                  if idx not in ["date", "player_1", "player_2"]
                }
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
        dico = {
                "player_1": match.team1,
                "player_2": match.team2,
                "date": match.date
                }
        for key, value in match.autres.items():
            dico[key] = value
        return dico
