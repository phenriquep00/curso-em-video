# putting stuff in position without sort()/sorted()

num = list()

for numbers in range(1, 6):
    num.append(int(input('Type a number: ')))
    if len(num) == 1:
        print(f'The value {num[0]} was added on the last position.')

    if len(num) == 2:
        if num[1] < num[0]:
            num.reverse()
            print(f'The value {num[1]} was added on the first position.')
        else:
            print(f'The value{num[1]} was added on the last position.')

    if len(num) == 3:
        if num[0] < num[2] < num[1]:
            num.insert(1, num[2])
            num.pop()
            print(f'The value {num[1]} was added to the second position.')
        elif num[2] < num[0]:
            num.insert(0, num[2])
            num.pop()
            print(f'The value {num[0]} was added to the first position.')
        else:
            print(f'The value {num[2]} was added on the last position.')

    if len(num) == 4:
        if num[3] < num[0]:
            num.insert(0, num[3])
            num.pop()
            print(f'The value {num[0]} was added on the first position.')
        elif num[0] < num[3] < num[1]:
            num.insert(1, num[3])
            num.pop()
            print(f'The value {num[1]} was added on the second position.')
        elif num[1] < num[3] < num[2]:
            num.insert(2, num[3])
            num.pop()
            print(f'The value {num[2]} was added in the third position.')
        else:
            print(f'The value {num[3]} was added on the last position.')

    if len(num) == 5:
        if num[4] < num[0]:
            num.insert(0, num[4])
            num.pop()
            print(f'The value {num[0]} was added in the first position.')
        elif num[0] < num[4] < num[1]:
            num.insert(1, num[4])
            num.pop()
            print(f'The value {num[1]} was added in the second position.')
        elif num[1] < num[4] < num[2]:
            num.insert(2, num[4])
            num.pop()
            print(f'The value {num[2]} was added on the third position.')
        elif num[2] < num[4] < num[3]:
            num.insert(3, num[4])
            num.pop()
            print(f'The value {num[3]} was added on the forth position.')
        else:
            print(f'The value {num[4]} was added at the last position.')
print(num)
