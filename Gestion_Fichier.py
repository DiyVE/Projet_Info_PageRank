import sys
from tqdm import tqdm
from progress.bar import IncrementalBar

"""
Module Permettant de gérer toutes les interactions avec les fichiers 
"""


class Fichiers():
    """
    Méthodes
    --------

        extraire_donnees_fichier()

        ecrire_donnees_fichier()
    """
    def extraire_donnees_fichier(self, nom_fichier):
        """
        Paramètres :
        
            nom_fichier (fichier) : nom du fichier dont on va extraire les données

        """

        self.hyperliens = {} #initialiser le dictionnaire
        try:
            with open(nom_fichier, "r") as f: #ouvrir le fichier en mode lecture
                lignes = f.readlines()
                self.N = int(lignes[0])
                # Barre_de_chargement = IncrementalBar("Création du Dictionnaire d'Hyperliens",max = (len(readlines)-1))
                for ligne in lignes[1:]: #parcourir l'ensemble des lignes
                    elements_ligne = ligne.split()
                    self.hyperliens.setdefault(int(elements_ligne[0]), set()).add(int(elements_ligne[1])) #Ajouter les pages et les hyperliens au dictionnaire
            
            print("Création du dictionnaire terminée")
            return self.hyperliens, self.N
        except IOError: #Lever l'exception 
            return -1
    
    #Inscrire les données (pagerank et poids) dans les fichiers
    def ecrire_donnees_fichier(self, vecteur_des_poids, pagerank, parametres): #pourquoi poids
        """
        Paramètres :
            vecteur_des_poids (list) : 
            pagerank (list) : classement des pages 
            paramètres (dict) : Dictionnaire qui contient les paramètres
        """
        with open("{}.prw".format(parametres["nom_fichier_reseau"][:-4]), "w") as f: #ouvrir le fichier "nom_fichier_reseau.prw" en mode écriture
            f.write(f"{self.N} {parametres['alpha']} {parametres['k']}\n") #ecrire les paramètres N, alpha et k 
            for poids in vecteur_des_poids:
                f.write("{}\n".format(poids)) #ecrire les poids dans l'ordre croissant
        with open("{}.pr".format(parametres["nom_fichier_reseau"][:-4]), "w") as f: #ouvrir le fichier "nom_fichier_reseau.pr" en mode écriture
            for page in pagerank:
                f.write("{}\n".format(page)) #ecrire les numéros de pages dans l'ordre croissant