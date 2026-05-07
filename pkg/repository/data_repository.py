"""Implémentation de la classe pour l'import et l'export des bases de données"""
from typing import Any
from pandas import read_csv, DataFrame


class DataRepository:
    """Classe s'occupant de l'import et de l'export des bases de données"""
    def __init__(self, file, adapter, sep=","):
        self.adapter = adapter
        self.file = file
        self.sep = sep
        self.df = None

    def load(self) -> [Any]:
        """Permet de charger une base

        Returns
        --------
        [Any] : liste avec chaque ligne du CSV originel
        """
        self.df = read_csv(self.file, sep=self.sep)
        return [self.adapter.adapt(row) for _, row in self.df.iterrows()]

    def save(self, objects: list):
        """Renvoie la base de données modifiée en CSV

        Parameters
        ----------
        objects : list
        """
        rows = [self.adapter.to_row(obj) for obj in objects]
        df = DataFrame(rows)
        df.to_csv(self.file, index=False)
