from pkg.adapter.volley_match_men_adapter import VolleyMatchMenAdapter
from pkg.adapter.volley_match_women_adapter import VolleyMatchWomenAdapter
# from pkg.adapter.volley_coach_adapter import VolleyCoachAdapter
# from pkg.adapter.volley_country_adapter import VolleyCountryAdapter
from pkg.adapter.volley_player_men_adapter import VolleyPlayerMenAdapter
from pkg.adapter.volley_player_woman_adapter import VolleyPlayerWomanAdapter
from pkg.adapter.tennis_player_men_adapter import TennisPlayerMenAdapter
from pkg.adapter.tennis_player_women_adapter import TennisPlayerWomenAdapter
from pkg.adapter.tennis_match_men_adapter import TennisMatchMenAdapter
from pkg.adapter.tennis_match_women_adapter import TennisMatchWomenAdapter
from pkg.adapter.basketball_match_adapter import BasketballMatchAdapter
from pkg.adapter.basketball_player_adapter import BasketballPlayerAdapter
from pkg.adapter.basketball_equipe_adapter import BasketballEquipeAdapter
#from pkg.adapter.lol_coach_adapter import LolCoachAdapter
from pkg.adapter.lol_match_adapter import LolMatchAdapter
from pkg.adapter.lol_player_adapter import LolPlayerAdapter
from pkg.adapter.lol_team_adapter import LolTeamAdapter

from pkg.adapter.football_match_adapter import FootballMatchAdapter
"""
from pkg.adapter.foot_country_adapter import FootCountryAdapter
from pkg.adapter.foot_league_adapter import FootLeagueAdapter
from pkg.adapter.foot_player_adapter import FootPlayerAdapter
from pkg.adapter.foot_team_adapter import FootTeamAdapter
"""


class DatasetConfiguration:

    def __init__(self, dataset_path, dataset_sep, adapter):
        self.dataset_path_match = dataset_path
        self.dataset_sep_match = dataset_sep
        self.adapter_match = adapter

"""
volleyball_configuration = DatasetConfiguration(
    dataset_path_match="resources/data/volleyball/match_men.csv",
    dataset_sep_match=",",
    adapter_match=VolleyMatchAdapter(),
)
"""

volleyball_match_men_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/match_men.csv",
    dataset_sep=",",
    adapter=VolleyMatchMenAdapter(),
)

volleyball_match_women_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/match_women.csv",
    dataset_sep=",",
    adapter=VolleyMatchWomenAdapter(),
)
"""
volleyball_coach_men_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/coach_men.csv",
    dataset_sep=",",
    adapter=VolleyCoachAdapter(),
)

volleyball_coach_women_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/coach_women.csv",
    dataset_sep=",",
    adapter=VolleyCoachAdapter(),
)


volleyball_country_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/country.csv",
    dataset_sep=",",
    adapter=VolleyCountryAdapter(),
)
"""

volleyball_player_men_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/player_men.csv",
    dataset_sep=",",
    adapter=VolleyPlayerMenAdapter(),
)

volleyball_player_women_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/player_women.csv",
    dataset_sep=",",
    adapter=VolleyPlayerWomanAdapter(),
)


tennis_match_men_configuration = DatasetConfiguration(
    dataset_path="work/tennis/atp_matches_2024.csv",
    dataset_sep=",",
    adapter=TennisMatchMenAdapter()
)

tennis_match_women_configuration = DatasetConfiguration(
    dataset_path="work/tennis/wta_matches_2024.csv",
    dataset_sep=",",
    adapter=TennisMatchWomenAdapter()
)
tennis_player_men_configuration = DatasetConfiguration(
    dataset_path="work/tennis/atp_players_2024.csv",
    dataset_sep=",",
    adapter=TennisPlayerMenAdapter()
)

tennis_player_women_configuration = DatasetConfiguration(
    dataset_path="work/tennis/wta_players_2024.csv",
    dataset_sep=",",
    adapter=TennisPlayerWomenAdapter()
)

#lol_coach_configuration = DatasetConfiguration(
#    dataset_path="work/league_of_legends/coach.csv",
#    dataset_sep=",",
#    adapter=LolCoachAdapter
#)
lol_match_configuration = DatasetConfiguration(
    dataset_path="work/league_of_legends/match.csv",
    dataset_sep=",",
    adapter=LolMatchAdapter()
)

lol_player_configuration = DatasetConfiguration(
    dataset_path="work/league_of_legends/player.csv",
    dataset_sep=",",
    adapter=LolPlayerAdapter()
)

lol_team_configuration = DatasetConfiguration(
    dataset_path="work/league_of_legends/team.csv",
    dataset_sep=",",
    adapter=LolTeamAdapter()
)
"""
football_league_configuration = DatasetConfiguration(
    dataset_path="work/football/league.csv",
    dataset_sep=",",
    adapter=FootLeagueAdapter
)
"""
football_match_configuration = DatasetConfiguration(
    dataset_path="work/football/match.csv",
    dataset_sep=",",
    adapter=FootballMatchAdapter()
)
"""
football_player_configuration = DatasetConfiguration(
    dataset_path="work/football/player.csv",
    dataset_sep=",",
    adapter=FootPlayerAdapter
)

football_team_configuration = DatasetConfiguration(
    dataset_path="work/football/team.csv",
    dataset_sep=",",
    adapter=FootTeamAdapter
)
"""
basket_match_configuration = DatasetConfiguration(
    dataset_path="work/basketball/game.csv",
    dataset_sep=",",
    adapter=BasketballMatchAdapter()
)

basket_player_configuration = DatasetConfiguration(
    dataset_path="work/basketball/player.csv",
    dataset_sep=",",
    adapter=BasketballPlayerAdapter()
)

basket_team_configuration = DatasetConfiguration(
    dataset_path="work/basketball/team.csv",
    dataset_sep=",",
    adapter=BasketballEquipeAdapter()
)
