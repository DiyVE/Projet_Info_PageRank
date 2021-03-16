import time
dico = dict()
alpha = 0.85

with open("worm.net", "r") as f:
    N = int(f.readline())
    line = f.readline()
    while line != "":
        formated_line = line.split()
        if int(formated_line[0]) not in dico:
            dico[int(formated_line[0])] = set()
        dico.get(int(formated_line[0])).add(int(formated_line[1]))
        line = f.readline()
time.sleep(1)
print(dico)

G = [([(1-alpha)/N]*N) for i in range(N)]

for i in range(N):
    if i not in dico :
        G[i] = [1/N]*N
    else :
        taille = len(dico.get(i))
        for page in dico[i]:
            G[i][page] = (1/taille)*alpha + (1-alpha)/N


pi_n = []*N
pi_n_plus_1 = [1/N]*N
ite = 0
for k in range(10):
    ite += 1
    pi_n = list(pi_n_plus_1)
    tps1 = time.time()
    for i in range(N):
        somme = 0
        for j in range(N):
            somme += pi_n[j]*G[j][i]
        pi_n_plus_1[i] = somme
    tps2 = time.time()
    print(tps2 - tps1)
print(pi_n, ite)
