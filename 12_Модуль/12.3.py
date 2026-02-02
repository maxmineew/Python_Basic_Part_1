def aboutWater(price):
    print('Название: КлирВотер')
    print('Производитель: ВодЗавод')
    print('Цена:', price)
aboutWater('25')
aboutWater('30')
aboutWater('40')

print('Задача 2')

import math

def sphereArea(radius):
    print(f'Площадь сферы равна: {float(2 * math.pi * (radius ** 2))} кв.км.')

def sphereVolume(radius):
    print(f'Объем шара равен: {((4 / 3) * math.pi * (radius ** 2))} куб.км.')

sphereArea(6371)
sphereVolume(6371)

print('Задача 3')
# Задача 3. Простые числа
#
# Пользователь вводит число N — количество чисел в последовательности. Напишите программу, которая проверяет,
# сколько из этих чисел являются простыми. Для проверки простоты числа реализуйте функцию isPrime.

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Не простое")
            break
    else:
        print("Простое")

# ** 0.5 - это по сути взятие корня из числа. Нам нет необходимости проверять числа дальше корня, т.к.
# проверив все множители до корня - мы проверим все возможные варианты делимости числа.

n = int(input("Введите количество чисел в последовательности: "))
for i in range(n):
    new_number = int(input("Введите число: "))
    is_prime(new_number)


# В целом с нашими текущими знаниями этого решения достаточно. Посчитать количество придётся вручную.
# Но решим задачку и вторым вариантом с забеганием вперед:

def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


n = int(input("Введите количество чисел в последовательности: "))
count = 0
for i in range(n):
    new_number = int(input("Введите число: "))
    if is_prime(new_number):
        count += 1




