number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

print("Первое число: ", number1)
print("Второе число: ", number2)

message = '''
Выберете математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение

Ваш выбор:
'''

operation = input(message)
try:
    if operation == '+':
        result = number1 + number2
        print('Результат сложение', result)
    elif operation == '-':
        result = number1 - number2
        print('Результат вычитание', result)
    elif operation == '/':
        result = number1 / number2
        print('Результат деление', result)
    elif operation == '*':
        result = number1 * number2
        print('Результат умножение: ', result)
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
