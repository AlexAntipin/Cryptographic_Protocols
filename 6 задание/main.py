import random
from random import randint
from sympy import isprime

def gcd_fun(x, y):
    if(y == 0): # it divide every number
        return x  # return x
    else:
        return gcd_fun(y, x % y)


def gen_secret():
    secret_suler = []
    for i in range(1, 11):
        file = open(f'{i}_secret.txt', 'r')
        m = file.read()
        bin_result = ''.join(format(ord(x), '08b') for x in m)
        bin_result = int(bin_result, 2)
        m = bin_result
        secret_suler.append(m)
    #f = open('secret.txt', 'w')
    #a = random.randint(1, 100000)
    #print('Введите количество секретов = ', end ='')
    #n_count = int(input())
    #for i in range(n_count):
    #    a = random.randint(1, 10000) % n
    #    secret_suler.append(a)
    print(f'Выведем секреты = {secret_suler}')
    #for i in range(n_count):
    #    f.write(str(secret_suler[i]) + ' ')
    #f.close()

def gen_key_rsa():
    print('Введите количество бит для простых чисел =')
    exp = int(input())

    q = randint(pow(10, exp - 1), pow(10, exp))
    while not isprime(q):
        q = randint(pow(10, exp - 1), pow(10, exp))

    p = randint(pow(10, exp - 1), pow(10, exp))
    while not isprime(p):
        p = randint(pow(10, exp - 1), pow(10, exp))

    n = p * q

    file = open('n.txt', 'w')
    print(f'Выведем n = {n}')
    file.write(str(n))
    file.close()

    fe = (p - 1) * (q - 1)

    file = open('fe.txt', 'w')
    print(f'Выведем fe = {fe}')
    file.write(str(fe))
    file.close()

    e = randint(1, fe)
    while not isprime(e) or gcd_fun(e, fe) != 1:
        e = randint(1, fe)

    file = open('e.txt', 'w')
    print(f'Выведем e = {e}')
    file.write(str(e))
    file.close()

    file = open('Открытый ключ.txt', 'w')
    print(f'Выведем открытый ключ = {e} {n}')
    file.write(str(e) + ' ' + str(n))
    file.close()

    d = pow(e, -1, fe)

    file = open('d.txt', 'w')
    print(f'Выведем d = {d}')
    file.write(str(d))
    file.close()

    file = open('Закрытый ключ.txt', 'w')
    print(f'Выведем закрытый ключ = {d} {n}')
    file.write(str(d) + ' ' + str(n))
    file.close()



def step_1():
    file = open('e.txt', 'r')
    e = int(file.read())
    file.close()

    file = open('n.txt', 'r')
    n = int(file.read())
    file.close()

    s = []
    for i in range(1, 11):
        file = open(f'{i}_secret.txt', 'r')
        m = file.read()
        bin_result = ''.join(format(ord(x), '08b') for x in m)
        bin_result = int(bin_result, 2)
        m = bin_result
        s.append(m)

    print(f'Выводим массив изначальных сообщений{s}')
    str_n = int(s[0])
    #print(str_n.to_bytes((str_n.bit_length() + 7) // 8, 'big').decode('utf8'))
    c = []
    for i in range(len(s)):
        c.append(pow(s[i], e, n))

    print(f'Выводим массив защифрованных сообщений{c}')

    for i in range(1, 11):
        file = open(f'{i}_shifr_secret.txt', 'w')
        file.write(str(c[i - 1]))


    #file = open('c.txt', 'w')
    #for i in range(len(c)):
    #    file.write(str(c[i]) + ' ')
    #file.close()

def step_2():
    c = []
    for i in range(1, 11):
        file = open(f'{i}_shifr_secret.txt', 'r')
        m = file.read()
        file.close()
        c.append(int(m))
    print(f'Выводим с = {c}')

    file = open('e.txt', 'r')
    e = int(file.read())
    file.close()

    file = open('n.txt', 'r')
    n = int(file.read())
    file.close()

    print('Введите номер секрета = ', end = '')
    numer = int(input())

    file  = open(f'{numer}_shifr_secret.txt', 'r')
    c_bob = int(file.read())
    #print(f'Сообщение которое выбрал Боб {c_bob}')
    r = random.randint(1, n - 1)

    file = open('r.txt', 'w')
    file.write(str(r))
    file.close()

    c_bob = (c_bob * pow(r, e, n)) % n

    file = open('c_bob.txt', 'w')
    file.write(str(c_bob))
    file.close()


def step_3():
    file = open('d.txt', 'r')
    d = int(file.read())
    file.close()

    file = open('c_bob.txt', 'r')
    c_bob = int(file.read())
    file.close()

    file = open('n.txt', 'r')
    n = int(file.read())
    file.close()

    p_alisa = pow(c_bob, d, n)

    file = open('p_alisa.txt', 'w')
    file.write(str(p_alisa))
    file.close()


def step_4():
    file = open('r.txt', 'r')
    r = int(file.read())
    file.close()

    file = open('p_alisa.txt', 'r')
    p_alisa = int(file.read())
    file.close()

    file = open('n.txt', 'r')
    n = int(file.read())
    file.close()

    secret = (p_alisa * pow(r, -1, n)) % n
    print(secret)

    print(secret)
    file = open('secret.txt', 'w')
    stroka = secret.to_bytes((secret.bit_length() + 7) // 8, 'big').decode('utf8')
    file.write(stroka)
    print(secret.to_bytes((secret.bit_length() + 7) // 8, 'big').decode('utf8'))

    file = open('Секрет для Боба.txt', 'w')
    file.write(str(secret))
    file.close()

while True:
    print('')
    action = input(
        "Введите 0 - для генерации данных для RSA, 1 - для шифровании всех секретов,"
        " 2 - для выбора секрета Бобом, 3 - Получение Бобом секрета" + "\n" + "4 - для расшифрования секрета,"
                                                                              "5 - для выхода ")
    if action == "0":
        gen_key_rsa()
    elif action == "1":
        step_1()
    elif action == "2":
        step_2()
    elif action == "3":
        step_3()
    elif action == "4":
        step_4()
    elif action == "5":
        exit(0)

#gen_key_rsa()
#gen_secret()
#step_1()
#step_2()
#step_3()
#step_4()