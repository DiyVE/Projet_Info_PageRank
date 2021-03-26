'''Faire le page rank de la version Numpy'''
import numpy as np #import du module 


alpha=0.85
#Récupérer les données des dictionnaires
dictionnaire_1, dictionnaire_2, nombre_de_pages = dictionnaire() 

#Calculer H
def matrice_H():
  ''' 
  Permet de construire la matrice H
sortie : matrice H (array)
  '''
  H=np.zeros((nombre_de_pages,nombre_de_pages)))# Initialiser une matrice nulle 
  for lignes,i in dictionnaire_1.items(): # Parcourir les clés et les valeurs du dictionnaire
      for colonnes in i: #Parcourir dans les valeurs la liste 
          H[lignes,colonnes]=1/len(i) #Transformer les coefficients nuls 
  print(H)
    
#Calculer S  
def matrice_S():  
  '''Permet de construire la matrice S
    sortie : matrice S (array)
  ''' 
  S=matrice_H() #Initialiser S en H
  for j in range(np.shape(H)[0]): #Parcourir le nombre de lignes de H  
      if np.all(S[j,:] == 0) : #Regarder si toute la ligne est nulle
          S[j,:] = 1/nombre_de_pages #Transfomer cette ligne nulle en 1/nombre de pages
  print(S)
#Calculer les poids par la méthode récursive
pi_0=np.array((nombre_de_pages))#Initialiser un vecteur 

def matrice_G():
  '''Permet de construire la matrice G
  sortie : matrice G 
  '''
  e=np.ones((nombre_de_pages,1))#Initialiser le vecteur e en un vecteur colonnes remplit de 1
  G=alpha*S+((1-alpha)/nombre_de_pages)*(e@e.T) #Faire le calcul avec la formule 
  print(G)

def vecteur_poids(k, G):
  '''Permet de calculer les poids 
  param: k (int)
  param: matrice G (array)
  sortie: vecteur poids trié dans l'ordre décroissant
  '''
    poids=[]
    
    if k==0: #Initialiser le cas terminal 
        return np.full(shape=(1,nombre_de_pages),fill_value=1/nombre_de_pages) #Renvoyer une matrice de taille (1,nombre de pages) avec comme valeur 1/nombre de pages
    else: #Faire le cas général
        return np.dot(vecteur_poids(k-1, G),G) #Renvoyer le produit entre le vecteur poids d'avant et la matrice G
    
    return np.sort(vecteur_poids(150,G))[::-1])#Trier dans l'ordre décroissant 
