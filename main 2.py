# #           Задание №1
# #
# # num1 = int(input('Введите число: '))
# # num2 = int(input('Введите число: '))
# #
# # for i in range(num1, num2+1):
# #     if i % 7 == 0:
# #         print(i)
# #
# #           Задание №2
# #
# # num1 = int(input('Введите число: '))
# # num2 = int(input('Введите число: '))
# # count = 0
# #
# # for i in range(num1, num2+1):
# #     print(i, end=', ')
# # print()
# # for i in range(num2, num1-1, -1):
# #     print(i, end=', ')
# # print()
# # for i in range(num1, num2+1):
# #     if i % 7 == 0:
# #         print(i, end=', ')
# #     if i % 5 == 0:
# #         count += 1
# # print()
# # print('Количество делитей на 5:', count)
# #
# #           Задание №3
# #
# # num1 = int(input('Введите число: '))
# # num2 = int(input('Введите число: '))
# #
# # for i in range(num1, num2+1):
# #     if i % 3 == 0 and i % 5 == 0:
# #         print("Fizz Buzz")
# #     elif i % 3 == 0:
# #         print("Fizz")
# #     elif i % 5 == 0:
# #         print("Buzz")
# #     else:
# #         print(i)
# #
# #           Задание №4
# # #
# # num1 = int(input('Введите число: '))
# # num2 = int(input('Введите число: '))
# # even_numbers = 0
# # odd_numbers = 0
# # multiple_of_9 = 0
# # count_even = 0
# # count_odd = 0
# # count = 0
# # for i in range(num1, num2+1):
# #     if i % 2 == 0:
# #         even_numbers += i
# #         count_even += 1
# #     elif i % 2 != 0:
# #         odd_numbers += i
# #         count_odd += 1
# #     if i % 9 == 0:
# #         count += 1
# # print("Сумма чётных: ", even_numbers)
# # print("Среднеарифметическое чётных: ", even_numbers/count_even)
# # print("Сумма нечётных: ", odd_numbers)
# # print("Среднеарифметическое чётных: ", odd_numbers/count_odd)
# # print("Количество цифр кратных 9: ", count)
# #
# #           Задание №5
# #
# # num1 = int(input('Введите число: '))
# # symbol = input('Введите символ для отображения: ')
# # for i in range(num1):
# #     print(symbol)
# #
# #           Задание №6
# #
# # num1 = int(input("Введите число: "))
# # while num1 != 7:
# #     if num1 > 0:
# #         print("Number is positive")
# #     if num1 < 0:
# #         print("Number is negative")
# #     if num1 == 0:
# #         print("Number is equal to zero")
# #     num1 = int(input("Введите число: "))
# # print("Good bye!")
# #
# #           Задание №7
# #
# # num1 = int(input("Введите число: "))
# # min_num = num1
# # max_num = num1
# # sum_numbers = 0
# # while num1 != 7:
# #     sum_numbers += num1
# #     if num1 > max_num:
# #         max_num = num1
# #     if num1 < min_num:
# #         min_num = num1
# #     print("Сумма введеных чисел", sum_numbers)
# #     print("Минимальное введеное число", min_num)
# #     print("Максимальное введеное число", max_num)
# #     num1 = int(input("Введите число: "))
# # print("Good bye!")
# #
# #           Доп задания №1
# #
# # num1 = int(input("Введите число x: "))
# # num2 = int(input("Введите число y: "))
# # degree_digit = num1 ** num2
# # print("x в степени y: ", degree_digit)
# #
# #           Доп задание №2
# #
# # two_digits = 0
# # for i in range(100, 1000):
# #     num1 = i // 100
# #     num2 = i // 10 % 10
# #     num3 = i % 10
# #     count = 0
# #     if num1 == num2:
# #         count += 1
# #     if num1 == num3:
# #         count += 1
# #     if num2 == num3:
# #         count += 1
# #     if count == 1:
# #         two_digits += 1
# # print("Количество 2-х одинаковых цифр: ", two_digits)
# #
# #           Доп задание №3
# #
# # digits = 0
# # for i in range(100, 10000):
# #     if 100 < i < 1000:
# #         num1 = i // 100
# #         num2 = i // 10 % 10
# #         num3 = i % 10
# #         count = 0
# #         if num1 == num2:
# #             count += 1
# #         if num1 == num3:
# #             count += 1
# #         if num2 == num3:
# #             count += 1
# #         if count == 0:
# #             digits += 1
# #     if 1000 < i < 10000:
# #         num1 = i // 1000
# #         num2 = i // 100 % 10
# #         num3 = i // 10 % 10
# #         num4 = i % 10
# #         count = 0
# #         if num1 == num2:
# #             count += 1
# #         if num1 == num3:
# #             count += 1
# #         if num1 == num4:
# #             count += 1
# #         if num2 == num3:
# #             count += 1
# #         if num2 == num4:
# #             count += 1
# #         if num3 == num4:
# #             count += 1
# #         if count == 0:
# #             digits += 1
# # print("Количество комбинаций разных цифр: ", digits)
# #
# #           Доп задание №4
# #
# # num1 = int(input("Введите число: "))
# # num_str = str(num1)
# # new_num = ''
# # for num in num_str:
# #     print(num)
# #     if num != '3' and num != '6':
# #         new_num += num
# # print(int(new_num))
# #
# #           Доп задание №3 (2-ой вариант)
# #
# # digits = 0
# # for i in range(100, 10000):
# #     if 100 < i < 1000:
# #         num1 = i // 100
# #         num2 = i // 10 % 10
# #         num3 = i % 10
# #         count = 0
# #         if num1 != num2 and num1 != num3 and num2 != num3:
# #             digits += 1
# #     if 1000 < i < 10000:
# #         num1 = i // 1000
# #         num2 = i // 100 % 10
# #         num3 = i // 10 % 10
# #         num4 = i % 10
# #         count = 0
# #         if num1 != num2 and num1 != num3 and num1 != num4 and num2 != num3 and num2 != num4 and num3 != num4:
# #             digits += 1
# # print("Количество комбинаций разных цифр: ", digits)
#
# #          Рисунок "e"
# #
# print('Малюнок "e"', end='\n')
#
# for h in range(9):
#     for w in range(9):
#         if h+w <= 8 and h>=w or h+w >= 8 and h<=w:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
# print()

def square(side_length, symbol, log):
    for i in range(side_length):
        for j in range(side_length):
            if log is False:
                if i == 0 or i == side_length-1 or j == 0 or j == side_length-1:
                    print(symbol, end='')
                else:
                    print(" ", end='')
            else:
                print(symbol, end='')
        print()


square(5, '*', True)