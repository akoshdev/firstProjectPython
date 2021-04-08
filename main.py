# import random
#
# number = random.randint(1, 100)
# print(number)
# user_number = None
# count = 0
# levels = {1: 10, 2: 5, 3: 3}
# level = int(input('Viberite uroven slojnosti: '))
# # print(level)
# max_count = levels[level]
#
# while number != user_number:
#     count += 1
#     print(f'Popitka N {count}')
#     user_number = int(input('Vedite chislo: '))
#     if count == max_count:
#         print('Vi proigrali:')
#         break
#     if number == user_number:
#         print('Pobeda')
#         break
#     elif number < user_number:
#         print('Vash chislo bolshe zagadonnogo!')
#     else:
#         print('Vash chislo menshe zagadonnogo!')


import random

a = random.randint(1, 200)
b = random.randint(1, 200)
c = int(input(f'{a} + {b} = '))

if c == (a + b):
    print("Tog'ri:")
else:
    print("No tog'ri:")
