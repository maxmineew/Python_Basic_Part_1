Задача 1. Космические рейнджеры
#1 Вариант
chatl = int(input('Сколько чатлов? '))

cr = chatl / 2200
print('Это', cr, 'CR')

ship = round(cr * 1 // 0.5)
print('Можно купить', ship, 'кораблей(-я)')

#2 Вариант

Задача 2. Компьютерное зрение

chatl = int(input('Сколько чатлов? '))

cr = float(chatl / 2200)
print('Это', cr, 'CR')

ship = round(cr * 1 // 0.5)
print('Можно купить', ship, 'кораблей(-я)')

print('Введите местоположение фигуры')
x = float(input('По горизонтали: '))
y = float(input('По вертикали: '))

# Координаты квадрата
# cell_x = int(x * 10)
# cell_y = int(y * 10)

if 0.0 < x < 0.8 and 0.0 < y < 0.8:
    print('Фигура находится в клетке ', '(', int(x * 10), ',', int(y * 10), ')')
else:
    print('Клетки с такой координатой не существует.')

Задача 3. Точность и аккуратность

print('Введите местоположение фигуры')
x = float(input('По горизонтали: '))
y = float(input('По вертикали: '))

if 0 < x < 0.8 and 0 < y < 0.8:
    xSquare = int(x * 10)
    ySquare = int(y * 10)
    print('Фигура находится в клетке ', '(', xSquare, ',', ySquare, ')')
    xCentre = xSquare / 10 + 0.05 # Координаты квадрата
    yCentre = ySquare / 10 + 0.05 # Координаты квадрата
    xPosition = round(xCentre - x, 3)
    yPosition = round(yCentre - y, 3)
    print('Поправьте положение фигуры на', '(', xPosition, ',', yPosition, ')')
else:
    print('Клетки с такой координатой не существует.')


