import sympy as sp
import random
from random import randint
from sympy import isprime


# def h(m: str, x: list[int], k: int, t: int) -> list[list[int]]:
#     summa = sum([ord(i) for i in m])
#     binary = bin(int(f'{summa}{"".join(str(i) for i in x)}'.encode('utf-8').hex(), 16)).replace('0b', '')
#
#     result = []
#     for i in range(t):
#         temp = []
#         for j in range(k):
#             temp.append(int(binary[j + i * t]))
#         result.append(temp)
#
#     return result
import hashlib

def gen_n(l):
    exp = l
    q = randint(pow(2, exp - 1), pow(2, exp))
    while not isprime(q):
        q = randint(pow(2, exp - 1), pow(2, exp))
    # print('q=', q)
    p = randint(pow(2, exp - 1), pow(2, exp))
    while not isprime(p):
        p = randint(pow(2, exp - 1), pow(2, exp))
    print('p = ', p)
    print('q = ', q)
    n = p * q
    print('n = ', n)
    file = open('n.txt', 'w')
    file.write(str(n))
    file.close()
    return n


def gen_key(n, k):
    s = []
    v = []
    for _ in range(k):
        x = random.randint(1, n - 1)
        s.append(x)
        v.append(pow(pow(x, 2, n), -1, n))
    file = open('private_key.txt', 'w')
    file.write(' '.join(map(str, s)))
    file.close()
    file = open('public_key.txt', 'w')
    file.write(' '.join(map(str, v)))
    file.close()
    return v, s


def Alice(k, t, n):
    r_lst = []
    x_lst = []
    file = open('m.txt', 'r')
    m = file.read()
    file.close()
    for _ in range(t):
        r = random.randint(0, n - 1)
        r_lst.append(r)
        x_lst.append((r ** 2) % n)

    file = open('r_lst.txt', 'w')
    file.write(' '.join(map(str, r_lst)))
    file.close()

    file = open('x_lst.txt', 'w')
    file.write(' '.join(map(str, x_lst)))
    file.close()

    tmp = bin(int(hashlib.md5((str(m) + "".join(str(i) for i in x_lst)).encode()).hexdigest(), 16))[2:]
    H = []
    for _ in range(t):
        s = []
        for _ in range(k):
            s.append(int(tmp[0]))
            tmp = tmp[1:]
        H.append(s)

    file = open('private_key.txt', 'r')
    s = list(map(int, file.read().split()))
    file.close()
    y_lst = []
    for i in range(len(H)):
        s_mul = (s[0] ** H[i][0]) % n
        # print(s_mul)
        for j in range(1, len(H[i])):
            s_mul *= (s[j] ** H[i][j]) % n
            s_mul = s_mul % n
        y = (r_lst[i] * s_mul) % n
        # print (r_lst[i], s_mul, n)
        y_lst.append(y)

    file = open('b_ij.txt', 'w')
    file.write('\n'.join([' '.join(map(str, i)) for i in H]))
    file.close()

    file = open('y_i.txt', 'w')
    file.write(' '.join(map(str, y_lst)))
    file.close()


def Bob(n, t, k):
    file = open('m.txt', 'r')
    m = file.read()
    file.close()

    H = []
    file = open('b_ij.txt', 'r')
    b_i = file.read().split('\n')
    for i in b_i:
        H.append(list(map(int, i.split())))
    file.close()

    file = open('y_i.txt', 'r')
    y = list(map(int, file.read().split()))
    file.close()

    file = open('public_key.txt', 'r')
    v = list(map(int, file.read().split()))
    file.close()

    z = []
    for i in range(t):
        v_mul = (v[0] ** H[i][0]) % n
        for j in range(1, len(H[i])):
            v_mul *= (v[j] ** H[i][j]) % n
            v_mul = v_mul % n
        z_i = (y[i] ** 2 * v_mul) % n
        z.append(z_i)

    #H_ = h(m, z, k, t)
    tmp = bin(int(hashlib.md5((str(m) + "".join(str(i) for i in z)).encode()).hexdigest(), 16))[2:]
    H_ = []
    for _ in range(t):
        s = []
        for _ in range(k):
            s.append(int(tmp[0]))
            tmp = tmp[1:]
        H_.append(s)


    if H_ == H:
        print('Подпись верна!')
    else:
        print('Подпись не верна!')


def main():
    print(
        'Выберете что вы хотите сделать: \n \t1 - сгенерировать число n\n \t2 - сгенерировать ключи\n \t3 - подписать сообщение\n \t4 - проверить подпись')
    f = input()
    if f == '1':
        l = int(input('Введите длинну простых чисел в битах\n'))
        gen_n(l)
    elif f == '2':
        file = open('n.txt', 'r')
        n = int(file.read())
        file.close()

        file = open('k.txt', 'r')
        k = int(file.read())
        file.close()
        gen_key(n, k)
    elif f == '3':
        file = open('n.txt', 'r')
        n = int(file.read())
        file.close()

        file = open('k.txt', 'r')
        k = int(file.read())
        file.close()

        file = open('t.txt', 'r')
        t = int(file.read())
        file.close()
        Alice(k, t, n)
    elif f == '4':
        file = open('n.txt', 'r')
        n = int(file.read())
        file.close()

        file = open('k.txt', 'r')
        k = int(file.read())
        file.close()

        file = open('t.txt', 'r')
        t = int(file.read())
        file.close()
        Bob(n, t, k)


if __name__ == '__main__':
    main()

#
# n = gen_n()
# k = 10
# t = 10
#
# gen_key(n, k)
#
# Alice(k, t, n)
#
# Bob(n, t, k)
