import sys
import terminal

class Utilisateur():
    def __init__(self):
        self.parametres = {'type_execution': '-N', 'alpha': 0.85, 'k': 150, 'epsilon': -1}  # On initialise le dictionnaire paramètre avec les valeurs par defaut associées
        self.liste_erreurs = []  # Liste contenant toute les erreurs pouvant avoir survenue lors de la saisie

    def recuperer_parametres_utilisateur(self, ligne_commande):
        ligne_commande = ligne_commande[1:]  # On enlève le premier élément qui correspond au nom du fichier .py
        try:
            self.parametres["nom_fichier_reseau"] = ligne_commande[-1]  # On lit le dernier élément de la liste ligne_commande qui correspond au nom du fichier réseau
        except IndexError:
            self.liste_erreurs.append("Le nom du fichier réseau n'a pas été donné")
        index_liste_parametre = 0

        while index_liste_parametre < len(ligne_commande)-1:  # Tant que la fin de la liste ligne_commande n'a pas été lue en entier (sans compter le fichier)

            if ligne_commande[index_liste_parametre] == '-P' or ligne_commande[index_liste_parametre] == '-N' or ligne_commande[index_liste_parametre] == '-C':
                self.parametres['type_execution'] = ligne_commande[index_liste_parametre]

            elif ligne_commande[index_liste_parametre] == '-A':
                try:
                    if 0 < float(ligne_commande[index_liste_parametre+1]) < 1:
                        self.parametres['alpha'] = ligne_commande[index_liste_parametre+1]

                    else:
                        self.liste_erreurs.append("La valeur de alpha doit être comprise entre 0 et 1")
                    index_liste_parametre += 1

                except ValueError or IndexError:
                    self.liste_erreurs.append("Aucune valeur de alpha saisie !")

            elif ligne_commande[index_liste_parametre] == '-K':
                try:
                    if float(ligne_commande[index_liste_parametre+1]) == int(ligne_commande[index_liste_parametre+1]) and float(ligne_commande[index_liste_parametre+1]) > 0:
                        self.parametres['k'] = ligne_commande[index_liste_parametre+1]

                    else:
                        if float(ligne_commande[index_liste_parametre+1]) < 0:
                            self.liste_erreurs.append("La valeur de k doit être positive")

                        if float(ligne_commande[index_liste_parametre+1]) == int(ligne_commande[index_liste_parametre+1]):
                            self.liste_erreurs.append("La valeur de k doit être entière")
                    index_liste_parametre += 1

                except ValueError or IndexError:
                    self.liste_erreurs.append("Aucune valeur de k saisie !")

            elif ligne_commande[index_liste_parametre] == '-E':
                try:
                    if float(ligne_commande[index_liste_parametre+1]) > 0:
                        self.parametres['epsilon'] = ligne_commande[index_liste_parametre+1]

                    else:
                        self.liste_erreurs.append("La valeur de epsilon doit être entière")

                    index_liste_parametre += 1

                except ValueError or IndexError:
                    self.liste_erreurs.append("Aucune valeur de epsilon saisie !")
            else:
                self.liste_erreurs.append("L'option {} n'a pas été reconnue !".format(ligne_commande[index_liste_parametre]))

            index_liste_parametre += 1
        if len(self.liste_erreurs) == 0:  # Si aucune erreur n'a été détectée
            return 1

        else:
            return -1

    def afficher_les_erreurs(self):
        print("/!\ Plusieurs erreurs ont été détectées :\n")
        for erreur in self.liste_erreurs:  # Affiche les erreurs enregistrées
            print(terminal.red(f"         - {erreur}"))
        print("\nLa génération des fichiers de sortie ne peut aboutir.\nAfin de corriger vos erreurs veuillez consulter l'aide en tapant <....py --help>")
