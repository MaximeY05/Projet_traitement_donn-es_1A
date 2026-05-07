"""Fichier de tests pour stats_service"""
from datetime import date
import pytest
from pkg.models.match import Match
from pkg.models.joueur import Joueur
from pkg.services.stats_service import StatsService

# --- FONCTIONS DE PRÉPARATION ---


def preparer_joueurs():
    """Crée une liste de vrais objets Joueur"""
    return [
        Joueur(nom="Lebron", date_naissance="1984-12-30", sexe="M", joueur_id=23,
               autres={"rating_standard": "2800"}),
        Joueur(nom="Jordan", date_naissance="1963-02-17", sexe="M", joueur_id=45,
               autres={"rating_standard": "2900"})
    ]


def preparer_matches():
    """Crée une liste de vrais objets Match avec des données variées"""
    return [
        Match(id=1, date=date(2024, 1, 1), team1="Lakers", team2="Bulls",
              score1=110, score2=100,
              autres={"time": "00:48:00", "fg3_pct_home": 0.4, "surface": "Hard"}),
        Match(id=2, date=date(2024, 1, 5), team1="Lakers", team2="Celtics",
              score1=0, score2=2,
              autres={"time": "01:30:00", "surface": "Hard"}),
        Match(id=3, date=date(2024, 1, 10), team1="Bulls", team2="Lakers",
              score1=80, score2=120,
              autres={"time": "00:52:00", "fg3_pct_away": 0.5, "surface": "Clay"})
    ]

# --- TESTS DU STATS SERVICE ---


def test_compute_ranking():
    """Vérifie que le classement par points (3 pts par victoire) est correct"""
    matches = preparer_matches()
    service = StatsService(matches=matches)

    ranking = service.compute_ranking()

    # Lakers a 2 victoires (Match 1 et 3) -> 6 points
    assert ranking["Lakers"] == 6
    # Celtics a 1 victoire (Match 2) -> 3 points
    assert ranking["Celtics"] == 3


@pytest.mark.parametrize("nom_equipe, taux_attendu", [
    ("Lakers", 66.66),  # 2 victoires sur 3 matchs
    ("Celtics", 100.0),  # 1 victoire sur 1 match
    ("Bulls", 0.0)      # 0 victoire sur 2 matchs
])
def test_get_winrate(nom_equipe, taux_attendu):
    """Vérifie le calcul du pourcentage de victoire"""
    service = StatsService(matches=preparer_matches())
    assert service.get_winrate(nom_equipe) == pytest.approx(taux_attendu, 0.1)


def test_get_average_game_time():
    """Vérifie la moyenne de temps au format MM:SS"""
    service = StatsService(matches=preparer_matches())
    # Moyenne de 48min, 90min (1h30) et 52min -> (48+90+52)/3 = 63 min et 20 sec
    assert service.get_average_game_time() == "63:20"


def test_get_player_by_name():
    """Vérifie qu'on récupère bien le bon objet Joueur"""
    joueurs = preparer_joueurs()
    service = StatsService(joueurs=joueurs)

    j = service.get_player_by_name("Lebron")
    assert j.joueur_id == 23
    assert service.get_player_by_name("Inconnu") is None


def test_get_surface_winrate():
    """Vérifie le winrate par surface pour le Tennis"""
    service = StatsService(matches=preparer_matches())

    # Lakers a joué 2 fois sur "Hard" (1 victoire, 1 défaite) -> 50%
    # Lakers a joué 1 fois sur "Clay" (1 victoire) -> 100%
    stats = service.get_surface_winrate("Lakers")

    assert stats["Dur"] == 50.0
    assert stats["Terre battue"] == 100.0


def test_get_3pts_efficiency():
    """Vérifie l'efficacité au basket"""
    service = StatsService(matches=preparer_matches())

    # Lakers: Match 1 (home) 0.4 + Match 3 (away) 0.5 -> Moyenne 0.45
    assert service.get_3pts_efficiency("Lakers") == 45.0
