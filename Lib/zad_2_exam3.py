# 2 Определить функцию, которая проверяет является ли строка, введенная пользователем,
# целым числом.
# Решение задачи сдать ссылкой на GitHub.


def prov_int(z):
    int(input("Введите число: "))

    try:
        return True, ('эта строка - Целое число')

    except ValueError:
        return False, ('Эта строка не является целым числом')
print(prov_int(input()))
#ИЛИ
#Даны две строки. Определить функцию, которая будет находить индекс второго вхождения второй строки в первую.
# Если подстрока ' ' вывести None. Решение сдать ссылкой на GitHub.
#Input:                                 Output:
# func('marry', 'r')            --> 3
# func('merry christmas', 's')  --> 14
# func('happy new year', ' ')   --> None

