# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N. (Выполнили на семинаре)


def Find_Mult(num):
    mult = []
    div = 2
    while num > 1:
        while num % div == 0:
            mult.append(div)
            num /= div
        div += 1
    return mult

number = int(input("enter a natural number: "))
print(Find_Mult(number))