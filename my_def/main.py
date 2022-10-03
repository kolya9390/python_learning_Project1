def predict(numbers):  # угадываем число
    import random
    number = random.randint(1, 100)
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


predict(int(input("Введите загаданое число")))
