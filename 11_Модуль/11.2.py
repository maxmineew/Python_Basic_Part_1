Задача 1. Ставки на спорт

bet = float(input('Сколько ставим? ')) #1234
ratio = float(input('Какой коэффициент? ')) #1.716
win = bet * ratio
print(round(win, 2))


Задача 2. День рождения

age = float(input('Какой возраст? ')) #5
body_temp = float(input('Какая температура? ')) #36.6

money = round(age * body_temp, 2)

print('Отец подарит сыну', money, 'руб.')


Задача 3. Индекс массы тела

weight = float(input('Введите вес: '))
height = float(input('Введите рост: '))

bmi = round(weight // (height ** 2), 2)

print('Индекс массы тела равен:', bmi)

if bmi < 18.5:
    print('Недобор массы тела.')
elif bmi < 25:
    print('Все нормально).')
elif bmi < 30:
    print('Избыток.')
else:
    bmi >= 30
    print('У вас ожирение(.')