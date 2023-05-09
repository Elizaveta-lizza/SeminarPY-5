# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите число: '))
b = int(input('Введите степень: '))

def RaiseToPowerRecursive(a, b):
    if b == 1:
        return a
    return RaiseToPowerRecursive(a, b - 1) * a

print(RaiseToPowerRecursive(a, b))