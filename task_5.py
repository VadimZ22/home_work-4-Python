# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.*
# Пример:
#             - 2*x² + 4*x + 5 = 0
#             - 5*x² + 2*x + 43 = 0
#             - Результат: 7*x^2 + 6*x + 48 = 0

with open ('file_1.txt', 'r') as data:
    str_1 = str(data.readlines())
str_1 = str_1[2:-2]
a, lit_b, b, lit_c, c = str_1[:-3].split()
b = lit_b + b
c = lit_c + c
print(a, b, c)
a = int(a[:a.index('*')])
b = int(b[:b.index('*')])
c = int(c)
print(a, b, c)

with open ('file_2.txt', 'r') as data:
    str_2 = str(data.readlines())
str_2 = str_2[2:-2]
a_2, lit_b_2, b_2, lit_c_2, c_2 = str_2[:-3].split()
b_2 = lit_b_2 + b_2
c_2 = lit_c_2 + c_2
a_2 = int(a_2[:a_2.index('*')])
b_2 = int(b_2[:b_2.index('*')])
c_2 = int(c_2)
print(type(a_2), b_2, c_2)

a_res = a + a_2
b_res = b + b_2
c_res = c + c_2
result = str(a_res) + "*x^2 + " + str(b_res) + "*x + " + str(c_res) + " = 0"

with open ('file_3.txt', 'w') as data:
    data.write(result)
