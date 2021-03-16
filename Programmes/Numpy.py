import numpy as np
import time

def dictionnaire(nom_fichier = "fichier.txt"):
    dico_2 = dict()
    dico_1 = dict()
    with open("worm.net", "r") as f:
       N = int(f.readline())
       line = f.readline()
       while line != "":
           formated_line = line.split()
           dico_2.setdefault(int(formated_line[1]), list()).append(int(formated_line[0]))
           dico_1.setdefault(int(formated_line[0]), list()).append(int(formated_line[1])) #initialisation dictionnaire clé : page, valeur : hyperlien
           line = f.readline()
    time.sleep(1)
    return dico_1, dico_2, N

alpha=0.85

dico_1, dico_2, N = dictionnaire()
print(dico_1,dico_2)
#Calcul de H
H=np.zeros((N,N))
for lignes,i in dico_1.items():
    for colonnes in i:
        H[lignes,colonnes]=1/len(i)
print(H)
    
#Calcul de S     
S=H
for j in range(np.shape(H)[0]):  # np.shape(H)[0] = nombre de lignes de H
    if np.all(S[j,:] == 0) :
        S[j,:] = 1/N 
print(S)

#Calcul de G :
e=np.ones((N,1))
G=alpha*S+((1-alpha)/N)*(e@e.T)
print(G)
pi_0=np.array((N))

#Calcul des poids

def vecteur_poids(k, G):
    if k==0:
        return [1/N, 1/N, 1/N, 1/N, 1/N, 1/N]
    else:
        return np.dot(vecteur_poids(k-1, G),G)
print(vecteur_poids(150,G))
