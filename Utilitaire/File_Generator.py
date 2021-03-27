import random

N = 120  # Nombre de Pages
column_emptyratio = 0.95  # Ratio de cases vides sur une ligne de H (1: toute les cases de la ligne correspondante sont vides)
line_emptyratio = 0.05  # Ratio de lignes vides de H (1: toute les lignes de H sont vides)

with open("sources.txt", 'w') as f:
    f.write(str(N)+"\n")
    for i in range(N):
        if random.choices([0, 1], [line_emptyratio, 1-line_emptyratio]) == [1]:
            for j in range(N):
                if random.choices([0, 1], [column_emptyratio, 1-column_emptyratio]) == [1] and i != j:
                    line = f"{i} {j}\n"
                    f.write(line)