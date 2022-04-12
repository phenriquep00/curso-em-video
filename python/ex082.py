num = list()
yes_no = 'y'

while True:
    num.append(int(input('Type a value: ')))
    yes_no = str(input('Want to continue? [y/n]: '))
    if 'n' in yes_no:
        break
even_number = list()
odd_number = list()

for n in num:
    if n % 2 == 0:
        even_number.append(n)
    else:
        odd_number.append(n)

print(f'Listed inputs: {num}')

if len(even_number) == 0:
    print('No even numbers added to the list.')
else:
    print(f'Even numbers: {even_number}')

if len(odd_number) == 0:
    print('No odd numbers added to the list.')
else:
    print(f'Odd numbers: {odd_number}')
