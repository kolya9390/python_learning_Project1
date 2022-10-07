def is_valid_predict(numbers):
    return numbers.isdigit() and 1 < int(numbers) < 100


def predict_game(answer):  # угадываем число от 1 до n
    answer.lower()
    if answer == 'no':
        return print('Прощай...''\n')
    import random
    name = input('Как вас зовут?''\n')
    count = 0
    print(f' Добро пожаловать в числовую угадайку, {name}')
    n = int(input(f'{name},Введите конечную границу от 1 до (N)''\n'))
    while 1 > 0:
        numbers = input(f'Введите число от 1 до {n}''\n')
        if is_valid_predict(numbers):
            numbers = int(numbers)
            break
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
    count += 1
    number = random.randint(1, n)
    while numbers != number:
        if numbers < number:
            print('Слишком мало, попробуйте еще раз')
            numbers = int(input())
            count += 1
            continue
        elif numbers > number:
            print('Слишком много, попробуйте еще раз')
            numbers = int(input())
            count += 1
            continue
        elif numbers == number:
            break
    return print("Вы угадали, поздравляем!",
                 "\n"f"Спасибо, что играли в числовую угадайку. Еще увидимся...{name}",
                 f"Совершено {count} попыток""\n"), predict_game(input('Введите [YES], если хотите повторить и [NO],'
                                                                       'если хотите закончить.''\n'))


def predict_n(n):  # Количество попыток для угадывания числа в промежутке от 1 до n
    if n % 2 != 0:
        n += 1
    count = 1
    middle = n // 2
    while middle != 1 and middle != 0:
        if middle % 2 != 0 and middle != 1:
            middle = middle + 1
        middle //= 2
        count += 1
    return count


def predict_game_switch():
    return print(predict_game(input('Введите [YES], когда будете готовы начать игру в числовую угадайку.''\n')))


def is_password_good(password):
    flag = False
    c = 0
    for i in password:
        if i.isdigit():
            c += 1
            break
    for i in password:
        if i.isupper():
            c += 1
            break
    for i in password:
        if i.islower():
            c += 1
            break
    if c == 3 and len(password) > 7:
        flag = True
    return flag


def list_ABC():
    import random
    ABC = []
    abc = ['abcdefghijklmnopqrstuvwxyz']
    for i in range(0, 4, random.randint(1, 3)):
        A = random.randint(0, 1)
        if A == 1:
            ABC.append([i[random.randint(0, len(abc) + 1)].upper() for i in abc])
        elif A == 0:
            ABC.append([i[random.randint(0, len(abc) + 1)].lower() for i in abc])

    return ABC


def list_symbol():
    import random
    symbols = ['!@#$%^&*(][{}=+_-/.,)<>~`']

    random.shuffle(symbols)
    symbol = []
    for i in range(0, 3, random.randint(1, 3)):
        symbol.append([i[random.randint(0, len(symbols) + 1)] for i in symbols])
    return symbol


def list_number():
    import random
    numbers = []
    while 1 > 0:
        number = [random.randint(0, 9)]
        numbers.append(number)
        if len(numbers) == 5:
            break
    return numbers


def gen_password():  # len(n)
    import random
    chars = ''
    password = list_symbol() + list_ABC() + list_number()
    password = [str(i[0]) for i in password]
    random.shuffle(password)
    chars = chars.join(password)
    return print(chars) and is_password_good(chars)
