# Implémentation de la classe Joueur


class Joueur:
    """
    La classe Joueur permet de modéliser un joueur

    Atributes
    ----------
    nom : str
    prenom : str
    nationalite : str
    date_naissance : str
    sexe : str
    id : int
    """

    def __init__(
        self,
        nom: str,
        prenom: str,
        nationalite: str,
        date_naissance: str,
        sexe: str,
        id: int,
        autres: list[str],
            ):
        self.nom = nom
        self.prenom = prenom
        self.nationalite = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.id = id
        self.autres = autres

    def __str__(self) -> str:
        return f"{self.prenom} {self.nom}"
