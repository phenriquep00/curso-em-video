total_data = []
prov_data = []
grades = []
specific = int()
while True:
    prov_data.append(str(input('Name: ')))
    grades.append(float(input('Grade 1: ')))
    grades.append((float(input('Grade 2: '))))
    prov_data.append(grades[:])
    total_data.append(prov_data[:])
    prov_data.clear()
    grades.clear()

    ask = str(input("Want to continue? [y/n] "))[0].lower()
    if 'n' in ask:
        print('¬'*30)
        print('N°   NAME:        AVERAGE:')
        print('-'*25)
        for n, a in enumerate(total_data):
            print(f'{total_data.index(total_data[n])}   {total_data[n][0]}        {((sum(total_data[n][1])) / 2)}')

        specific = int(input('Show the grade of a specific student? [use the student number]: {999 to interrupt}'))
        while specific != 999:
            print(f'{total_data[specific]}')
            specific = int(input('Show the grade of another student? {999 to interrupt}: '))
        else:
            break
