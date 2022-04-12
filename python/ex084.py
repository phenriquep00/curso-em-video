total_data = []
parameter_data = []
total = 0
weights = []
heaviest_person = []
litest_person = []

while True:

    parameter_data.append(str(input('Type a name: ')))
    parameter_data.append(int(input(f"What's {parameter_data[0]}'s weight? ")))
    weights.append(parameter_data[1])
    total_data.append(parameter_data[:])
    parameter_data.clear()

    total += 1

    call = str(input("Want to add data from other person? [y/n]"))[0].lower()
    if 'n' in call:
        break

weights.sort()
for n in total_data:
    if n[1] == weights[-1]:
        heaviest_person.append(n[0])
    elif n[1] == weights[0]:
        litest_person.append(n[0])

print('=-'*30)
print(f'The total of registered person were {total}')
print(f'The highest weight detected was {weights[-1]}, from the following person(s): {heaviest_person}')
print(f'The lowest weight detected was {weights[0]}, from the following person(s): {litest_person}')
