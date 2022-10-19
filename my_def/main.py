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


def predict_game_switch():  # Для запуска игры в Угадай число с выбраным промежутком от 1 до N
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


def gen_password():  # Генератор плюс минус надежных паролей
    import random
    chars = ''
    password = list_symbol() + list_ABC() + list_number()
    password = [str(i[0]) for i in password]
    random.shuffle(password)
    chars = chars.join(password)
    return print(chars) and is_password_good(chars)


def task_of_Josephus(n, k):  # Задача Иосифа Флавия
    print(f'в кругу {n} человек и каждый {k} умерает')
    answer = int(input('Попробуй угадать под каким номером человек выживет, но помни , выжевет только один...'"\n"))
    list_n_people = list(range(1, n + 1))
    while len(list_n_people) != 1:
        if k > len(list_n_people):
            while len(list_n_people) != 1:

                step = abs(k - len(list_n_people))
                while step > len(list_n_people):
                    step = abs(step - len(list_n_people))

                list_n_people.remove(list_n_people[step - 1])
                list_n_people = list_n_people[step - 1:] + list_n_people[0:step - 1]
            break

        list_n_people.remove(list_n_people[k - 1])
        list_n_people = list_n_people[k - 1:] + list_n_people[0:k - 1]
    if answer == list_n_people[0]:
        print(f'Вам повезло спасти человека под номером {list_n_people[0]}')
        print("...")
        print('Прощай...')

    if answer != list_n_people[0]:
        print(f'Вы проиграли, вы погубили ещё одну жизнь')
    return print(f"человек под номером {list_n_people[0]}")


def switch_task_of_Josephus():
    return print(task_of_Josephus(int(input('введи количтво людей вставших в круг''\n')),
                                  int(input('Каждый .. выбывает''\n'))))


def pascal(n):  # Треугольник Паскаля
    lst = []
    n = int(n)
    for i in range(n+1):
        m = [1] * (i+1)
        for j in range(i+1):
            if j != 0 and j != i:
                m[j] = lst[i-1][j] + lst[i-1][j-1]
        lst.append(m)

    return print(lst[n])

