# Вычислить число ПИ c заданной точностью d
#     *Пример:*
#     - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10
import math
p = math.pi
d = input("precision: ")
num_count = d.split('.')[1]
print(num_count)
print(p)
p = str(p)
print(p[:2+len(num_count)])
