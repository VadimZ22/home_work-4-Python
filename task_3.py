# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
from random import random

lst = [int(random() * 10) for _ in range(10)]
print(lst)
lst_temp = []
lst_res = []
for i in lst:
    lst_temp.append(i)
    index = lst.index(i)
    lst.pop(index)
    if i not in lst:
        lst_res.append(i)
    lst.insert(index, i)
    lst_temp.clear()
print(lst_res)

################## alt version #####################
new_lst = []
for i in lst:
    if lst.count(i) == 1:
        new_lst.append(i)
print(new_lst)