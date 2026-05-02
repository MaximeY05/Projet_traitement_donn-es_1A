# Implémentation de la classe Joueur


class Joueur:
    """
    La classe Joueur permet de modéliser un joueur

    Atributes
    ----------
    nom : str
    nationalite : str
    date_naissance : str
    sexe : str
    id : int
    """

    def __init__(
        self,
        nom: str,
        date_naissance: str,
        sexe: str,
        id: int,
        autres: dict,
            ):
        self.nom = nom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.id = id
        self.autres = autres

    def __str__(self) -> str:
        return f"{self.nom}"
