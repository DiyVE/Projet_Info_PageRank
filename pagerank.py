import sys
from Gestion_Utilisateur import Utilisateur
from Gestion_Fichier import Fichiers
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

""")

if Interaction_Utilisateur.recuperer_parametres_utilisateur(sys.argv) != -1:
    if Fichiers.extraire_donnees_fichier(Interaction_Utilisateur.parametres["nom_fichier_reseau"]) == -1:
        Interaction_Utilisateur.liste_erreurs.append("Le fichier {} du répertoire courant n'a pas pu être ouvert".format(Interaction_Utilisateur.parametres["nom_fichier_reseau"]))

if len(Interaction_Utilisateur.liste_erreurs) != 0:
    Interaction_Utilisateur.afficher_les_erreurs()
