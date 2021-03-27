import sys
from Gestion_Utilisateur import Utilisateur
from Gestion_Fichier import Fichiers
import Calculs_PageRank_Numpy
from tqdm import tqdm

Interaction_Utilisateur = Utilisateur()
Fichiers = Fichiers()

print(""" 
                     /$$$$$$$                                     /$$$$$$$                      /$$      
                    | $$__  $$                                   | $$__  $$                    | $$      
                    | $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$  /$$$$$$$ | $$   /$$
                    | $$$$$$$/|____  $$ /$$__  $$ /$$__  $$      | $$$$$$$/ |____  $$| $$__  $$| $$  /$$/
                    | $$____/  /$$$$$$$| $$  \ $$| $$$$$$$$      | $$__  $$  /$$$$$$$| $$  \ $$| $$$$$$/ 
                    | $$      /$$__  $$| $$  | $$| $$_____/      | $$  \ $$ /$$__  $$| $$  | $$| $$_  $$ 
                    | $$     |  $$$$$$$|  $$$$$$$|  $$$$$$$      | $$  | $$|  $$$$$$$| $$  | $$| $$ \  $$
                    |__/      \_______/ \____  $$ \_______/      |__/  |__/ \_______/|__/  |__/|__/  \__/
                                        /$$  \ $$                                                        
                                       |  $$$$$$/                                                        
                                        \______/    


                            ******************************************************************
                            | Crée par : Cassandra Mussard & Margot Helias & Clément Ramirez |
                            ******************************************************************


""")

if Interaction_Utilisateur.recuperer_parametres_utilisateur(sys.argv) != -1:
    if Fichiers.extraire_donnees_fichier(Interaction_Utilisateur.parametres["nom_fichier_reseau"]) == -1:
        Interaction_Utilisateur.liste_erreurs.append("Le fichier {} du répertoire courant n'a pas pu être ouvert".format(Interaction_Utilisateur.parametres["nom_fichier_reseau"]))
    else:
        Interaction_Utilisateur.parametres['N'] = Fichiers.N
        Calculs_PageRank_Numpy.retourner_le_pagerank_et_le_vecteurpoids(Interaction_Utilisateur.parametres, Fichiers.hyperliens)
        if Interaction_Utilisateur.parametres['type_execution'] == '-N':
            vecteur_des_poids, pagerank = Calculs_PageRank_Numpy.calculer_le_vecteur_poids(Interaction_Utilisateur.parametres, Fichiers.hyperliens)
            Fichiers.ecrire_donnees_fichier(vecteur_des_poids, pagerank, Interaction_Utilisateur.parametres)
            print("Création du PageRank Terminé !")
        elif Interaction_Utilisateur.parametres['type_execution'] == '-C':
            pass
        else:
            pass

if len(Interaction_Utilisateur.liste_erreurs) != 0:
    Interaction_Utilisateur.afficher_les_erreurs()

print("")
