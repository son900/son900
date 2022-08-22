from random import randint

#   Задание №1
#
li = [randint(-50, 50) for i in range(21)]
print(li)
li1 = li[:int(len(li)/3)]
li2 = li[int(len(li)/3):int(len(li)/3*2)]
li3 = li[int(len(li)/3*2):]
list1 = []
a = []
print(li1)
print(li2)
print(li3)

def sort_list(li):
    if sum(li) / len(li) > 0:
        list1 = li1 + li2
        print(list1)
        for i in range(len(list1) - 1):
            for j in range(len(list1) - 1 - i):
                if list1[j] > list1[j + 1]:
                    list1[j], list1[j + 1] = list1[j + 1], list1[j]
            a = list1+li3[::-1]
        print(a)
    else:
        list1 = li2 + li3
        for i in range(len(li1) - 1):
            for j in range(len(li1) - 1 - i):
                if li1[j] > li1[j + 1]:
                    li1[j], li1[j + 1] = li1[j + 1], li1[j]
            a = li1+list1[::-1]
        print(a)


sort_list(li)
#
#   Задание №2
rating_list = [randint(1, 12) for i in range(10)]

print('1) ', *rating_list)

def academic_performance(place_on_the_list, new_estimate):
    for i in range(len(rating_list)):
        if i+1 == place_on_the_list:
            rating_list[i] = new_estimate
    print('2) ', *rating_list)


def average_mark(rating_list):
    average = sum(rating_list)/len(rating_list)
    if average >= 10.7:
        print('3) Вы получите степендию')
    else:
        print(f'3) Вы не получите стпендию ваш средний бал: {average} меньше чем 10.7')


def sort_list(rating_list):
    digital = int(input('Введите в каком порядке вам нужны отсортированне оценки по возрстанию: 1, убыванию: 2 : '))
    if digital == 1:
        sort_ascending = sorted(rating_list)
        print('4) ', sort_ascending)
    if digital == 2:
        descending_sort = sorted(rating_list, reverse=True)
        print('4) ', descending_sort)
    else:
        print('Вы ввели не верное значение')


academic_performance(2, 10)
average_mark(rating_list)
sort_list(rating_list)

#   Задание №3
#
list_to_sort = [randint(1, 12) for i in range(10)]
print(list_to_sort)

def advanced_sorting(list_to_sort):
    for i in range(len(list_to_sort) - 1):
        count = 0
        for j in range(len(list_to_sort) - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
                count += 1
        if count == 0:
            break
        print(list_to_sort)


advanced_sorting(list_to_sort)