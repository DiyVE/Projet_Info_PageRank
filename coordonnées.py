
import numpy as np

import time
dico = dict()
dictionnaire = dict()
alpha = 0.85
with open("fichier1.txt", "r") as f:
   N = int(f.readline())
   line = f.readline()
   while line != "":
       formated_line = line.split()
       dictionnaire[(int(formated_line[0]),int(formated_line[1]))] = list() #colonne; ligne
       if int(formated_line[0]) not in dico:
           dico[int(formated_line[0])] = list()
       dico.get(int(formated_line[0])).append(int(formated_line[1]))
       line = f.readline()
time.sleep(1)

for i in dico.keys():
    for tuple in dictionnaire:
        if i == tuple[0]:
            dictionnaire[tuple]=alpha/len(dico[i])+(1-alpha)/N
print(dictionnaire)

#calcul du vecteur poids
vecteur_poids = []
s=0
i=0
s1=0
alpha=0.85
k=150 
a=0
ligne_non_nulle=0


for i in range(N):
    for clé in dictionnaire.keys():
        if i == clé[1] :
            s += dictionnaire[clé]*1/N
        ligne_non_nulle+=1
    s+=(1-alpha)*(N-i)/N**2
    vecteur_poids.append(s)
    s=0   
print(ligne_non_nulle)


#initialiser vecteur poids
for i in range(k):
    for clé in dictionnaire.keys():
        if i == clé[1] :
            s+= dictionnaire[clé]*vecteur_poids[clé[0]]
            ligne_non_nulle+=1
    s+=(1-alpha)*(N-i)/N**2
    vecteur_poids.append(s)
    s=0   
print(ligne_non_nulle)
print(vecteur_poids)
