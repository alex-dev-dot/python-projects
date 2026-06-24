# Чтобы исключить некорректный ввод со стороны пользователя, создадим бесконечный цикл с помощью while True. Далее мы запрашиваем значение для каждого из двух чисел (по отдельности), при этом исключая возможные ошибки в значении (ValueError) и в имени (NameError)
def main():
    first = get_number('What`s your first number? ')
    second = get_number('What`s your second number? ')
    operation = get_operation('What`s your operation? ')
    result = calculator(first, second, operation)
    print(result)

def get_number(message):
    while True:
        try:
            number = float(input(message))
        except ValueError:
            print('Enter a correct number!')
        else:
            return number

def get_operation(message):
    while True:
        operation = input(message)
        if operation != '+' and operation != '-' and operation != '*' and operation != '/':
            print('Enter a correct operation!')
        else:
            return operation

def calculator(first, second, operation):
    if operation == '+':
        return first + second

    elif operation == '-':
        return first - second

    elif operation == '/':
        if second != 0:
            return first / second
        else:
            return 'Делить на ноль нельзя!'
    elif operation == '*':
        return first * second

main()