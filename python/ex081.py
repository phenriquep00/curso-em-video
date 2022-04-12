number = list()
yes_no = 'y'
c = int()

while True:
    number.append(int(input('Type a value: ')))
    c += 1
    yes_no = str(input('Want to continue the list of values? [y/n]: '))[0].lower()
    if 'n' in yes_no:
        break

print(f'The amount of typed numbers was {c}')
number.sort(reverse=True)
print(f'The numbers in decreasing order is {number}')

if 5 in number:
    print('The number five was in the number list.')
else:
    print('The number five was not found in the list.')
