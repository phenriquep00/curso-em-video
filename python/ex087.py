matrix = []
lines = []
even = []
biggest_second = 0
sum_third = 0

for i in range(0, 3):
    for n in range(0, 3):
        lines.append(int(input(f'Type [{i}] [{n}]: ')))
        if lines[n] % 2 == 0:
            even.append(lines[n])
    matrix.append(lines[:])
    lines.clear()

print('¬'*30)

for i, n in enumerate(matrix):
    print(matrix[i])
print()
print(f'The sum of the even numbers is {sum(even)}')

for i in matrix[1]:
    if i >= biggest_second:
        biggest_second = i
print(f'The biggest numbr in the second line was: {biggest_second}')

for i in range(0, 3):
    sum_third += matrix[i][2]
print(f'The sum of the 3rd column was: {sum_third}')
