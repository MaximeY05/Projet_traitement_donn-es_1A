# Implématation de la classe permettant l'import des données

import pandas as pd

#from .sport import Sport


class Import():
    """Classe permattant la gestion des imports"""
    def __init__(self, sport: Sport, donnee: str) -> None:
        if not isinstance(sport, Sport) or not isinstance(donnee, str):
            raise TypeError("sport et donnee doivent être des chaines de caractères")
        if sport not in {"football", "volleyball", "basketball", "league_of_legends", "tennis"}:
            raise ValueError("Le sport n'est pas dans la base de données")
        if sport == "football" and donnee not in {"country", "league", "match", "player", "team"}:
            raise ValueError("Ces données ne sont pas dans la base de données")
        if sport == "tennis" and donnee not in {"atp_matches_2024", "atp_players_2024",
                                                "wta_matches_2024", "wta_players_2024"}:
            raise ValueError("Ces données ne sont pas dans la base de données")
        if sport == "league_of_legends" and donnee not in {"coach", "match", "player", "team"}:
            raise ValueError("Ces données ne sont pas dans la base de données")
        if sport == "basketball" and donnee not in {"game", "player", "team"}:
            raise ValueError("Ces données ne sont pas dans la base de données")
        if sport == "volleyball" and donnee not in {"coach_men", "coach_women", "country",
                                                    "match_men", "match_women", "player_men",
                                                    "player_women"}:
            raise ValueError("Ces données ne sont pas dans la base de données")
        self.sport: Sport = sport
        self.donnee: str = donnee
        self.bdd = pd.read_csv(f"Projet_traitement_donn-es_1A/work/{sport}/{donnee}.csv")

    def enregistre_modif(self) -> None:
        self.bdd.to_csv(f"Projet_traitement_donn-es_1A/work/{self.sport}/{self.donnee}.csv",
                        index=False, sep=",", encoding="utf-8")
    

print(type(pd.read_csv("Projet_traitement_donn-es_1A/work/foot/country.csv")))