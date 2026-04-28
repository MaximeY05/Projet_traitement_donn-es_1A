"Adapter de base pour tous les autres selon les sports etc"
from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    """Classe implémentant l'adapter qui sert de base"""
    @abstractmethod
    def adapt(self, row):
        """Méthode abstraite pour convertir les lignes lues par pandas en objet python"""
        raise NotImplementedError

    @abstractmethod
    def to_row(self, match):
        """Méthode abstraite pour reconvertir les objets python afin de les remettre en csv"""
        raise NotImplementedError
