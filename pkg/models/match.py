"""Implémentation de la classe Match"""
from dataclasses import dataclass, field
from typing import Any
from datetime import datetime


@dataclass
class Match:
    """
    La classe Match permet de modéliser un match

    Atributes
    ----------
    id : int
    date : datetime
    team1 : str
    team2 : str
    score1 : int
    score2 : int
    autres : {str: Any}
    """
    id: int
    date: datetime
    team1: str
    team2: str
    score1: int
    score2: int
    autres: dict[str, Any] = field(default_factory=dict)

    def winner(self):
        """Donne le gagnant d'un match

        Returns
        --------
        str : Gagnant du match
        """
        if self.score1 > self.score2:
            return self.team1
        if self.score2 > self.score1:
            return self.team2
        return None

    def __str__(self):
        return f"{self.date} | {self.team1} {self.score1} - {self.score2} {self.team2}"

    def __repr__(self):
        return (
            f"Match(date='{self.date}', "
            f"team1='{self.team1}', team2='{self.team2}', "
            f"score1={self.score1}, score2={self.score2}')"
        )
