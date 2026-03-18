# Implémentation de la classe Joueur

from typing import Any


class Joueur:
    """
    La classe Joueur permet de modéliser un joueur

    Atributes
    ----------
    nom : str
    prenom : str
    nationalite : str
    age : int
    sexe : str
    stats : dict[distinctions: str, nbre: int | float]
    sport : Sport
    id : int 
    """

    def __init__(self):
        self.__nom = None
        self.prenom = None
        self.age = None
        self.sexe = None
        self.stats = None
        self.sport = None
        self.id = None

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"
    
    def modifier_joueur(
            self,
            nom : str,
            prenom : str,
            age : int,
            sexe : str,
            stats : dict[str, int | float],
            sport : list["Sport"],
            id : int
    ) -> None:
        
        self.__nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe
        self.stats = stats
        self.sport = sport
        self.id = id

    def afficher_stat(self) -> None:
        for cle, valeur in (self.stats).items():
            print(f"{cle}: {valeur}")

    def ajouter_stat(self, stat: str, nombre : int) -> None:
        (self.stats)[stat] = nombre
    
    def ajouter_sport(self, sport : "Sport") -> None:
        (self.sport).append(sport)
    
    def suppr_joueur(self) -> None:
        pass






























    def __str__(self) -> str:
        return f"Personne de pseudo {self.__pseudo}"

    def __repr__(self) -> str:
        return f"_Personne({self.__pseudo})"