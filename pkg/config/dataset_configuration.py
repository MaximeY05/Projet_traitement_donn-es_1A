from pkg.adapter.volley_match_adapter import VolleyMatchAdapter
from pkg.adapter.volley_coach_adapter import VolleyCoachAdapter
from pkg.adapter.volley_country_adapter import VolleyCountryAdapter
from pkg.adapter.volley_player_adapter import VolleyPlayerAdapter
from pkg.adapter.tennis_match_adapter import TennisMatchAdapter
from pkg.adapter.tennis_player_adapter import TennisPlayerAdapter
from pkg.adapter.lol_coach_adapter import LolCoachAdapter
from pkg.adapter.lol_match_adapter import LolMatchAdapter
from pkg.adapter.lol_player_adapter import LolPlayerAdapter
from pkg.adapter.lol_team_adapter import LolTeamAdapter
from pkg.adapter.foot_country_adapter import FootCountryAdapter
from pkg.adapter.foot_league_adapter import FootLeagueAdapter
from pkg.adapter.foot_match_adapter import FootMatchAdapter
from pkg.adapter.foot_player_adapter import FootPlayerAdapter
from pkg.adapter.foot_team_adapter import FootTeamAdapter
from pkg.adapter.basket_game_adapter import BasketGameAdapter
from pkg.adapter.basket_player_adapter import BasketPlayerAdapter
from pkg.adapter.basket_team_adapter import BasketTeamAdapter


class DatasetConfiguration:

    def __init__(self, dataset_path, dataset_sep, adapter):
        self.dataset_path_match = dataset_path
        self.dataset_sep_match = dataset_sep
        self.adapter_match = adapter


<<<<<<< HEAD
volleyball_configuration = DatasetConfiguration(
    dataset_path_match="resources/data/volleyball/match_men.csv",
    dataset_sep_match=",",
    adapter_match=VolleyMatchAdapter(),
)
=======
volleyball_match_men_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/match_men.csv",
    dataset_sep=",",
    adapter=VolleyMatchAdapter(),
)

volleyball_match_women_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/match_women.csv",
    dataset_sep=",",
    adapter=VolleyMatchAdapter(),
)

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

volleyball_player_men_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/player_men.csv",
    dataset_sep=",",
    adapter=VolleyPlayerAdapter(),
)

volleyball_player_women_configuration = DatasetConfiguration(
    dataset_path="work/volleyball/player_women.csv",
    dataset_sep=",",
    adapter=VolleyPlayerAdapter(),
)

tennis_match_men_configuration = DatasetConfiguration(
    dataset_path="work/tennis/atp_matches_2024.csv",
    dataset_sep=",",
    adapter=TennisMatchAdapter
)

tennis_match_women_configuration = DatasetConfiguration(
    dataset_path="work/tennis/wta_matches_2024.csv",
    dataset_sep=",",
    adapter=TennisMatchAdapter
)

tennis_player_men_configuration = DatasetConfiguration(
    dataset_path="work/tennis/atp_players_2024.csv",
    dataset_sep=",",
    adapter=TennisPlayerAdapter
)

tennis_player_women_configuration = DatasetConfiguration(
    dataset_path="work/tennis/wta_players_2024.csv",
    dataset_sep=",",
    adapter=TennisPlayerAdapter
)

lol_coach_configuration = DatasetConfiguration(
    dataset_path="work/league_of_legends/coach.csv",
    dataset_sep=",",
    adapter=LolCoachAdapter
)

lol_match_configuration = DatasetConfiguration(
    dataset_path="work/league_of_legends/match.csv",
    dataset_sep=",",
    adapter=LolMatchAdapter
)

lol_player_configuration = DatasetConfiguration(
    dataset_path="work/league_of_legends/player.csv",
    dataset_sep=",",
    adapter=LolPlayerAdapter
)

lol_team_configuration = DatasetConfiguration(
    dataset_path="work/league_of_legends/team.csv",
    dataset_sep=",",
    adapter=LolTeamAdapter
)

foot_country_configuration = DatasetConfiguration(
    dataset_path="work/football/country.csv",
    dataset_sep=",",
    adapter=FootCountryAdapter
)

foot_league_configuration = DatasetConfiguration(
    dataset_path="work/football/league.csv",
    dataset_sep=",",
    adapter=FootLeagueAdapter
)

foot_match_configuration = DatasetConfiguration(
    dataset_path="work/football/match.csv",
    dataset_sep=",",
    adapter=FootMatchAdapter
)

foot_player_configuration = DatasetConfiguration(
    dataset_path="work/football/player.csv",
    dataset_sep=",",
    adapter=FootPlayerAdapter
)

foot_team_configuration = DatasetConfiguration(
    dataset_path="work/football/team.csv",
    dataset_sep=",",
    adapter=FootTeamAdapter
)

basket_game_configuration = DatasetConfiguration(
    dataset_path="work/basketball/game.csv",
    dataset_sep=",",
    adapter=BasketGameAdapter
)

basket_player_configuration = DatasetConfiguration(
    dataset_path="work/basketball/player.csv",
    dataset_sep=",",
    adapter=BasketPlayerAdapter
)

basket_team_configuration = DatasetConfiguration(
    dataset_path="work/basketball/team.csv",
    dataset_sep=",",
    adapter=BasketTeamAdapter
)
>>>>>>> a3d35420f0cc793cad0e3f2bf230a47d04d3f601
