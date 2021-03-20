import time
import numpy as np
from tqdm import tqdm
import cProfile
dico = dict()
dico2 = dict()

alpha = 0.85

with open("brainlinks.net", "r") as f:
    lines = f.readlines()
    N = int(lines[0])
    for line in tqdm(lines[1:]):
        formated_line = line.split()
        if int(formated_line[0]) not in dico:
            dico[int(formated_line[0])] = set()
        dico.get(int(formated_line[0])).add(int(formated_line[1]))
        if int(formated_line[1]) not in dico2:
            dico2[int(formated_line[1])] = set()
        dico2.get(int(formated_line[1])).add(int(formated_line[0]))


"""
dico = {0 : set([1, 2]), 1 : set([0, 1, 2, 3, 4 ,5]), 2 : set([0, 1, 4]), 3 : set([4, 5]), 4 : set([3, 5]), 5 : set([3])}
dico2 = {0 : set([1, 2]), 1 : set([1, 0, 2]), 2 : set([1, 0]), 3 : set([1, 4, 5]), 4 : set([1, 2, 3]), 5 : set([1, 3, 4])}
"""

"""
        f 0 1
        0 0 0
        1 1 0
"""
ite = 0
vide = set(range(N)) - set(dico.keys())

def vecteur_poids(k):
    if k==0:
        return [1/N]*N
    else:
        vect_plus = [0]*N
        vect = vecteur_poids(k-1)
        for i in range(N) :
            vectbis = list(vect)
            for j in dico2.get(i, ()) :
                #print(((1/len(dico[j])*alpha + (1-alpha)/N))*vectbis[j])
                vect_plus[i] += ((1/len(dico[j])*alpha + (1-alpha)/N))*vectbis[j]
                vectbis[j] = 0
            for j in vide :
                vect_plus[i] += (1/N)*vectbis[j]
                vectbis[j] = 0
            vect_plus[i] += ((1-alpha)/N)*sum(vectbis)
        return vect_plus

vect_plus = vecteur_poids(150)
vect_plus.sort(reverse=True)
print(vect_plus)

