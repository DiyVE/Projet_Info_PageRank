import sys
from tqdm import tqdm
"""
Module Permettant de gérer toutes les interactions avec les fichiers 
"""


class Fichiers():
    def extraire_donnees_fichier(self, nom_fichier):
        hyperliens = {}
        try:
            with open(nom_fichier, "r") as f:
                lignes = f.readlines()
                N = int(lignes[0])
                for ligne in tqdm(lignes[1:]):
                    elements_ligne = ligne.split()
                    hyperliens.setdefault(int(elements_ligne[0]), set()).add(int(elements_ligne[1]))
            return hyperliens
        except IOError:
            return -1