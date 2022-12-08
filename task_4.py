# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k(до 6 степени).* *Значения коэффициентов от -100 до 100
# *Пример:*
#        - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

max_degree = int(input("enter max degree: "))
lst = [random.randint(-3,3) for _ in range(max_degree)]

print(lst)
string = ''
k = len(lst)
for i in lst:
    lit = ''
    if i < 0:
        lit = ' - '
    if i > 0 and string:
        lit = " + "
    if abs(i) == 1: member = lit + f'x^{k}'
    else: member = lit + f'{str(abs(i))}*x^{k}'
    if k == 1: member = str(member[:member.index('^')])
    if i != 0:
        string += member
    k -= 1
string += ' = 0'
for i in string:
    print(i, end = '')

with open ('data.txt', 'w') as data:
    data.write(string)
