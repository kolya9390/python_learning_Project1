# Алгоритм быстрого слияния
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

# невырожденный триугольник
def is_valid_triangle(side1, side2, side3):
    if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side1 + side2:
        flag = True
    else:
        flag = False
    return flag


# ##
# Простое ли число?
def is_prime(num):
    flag = True
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
            if c > 2 or num==1:
                flag = False
                break
            else:
                flag = True

    return flag
## Следущее простое число
def next_is_prime(num):
    c=0
    while num > 0:
        c+=1
        if is_prime(c) and c > num:
            break
    return c


# сложность пароля
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


###
def is_valid_password(password):
    c = 0
    s=password.split(':')
    if len(s) == 3:
        c += 1

    if s[0][::1] == s[0][::-1]:
        c += 1

    if int(s[1]) % 2 == 0 and is_prime(int(s[2])):
        c += 1

    return c == 3

#### Правильность скобочкек
def is_correct_bracket(text):
    c = 0
    for i in text:
        if i == '(':
            c += 1
        if i == ')':
            c -= 1
            if c < 0:
                break
    return c == 0 and text[0] == '(' and text[-1] == ')'


##
# объявление функции
def convert_to_python_case(text):
    k = ''
    for i in text:

        if i.isupper():
            i = '_'+i
        k += i
    return k[1:]

def dice(again):
    import random
    again = 'д'
    if again.lower() == 'д':
        print('Бросаем кубики... ')
        print('Значения граней:')
        print(random.randint(1, 6))
        print(random.randint(1, 6))
#
#dice(input('Бросить кубики еще раз? (д = да, н = нет): '))



