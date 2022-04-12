# 5 numbers & the bigger&lower numbers
num = []

for v in range(1, 6):
    num.append(int(input(f'Type a integer number for the {v}° position: ')))

print(f'The typed number were:{num}.')
ordered_num = sorted(num)
bigger = ordered_num[4]
lower = ordered_num[0]
index_bigger = num.index(bigger)
index_lower = num.index(lower)
print(f'The biggest number was {bigger}, in the position {index_bigger + 1}.')
print(f'The lowest number was {lower}, in the position {index_lower + 1}.')
