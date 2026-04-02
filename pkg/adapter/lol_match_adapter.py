from typing import Dict
from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.match import Match


class LolMatchAdapter(BaseAdapter):

    def __init__(self):
        super().__init__()

    def adapt(self, row) -> Match:
        """
        Convertit une ligne provenant du fichier match.csv (lu par pandas)
        en un objet python Match.
        """

        return Match(
            patch=row["patch"],
            date=row["date"],
            week=row["week"],
            day=row["day"],
            game_of_day=row["game_of_day"],
            team_blue=row["team_blue"],
            team_red=row["team_red"],
            winner=row["winner"],
            duration=row["time"],
            # Statistiques d'équipe
            stats_blue={
                "kills": row["kills_team_blue"],
                "assists": row["assists_team_blue"],
                "deaths": row["deaths_team_blue"],
                "gold": row["gold_team_blue"],
                "turrets": row["turrets_team_blue"],
                "dragons": row["dragons_team_blue"],
                "barons": row["barons_team_blue"],
            },
            stats_red={
                "kills": row["kills_team_red"],
                "assists": row["assists_team_red"],
                "deaths": row["deaths_team_red"],
                "gold": row["gold_team_red"],
                "turrets": row["turrets_team_red"],
                "dragons": row["dragons_team_red"],
                "barons": row["barons_team_red"],
            },
            # Rôles des joueurs
            composition_blue={
                "top": row["top_team_blue"],
                "jungle": row["jungle_team_blue"],
                "mid": row["mid_team_blue"],
                "bot": row["bot_team_blue"],
                "sup": row["sup_team_blue"],
            },
            composition_red={
                "top": row["top_team_red"],
                "jungle": row["jungle_team_red"],
                "mid": row["mid_team_red"],
                "bot": row["bot_team_red"],
                "sup": row["sup_team_red"],
            },
            # Listes des picks et bans
            picks_blue=[row[f"pick_{i}_team_blue"] for i in range(1, 6)],
            picks_red=[row[f"pick_{i}_team_red"] for i in range(1, 6)],
            bans_blue=[row[f"ban_{i}_team_blue"] for i in range(1, 6)],
            bans_red=[row[f"ban_{i}_team_red"] for i in range(1, 6)]
        )

    def to_row(self, match: Match) -> Dict[str, any]:
        """
        Convertit un objet Match en dictionnaire compatible avec le format du CSV original.
        """
        row = {
            "patch": match.patch,
            "date": match.date,
            "week": match.week,
            "day": match.day,
            "game_of_day": match.game_of_day,
            "team_blue": match.team_blue,
            "team_red": match.team_red,
            "winner": match.winner,
            "time": match.duration,
            # Extraction des stats
            "kills_team_blue": match.stats_blue["kills"],
            "assists_team_blue": match.stats_blue["assists"],
            "deaths_team_blue": match.stats_blue["deaths"],
            "gold_team_blue": match.stats_blue["gold"],
            "turrets_team_blue": match.stats_blue["turrets"],
            "dragons_team_blue": match.stats_blue["dragons"],
            "barons_team_blue": match.stats_blue["barons"],
            "kills_team_red": match.stats_red["kills"],
            "assists_team_red": match.stats_red["assists"],
            "deaths_team_red": match.stats_red["deaths"],
            "gold_team_red": match.stats_red["gold"],
            "turrets_team_red": match.stats_red["turrets"],
            "dragons_team_red": match.stats_red["dragons"],
            "barons_team_red": match.stats_red["barons"],
            # Extraction des compositions
            "top_team_blue": match.composition_blue["top"],
            "jungle_team_blue": match.composition_blue["jungle"],
            "mid_team_blue": match.composition_blue["mid"],
            "bot_team_blue": match.composition_blue["bot"],
            "sup_team_blue": match.composition_blue["sup"],
            "top_team_red": match.composition_red["top"],
            "jungle_team_red": match.composition_red["jungle"],
            "mid_team_red": match.composition_red["mid"],
            "bot_team_red": match.composition_red["bot"],
            "sup_team_red": match.composition_red["sup"],
        }

        # Ajout des picks et bans indexés
        for i in range(5):
            row[f"pick_{i+1}_team_blue"] = match.picks_blue[i]
            row[f"pick_{i+1}_team_red"] = match.picks_red[i]
            row[f"ban_{i+1}_team_blue"] = match.bans_blue[i]
            row[f"ban_{i+1}_team_red"] = match.bans_red[i]

        return row
