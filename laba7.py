# Определить функцию для обработки пользовательского ввода и проверки ошибок
def get_input(prompt, error_message, range_min=0, range_max=8):
    while True:
        try:
            value = int(input(prompt))
            if range_min <= value <= range_max:
                return value
            else:
                print(error_message)
        except ValueError:
            print('Введены некорректные данные. Попробуйте снова.')

# Основной цикл
while True:

    # Ввод данных с проверкой на ошибки
    horizontal = get_input('Введите координату клетки фигуры по горизонтали: ', 'Введены некорректные данные. Попробуйте снова.')
    vertical = get_input('Введите координату клетки фигуры по вертикали: ', 'Введены некорректные данные. Попробуйте снова.')
    attackhorizontal = get_input('Введите координату атакуемой клетки по горизонтали: ', 'Введены некорректные данные. Попробуйте снова.')
    attackvertical = get_input('Введите координату атакуемой клетки по вертикали: ', 'Введены некорректные данные. Попробуйте снова.')
    figure = get_input('''Какую фигуру вы хотите использовать?
        1 -- Ферзь
        2 -- Ладья
        3 -- Слон
        4 -- Конь
        Ваш выбор: ''', 'Введены некорректные данные. Попробуйте снова.', range_min=1, range_max=4)

    # Проверка на совпадение цветов
    if (horizontal + vertical) % 2 == (attackhorizontal + attackvertical) % 2:
        print('Они одного цвета --', end=' ')
        if (horizontal + vertical) % 2 == 0:
            print('белого')
        else:
            print('черного')
    else:
        print('Нет, они не одного цвета')

    # Вычисление горизонтальных и вертикальных расстояний
    dx = abs(horizontal - attackhorizontal)
    dy = abs(vertical - attackvertical)

    # Проверьте, угрожает ли фигура полю + второй ход
    if figure == 1:     # Ферзь
        if horizontal == attackhorizontal or vertical == attackvertical or dx == dy:
            print(f'Ферзь угрожает полю ({attackhorizontal}; {attackvertical})')
        else:
            print(f'Ферзь не угрожает полю ({attackhorizontal}; {attackvertical})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({attackhorizontal}; {vertical})')
    elif figure == 2:   # Ладья
        if horizontal == attackhorizontal or vertical == attackvertical:
            print(f'Ладья угрожает полю ({attackhorizontal}; {attackvertical})')
        else:
            print(f'Ладья не угрожает полю ({attackhorizontal}; {attackvertical})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({attackhorizontal}; {vertical})')
    elif figure == 3:   # Слон
        if dx == dy:
            print(f'Слон угрожает полю ({attackhorizontal}; {attackvertical})')
        else:
            print(f'Слон не угрожает полю ({attackhorizontal}; {attackvertical})')
            if (horizontal + vertical) % 2 != (attackhorizontal + attackvertical) % 2:
                print(f'Слон никаким образом не может угрожать полю ({attackhorizontal}; {attackvertical})')
            else:
                attackhorizontal0, attackvertical0, attackhorizontal1, attackvertical1 = attackhorizontal, attackvertical, 0, 0
                while 0 < attackhorizontal0 < 9 and 0 < attackvertical0 < 9:
                    attackhorizontal0 += 1
                    attackvertical0 += 1
                    if abs(horizontal - attackhorizontal0) == abs(vertical - attackvertical0):
                        attackhorizontal1 = attackhorizontal0
                        attackvertical1 = attackvertical0
                        break
                attackhorizontal0 = attackhorizontal
                attackvertical0 = attackvertical
                while 0 < attackhorizontal0 < 9 and 0 < attackvertical0 < 9:
                    attackhorizontal0 += 1
                    attackvertical0 -= 1
                    if abs(horizontal - attackhorizontal0) == abs(vertical - attackvertical0):
                        attackhorizontal1 = attackhorizontal0
                        attackvertical1 = attackvertical0
                        break
                attackhorizontal0 = attackhorizontal
                attackvertical0 = attackvertical
                while 0 < attackhorizontal0 < 9 and 0 < attackvertical0 < 9:
                    attackhorizontal0 -= 1
                    attackvertical0 += 1
                    if abs(horizontal - attackhorizontal0) == abs(vertical - attackvertical0):
                        attackhorizontal1 = attackhorizontal0
                        attackvertical1 = attackvertical0
                        break
                attackhorizontal0 = attackhorizontal
                attackvertical0 = attackvertical
                while 0 < attackhorizontal0 < 9 and 0 < attackvertical0 < 9:
                    attackhorizontal0 -= 1
                    attackvertical0 -= 1
                    if abs(horizontal - attackhorizontal0) == abs(vertical - attackvertical0):
                        attackhorizontal1 = attackhorizontal0
                        attackvertical1 = attackvertical0
                        break
                print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({attackhorizontal1}; {attackvertical1})')
    else:   # Конь
        if abs(dx - dy) == 1:
            print(f'Конь угрожает полю ({attackhorizontal}; {attackvertical})')
        else:
            print(f'Конь не угрожает полю ({attackhorizontal}; {attackvertical})')
    break