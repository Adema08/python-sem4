# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

my_string = 'a a a b c a a d c d d'.split()
my_dict = {}
result_str = ''

for i in my_string:
    if i not in my_dict:
        my_dict[i] = 1
        result_str += f'{i} '
    else:
        result_str += f'{i}_{my_dict[i]} '
        my_dict[i] += 1
print(result_str)