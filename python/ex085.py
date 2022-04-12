numbers = list()
prov_lis = list()
even = list()
odd = list()
for i in range(0, 7):
    prov_lis.append(int(input(f'Type the {i+1}° number: ')))
    if prov_lis[i] % 2 == 0:
        even.append((prov_lis[i]))
    else:
        odd.append(prov_lis[i])
numbers.append(even)
numbers.append(odd)

print(numbers[0])
print(numbers[1])
