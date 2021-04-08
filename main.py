import random

number = random.randint(1, 100)
print(number)
user_number = None
count = 0
max_count = 3

while number != user_number:
    count += 1
    print(f'Popitka N {count}')
    user_number = int(input('Vedite chislo: '))
    if count == max_count:
        print('Vi proigrali:')
        break
    if number == user_number:
        print('Pobeda')
        break
    elif number < user_number:
        print('Vash chislo bolshe zagadonnogo!')
    else:
        print('Vash chislo menshe zagadonnogo!')
