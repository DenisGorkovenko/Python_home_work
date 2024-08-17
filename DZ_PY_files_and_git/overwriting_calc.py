#!/usr/bin/env python3

""" Задание 1. В файле calc.txt находится математическое выражение (например, 3285*210-123+854/12),
    нужно посчитать его результат и сохранить в этот же файл после знака равно
    (например, 3285*210-123+854/12=689798.1666666666)."""


def record_calc():
    try:
        with open('calc.txt', 'a+', encoding='utf-8') as file:
            file.seek(0)
            s = file.readline()
            res = eval(s)
            file.write(f'={res}')

    except:
        print('Ошибка при работе с файлом!')


if __name__ == "__main__":
    (record_calc())
