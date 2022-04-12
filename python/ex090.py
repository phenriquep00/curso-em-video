from time import sleep

total_data = {}
name = str(input('Student name: '))
total_data['name'] = name
average = float(input('Student average: '))
total_data['average'] = average
if average >= 7.0:
    total_data['situation'] = 'approved'
else:
    total_data['situation'] = 'reproved'
print('#' * 20)
for k, v in total_data.items():
    print(f'{k} : {v}')
    sleep(.5)
