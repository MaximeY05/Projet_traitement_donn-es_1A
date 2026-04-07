from pkg.adapter.base_adapter import BaseAdapter
from pkg.models.joueur import Joueur
from pkg.repository.data_repository import DataRepository


class JoueurService:

    def __init__(self, repository: DataRepository, adapter: BaseAdapter):
        self.repository = repository
        self.joueurs = repository.load()

    def create_joueur(
        self,
        nom: str,
        prenom: str,
        date_naissance: str,
        sexe: str,
            ):

        joueur = Joueur(
            nom,
            prenom,
            date_naissance,
            sexe,
        )
        self.joueurs.append(joueur)
        self.repository.save(self.joueurs)

        return joueur

    def display_joueurs(self):
        joueurs = self.repository.load()
        print(joueurs)
