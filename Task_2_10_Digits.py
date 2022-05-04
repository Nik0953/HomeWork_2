'''
Задача 2
Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
'''


# функция добивается корректного ввода ОДНОЙ цифры от 0 до 9 включительно.
def input_correct_1_digit():
    digit = ''
    good_digit = False
    while not good_digit:
        digit = input('Введите цифру от 1 до 9: ')
        good_digit = digit.isdigit()
        if good_digit:
            d = int(digit)
            if d < 0 or d > 9:
                good_digit = False
        if not good_digit:
            print('Ошибка! Нужна ТОЛЬКО цифра от 0 до 9.')
    return int(digit)


total_number_of_digits = 10
number_of_5 = 0

for i in range(1, total_number_of_digits + 1):
    print('Цифра N ', i, ':')
    number = input_correct_1_digit()
    if number == 5:
        number_of_5 += 1
    i += 1
    print()

print('Всего цифр', total_number_of_digits, 'из них пятерок', number_of_5)
print('end')
