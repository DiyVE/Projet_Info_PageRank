
import numpy as np

#Calculer H
def matrice_H(N, hyperliens): 
    ''' 
    Permet de construire la matrice H

    Paramètres
    ----------
    N: nombre de pages (int)
    hyperliens (dict)

    Sortie : matrice H (array)
    
    '''
    H=np.zeros((N,N)) 
    for lignes,i in hyperliens.items(): 
        for colonnes in i: 
            H[lignes,colonnes]=1/len(i)
    return H

#Calculer S
def matrice_S(H, N):  
    '''Permet de construire la matrice S

    Paramètres
    ----------
    H (array)
    N: nombre de pages (int)

    Sortie : matrice S (array)
    ''' 
    S=H 
    for j in range(np.shape(H)[0]):   
        if np.all(S[j,:] == 0) : 
            S[j,:] = 1/N 
    return S

#Calculer G
def matrice_G(S, parametres):
    '''Permet de construire la matrice G

    Paramètres
    ----------
    N: nombre de pages (int)
    parametres: (dict)
    matrice S:  (array)

    Sortie : matrice G (array)
    '''
    e=np.ones((parametres['N'],1))
    G=parametres['alpha']*S+((1-parametres['alpha'])/parametres['N'])*(e@e.T)
    return G

#Calculer le vecteur poids à partir de la matrice G
def vecteur_poids(G, parametres):
    '''Permet de calculer les poids 

    Paramètres
    ----------
    parametres (dict)
    G (array)

    Sortie: vecteur poids trié dans l'ordre décroissant
    '''

    vecteur_des_poids=dict()
    piplus = np.full(shape=(1,parametres['N']),fill_value=1/parametres['N'])
    epsiloncalc = 1
    k=0
    while epsiloncalc > parametres['epsilon'] and k < parametres['k']:
        pi = piplus
        piplus = np.dot(pi,G)
        epsiloncalc = np.max(piplus - pi)
        k += 1

    liste_des_poids = list(piplus)
    for i in range(parametres['N']):
        vecteur_des_poids[i] = piplus[0][i]
    
    return vecteur_des_poids
     

def calculer_le_vecteur_poids(parametres, hyperliens): #+trouver N
    ''' 
    Calculer le vecteur poids à partir des matrices H, S et G
    
    Paramètres :
    ----------
       parametres (dict)
       hyperliens(dict)

    Sortie : vecteur poids trié dans l'ordre décroissant

        
    '''
    N = parametres['N']
    H = matrice_H(N, hyperliens)
    S = matrice_S(H, N)
    G = matrice_G(S, parametres)
    pi = vecteur_poids(G, parametres) #à revoir

    pi = dict(sorted(pi.items(), key=lambda item: item[1], reverse=True))#attention faire tri décroissant #classer les poids du dictionnaire par ordre décroissant

    vecteur_des_poids = list(pi.values())
    pagerank = list(pi.keys())

    return vecteur_des_poids, pagerank
    #return vecteur_poids(150,G)

#Retourner le PageRank 
def calculer_pagerank(vecteur_des_poids):
    ''' 
    Calculer le PageRank

    Paramètre
    ---------
    vecteur_des_poids (dict) 

    Sortie : pagerank; classement des pages par poids décroissant
    
    '''
    #afficher liste des clés
    return vecteur_des_poids

#Retourner le pagerank et le vecteur poids
def retourner_le_pagerank_et_le_vecteurpoids(parametres, hyperliens):
    ''' 
    Retourner le pagerank et le vecteur poids

    Paramètres
    ----------
    parametres (dict)
    hyperliens (dict)

    Sortie : vecteur_poids et pagerank
    
    '''
    vecteur_poids = calculer_le_vecteur_poids(parametres, hyperliens)
    pagerank = calculer_pagerank(vecteur_poids)
    
    return vecteur_poids, pagerank