#           Модуль 3. Циклы.
#               Часть 4
# Задание 1
#
num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
if num1 == 1:
    print(num1)
for i in range(num1, num2+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
print()

#           Модуль 3. Циклы.
#               Часть 4
# Задание 2
#
for i in range(1, 11):
    for j in range(1, 11):
        product_of_numbers = i * j
        print(f'{i} * {j} = {product_of_numbers}')
print()

#           Модуль 3. Циклы.
#               Часть 4
# Задание 3
#
num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
for i in range(num1, num2+1):
    for j in range(1, 11):
        product_of_numbers = i * j
        print(f'{i} * {j} = {product_of_numbers}')
print()


#           Рисунок "а"
#
print('Малюнок "a"', end='\n')

for h in range(9):
    for w in range(9):
        if w >= h:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#           Рисунок "б"
#
print('Малюнок "б"', end='\n')

for h in range(9):
    for w in range(9):
        if h >= w:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#           Рисунок "в"
#
print('Малюнок "в"', end='\n')

for h in range(9):
    for w in range(9):
        if h+w <= 8 and w >= h:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#           Рисунок "г"
#
print('Малюнок "г"', end='\n')

for h in range(9):
    for w in range(9):
        if h+w >= 8 and h >= w:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#          Рисунок "д"
#
print('Малюнок "д"', end='\n')

for h in range(9):
    for w in range(9):
        if h+w >= 8 and h >= w or h+w <= 8 and w >= h:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#          Рисунок "e"
#
print('Малюнок "e"', end='\n')

for h in range(9):
    for w in range(9):
        if h+w <= 8 and h>=w or h+w >= 8 and h<=w:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#          Рисунок "ж"
#
print('Малюнок "ж"', end='\n')

for h in range(9):
    for w in range(9):
        if h+w <= 8 and h>=w:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#          Рисунок "з"
#
print('Малюнок "з"', end='\n')

for h in range(9):
    for w in range(9):
        if h+w >= 8 and h<=w:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#           Рисунок "и"
#
print('Малюнок "і"', end='\n')

for h in range(9):
    for w in range(9):
        if h+w <= 8:
            print('*', end='')
        else:
            print(' ', end='')
    print()
print()

#           Рисунок "к"
#
print('Малюнок "к"', end='\n')

for h in range(9):
    for w in range(9):
        if h+w >= 8:
            print('*', end='')
        else:
            print(' ', end='')
    print()

