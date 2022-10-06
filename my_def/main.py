def predict(numbers,n):  # угадываем число от 1 до n
    import random
    number = random.randint(1, n)
    while numbers != number:
        if numbers < number:
            print('Слишком мало, попробуйте еще раз')
            numbers = int(input())
            continue
        elif numbers > number:
            print('Слишком много, попробуйте еще раз')
            numbers = int(input())
            continue
        elif numbers == number:
            break
    return print("Вы угадали, поздравляем!")


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