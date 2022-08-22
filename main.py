# weight = int(input('input weight: '))
# height = int(input('input height: '))
# for h in range(height):
#     for w in range(weight):
#         if h == 0 or h == height - 1 or w == 0 or w == weight - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()
#
# number = int(input('input number: '))
# answer = 'Simple'
# for i in range(2, number // 2):
#     if number % i == 0:
#         answer = 'Not simple'
# print(f'This number is {answer}')

# number = int(input('input number: '))
# result = 0
# some_variable = 1
# while number != 0:
#     digit = number % 10
#     number = number // 10
#
#     if digit == 5:
#         continue
#
#     result = result + digit * some_variable
#     some_variable *= 10
#     # print(digit, end='-')
# print(result)


# for h in range(10):
#     for w in range(10 - h):
#         if h == 0 or h == 10 - 1 or w == 0 or w == 10 - h - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#
#     print()

t_line = 4
t_column = 3

print('    a b c d e f g h')
print('    - - - - - - - -')
for line in range(8):
    print(line + 1, end=' |')
    for column in range(8):
        if line == t_line and column == t_column:
            print(' T', end='')
        elif -1>t_line + t_column>1:
            print(' X', end='')
        else:
            print('  ', end='')
    print(f' | {line + 1}')
print('    - - - - - - - -')
print('    a b c d e f g h')
