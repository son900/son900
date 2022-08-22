#           Модуль 4. Функции.
#          Тема: Функции. Часть 2
#
# # Задание 1
def product_of_numbers(*args):
    product = 1
    for i in args:
        product *= i
    print('1)', f'Product of elements: {product}')


product_of_numbers(5, 6, 7, 8, 9)
#
# # Задание 2
def func_min_numbers(*args):
    min_numbers = min(args)
    print('2)', f'Минимальное число из введеных: {min_numbers}')


func_min_numbers(10, 9, 8, 15, 20)
#
# # Задание 3
def prime_numbers(*args):
    count = 0
    for i in args:
        if 1 <= i <= 3:
            count += 1
        else:
            elem = 0
            for j in range(2, int(i / 2)+1):
                if i % j == 0:
                    elem +=1
            if elem == 0:
                count += 1
    print('3)', f'Количество простых чисел: {count}')


prime_numbers(2, 4, 9, 7, 8)
#
# # Задание 4
def func_del_number(list_numbers, numbers_del):
    list_numbers1 = list_numbers.split()
    numbers_del1 = numbers_del.split()
    count = 0
    for i in numbers_del1:
        while i in list_numbers1:
            list_numbers1.remove(i)
            count += 1
    print('4)', f'Количество удаленных чисел: {count}')


func_del_number(input('Введите список чисел: '), input('Введите список для удаления: '))


#Сначало не правьно понял задание

# # Задание 5
# def repeating_elements(list_number_one, list_number_two):
#     list1 = list_number_one.split()
#     list2 = list_number_two.split()
#     repeating_list = []
#     for i in list1:
#         if i is not list2:
#             repeating_list.append(i)
#     for j in list2:
#         if j is not list1:
#             repeating_list.append(j)
#     unique_list = list(set(repeating_list))
#     print('5)', f'Общий список: {unique_list}')
#
#
# repeating_elements(input(), input())

# Задание 5
def repeating_elements(list_number_one, list_number_two):
    list1 = list_number_one.split()
    list2 = list_number_two.split()
    general_list = list1 + list2
    print('5)', f'Общий список: {general_list}')


repeating_elements(input('Введите числа для списка №1: '), input('Введите числа для списка №2: '))
#
# Задание 6
def exponentiation(list_of_numbers, degree_of):
    list = list_of_numbers.split()
    list_of_numbers_in_exponent = []
    for i in list:
        list_of_numbers_in_exponent.append(int(i) ** int(degree_of))
    print('6)', f'Новый список возведденый в {degree_of} степень: {list_of_numbers_in_exponent}')


exponentiation(input('Введите список чисел: '), input('Введите степень возведения: '))