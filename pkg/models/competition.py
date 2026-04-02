import Equipe 
import Match


class Competition:

    def __init__(self, id: int, nom: str, equipes: list[Equipe], matchs: list[Match]):
        self.nom = nom
        self.equipes = equipes
        self.matchs = matchs
    

