'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).
'''


def factor(n):
    if isinstance(n, int):
        if n >= 0:
            if n == 0 or n == 1:
                return 1
            else:
                product = 1
                for i in range(1, n + 1):
                    product *= i
                return product
        else:
            return
    else:
        return


d = 10
print(d, '! = ', factor(d), sep='')
print('')
print('дополнительно, для проверки функции:')
d = 0
print(d, '! = ', factor(d), sep='')
d = -1
print(d, '! = ', factor(d), sep='')
d = 'adfSDFdgs'
print(d, '! = ', factor(d), sep='')
