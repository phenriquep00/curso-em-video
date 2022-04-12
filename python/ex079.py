# unique values on a list
number_list = list()
yes_no = 'y'

while True:
    number_list.append(int(input('Type a number: ')))
    for c in number_list:
        if number_list.count(c) != 1:
            print('Current number is already in the list, was not added!')
            number_list.pop()
    yes_no = str(input('Want to continue? [y/n]: '))[0].lower()
    if yes_no == 'n':
        break

print(sorted(number_list))
