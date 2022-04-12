matrix = list()
lines = []
for i in range(0, 3):
    for n in range(0, 3):
        lines.append(int(input(f'Type [{i}] [{n}]:')))
    matrix.append(lines[:])
    lines.clear()

print('¬'*30)

for i, n in enumerate(matrix):
    print(matrix[i])
