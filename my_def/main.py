def is_valid_predict(numbers):
    return numbers.isdigit() and 1 < int(numbers) < 100

def predict(answer):  # угадываем число от 1 до n
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
            answer = 'NO'
            break
    return print("Вы угадали, поздравляем!",
                 "\n"f"Спасибо, что играли в числовую угадайку. Еще увидимся...{name}",
                 f"Совершено {count} попыток""\n"), predict(input('Введите [YES], если хотите повторить и [NO],'
                                                                  'если хотите закончить.''\n'))


def predict_n(n): ##'Количество попыток для угадывания числа в промежутке от 1 до n'
    if n % 2 != 0:
        n += 1
    count = 1
    middle = n//2
    while middle != 1 and middle != 0:
        if middle % 2 != 0 and middle != 1:
            middle = middle+1
        middle //= 2
        count += 1
    return count

print(predict(input('Введите [YES], когда будете готовы начать игру в числовую угадайку.''\n')))
