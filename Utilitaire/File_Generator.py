from numpy import random
N = 6
it = 6

with open("sources.txt", 'w') as f:
    f.write(str(N)+"\n")
    for i in range(it):
        f.write(str(random.randint(0, N)) + " " + str(random.randint(0, N)) + "\n")
