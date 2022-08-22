numbers_list1 = input('Введите числа для списка № 1: ')
numbers_list2 = input('Введите числа для списка № 2: ')
list1 = numbers_list1.split()
list2 = numbers_list2.split()
unique_list = []
repeating_list = []
uniq_list = []
#
common_list = list1 + list2
print('1)', common_list)
#
for i in common_list:
    if i not in unique_list:
        unique_list.append(i)
print('2)', unique_list)
#
for i in list1:
    if i in list2:
        repeating_list.append(i)
print('3)', repeating_list)
#
for i in list1:
    if i not in list2:
        uniq_list.append(i)
for j in list2:
    if j not in list1:
        uniq_list.append(j)
print('4)', uniq_list)
#
list1_min_max = [min(list1), max(list1)]
list2_min_max =[min(list2), max(list2)]
print('5)', 'min, max первого списка:', list1_min_max, 'min, max второго списка:', list2_min_max)