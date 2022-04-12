expression = str(input('Type a mathematical expression: '))
broke_ex = list(expression)
open_parenthesis = 0
closed_parenthesis = 0

for character in broke_ex:
    if character == '(':
        open_parenthesis += 1
    elif character == ')':
        closed_parenthesis += 1

if broke_ex[0] == ')':
    print('broke expression.')
elif broke_ex[-1] == '(':
    print('broke expression.')
elif open_parenthesis != closed_parenthesis:
    print('broke expression.')
else:
    print('expression checks out.')
