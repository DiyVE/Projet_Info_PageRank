import sys
parametres = {'type_execution': '-N', 'alpha': 0.85, 'k': 150, 'epsilon': -1}  # On initialise le dictionnaire parametre avec les valeurs par defaut associés


def recuperer_parametre_utilisateur(ligne_commande):
    ligne_commande = ligne_commande[1:]  # On enlève le premier élément qui correspond au nom du fichier .py
    parametres["nom_fichier_reseaux"] = ligne_commande.pop()  # On lit et on enlève le dernier élément de la liste ligne_commande qui correspond au nom du fichier résaux
    liste_erreurs = []  # Liste contenant toute les erreurs pouvant avoir survenue lors de la saisie
    index_liste_parametre = 0

    while index_liste_parametre < len(ligne_commande):  # Tant que la fin de la liste ligne_commande n'a pas été lue en entier

        if ligne_commande[index_liste_parametre] == '-P' or ligne_commande[index_liste_parametre] == '-N' or ligne_commande[index_liste_parametre] == '-C':
            parametres['type_execution'] = ligne_commande[index_liste_parametre]
        
        elif ligne_commande[index_liste_parametre] == '-A':
            try:
                if 0 < float(ligne_commande[index_liste_parametre+1]) < 1:
                    parametres['alpha'] = ligne_commande[index_liste_parametre+1]
                
                else:
                    liste_erreurs.append("La Valeur de alpha doit être comprise entre 0 et 1")
                index_liste_parametre += 1
            
            except ValueError or IndexError:
                liste_erreurs.append("Aucune valeur de alpha saisie !")
        
        elif ligne_commande[index_liste_parametre] == '-K':
            try:
                if float(ligne_commande[index_liste_parametre+1]) == int(ligne_commande[index_liste_parametre+1]) and float(ligne_commande[index_liste_parametre+1]) > 0:
                    parametres['k'] = ligne_commande[index_liste_parametre+1]
                
                else:
                    if float(ligne_commande[index_liste_parametre+1]) < 0:
                        liste_erreurs.append("La valeur de k doit être positive")
                    
                    if float(ligne_commande[index_liste_parametre+1]) == int(ligne_commande[index_liste_parametre+1]):
                        liste_erreurs.append("La valeur de k doit être entière")
                index_liste_parametre += 1
            
            except ValueError or IndexError:
                liste_erreurs.append("Aucune valeur de k saisie !")
        
        elif ligne_commande[index_liste_parametre] == '-E':
            try:
                if float(ligne_commande[index_liste_parametre+1]) > 0:
                    parametres['epsilon'] = ligne_commande[index_liste_parametre+1]
                
                else:
                    liste_erreurs.append("La valeur de epsilon doit être entière")
                
                index_liste_parametre += 1
            
            except ValueError or IndexError:
                liste_erreurs.append("Aucune valeur de epsilon saisie !")
        else:
            liste_erreurs.append("L'option {} n'a pas été reconnue !".format(ligne_commande[index_liste_parametre]))

        index_liste_parametre += 1
    if len(liste_erreurs) == 0:
        return parametres
    
    else:
        print("Plusieurs erreurs ont été détectés :")
        
        for erreur in liste_erreurs:
            print(f"         - {erreur}")

if __name__ == "__main__":
    print(recuperer_parametre_utilisateur(sys.argv))

