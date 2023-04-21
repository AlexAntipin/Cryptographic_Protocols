from random import randint
from sympy import isprime
from math import sqrt

def nod(a, b):
    while a % b != 0:
        tmp = b
        b = a % b
        a = tmp
    return b

def reverse_element(a, m):
    return pow(a, -1, m)

def gen_key():
    #print("Введите разрядность чисел p, q:")

    f1 = open('Разрядность p и q.txt', 'r')
    exp = int(f1.read())
    f1.close()

    q = randint(pow(2, exp - 1), pow(2, exp))
    while not isprime(q):
        q = randint(pow(2, exp - 1), pow(2, exp))
    # print('q=', q)
    p = randint(pow(2, exp - 1), pow(2, exp))
    while not isprime(p):
        p = randint(pow(2, exp - 1), pow(2, exp))
    n = p * q
    print(n)
    f1 = open('n.txt','w')
    f1.write(str(n))
    f1.close()

    f1 = open('k (Количество элементов в ключах).txt', 'r')
    k = int(f1.read())
    f1.close()

    # print('Введите кол-во элементов в ключах:')
    # k = int(input())
    x_arr = []
    v = []

    # kvad_ost = []
    # for i in range(n):
    #     x = (i * i) % n
    #     print('тут')
    #     if not x in kvad_ost:
    #         kvad_ost.append(x)

    # for _ in range(k):
    #     while True:
    #         #len_str_n = len(str(n))
    #         x = randint(1, n - 1)
    #         x2 = pow(x, 2, n)
    #         if nod(x2, n) == 1:
    #             x_arr.append(x)
    #             v.append(x2)
    #             break

    #print('Сгенерирован открытый ключ', v)
    s = []
    for i in range(k):
        while True:
            #len_str_n = len(str(n))
            x = randint(1, n - 1)
            if nod(x, n) == 1:
                x_1 = reverse_element(x, n)
                ans = (x_1 ** 2) % n
                s.append(x)
                v.append(ans)
                break

    #s = [pow(i, -1, n) for i in x_arr]
    #print('Сгенерирован закрытый ключ', s)
    f2 = open('Open_key.txt', 'w')
    f3 = open('Private_key.txt', 'w')
    for i in range(k):
        f2.write(str(v[i]) + '\n')
        f3.write(str(s[i]) + '\n')
    return


def step1():
    f4 = open('n.txt','r')
    n = int(f4.read())
    r = randint(1, n-1)
    #print('r= ', r)
    x = (r**2) % n
    f5 = open('x.txt', 'w')
    f5.write(str(x))
    f6 = open('r.txt', 'w')
    f6.write(str(r))
    #print('x= ',x)
    return


def step2():
    k = len(open('Open_key.txt', 'r').readlines())
    b = []
    for _ in range(k):
        q = randint(0,1)
        b.append(q)
    #print('b=', b)
    f7 = open('b.txt','w')
    for i in range(k):
        f7.write(str(b[i]) + '\n')
    return


def step3():
    k = len(open('Open_key.txt', 'r').readlines())
    f8 = open('r.txt','r')
    r = f8.read()
    s = []
    b = []
    f9 = open('Private_key.txt','r')
    for line in f9:
        s.append(int(line))
    #print(s)
    f10 = open('b.txt', 'r')
    for line in f10:
        b.append(int(line))
    y = 1
    f11 = open('n.txt', 'r')
    n = f11.read()
    for i in range(k):
        y = y * s[i]**b[i]
    y = y * int(r) % int(n)
    f12 = open('y.txt','w')
    f12.write(str(y))
    #print('y= ', y)
    #print('n= ',n)
    return


def step4():
    k = len(open('Open_key.txt', 'r').readlines())
    f13 = open('n.txt', 'r')
    f14 = open('x.txt', 'r')
    f15 = open('y.txt', 'r')
    n = int(f13.read())
    x = int(f14.read())
    y = int(f15.read())
    v = []
    b = []
    f16 = open('Open_key.txt', 'r')
    for line in f16:
        v.append(int(line))
    #print(v)
    f17 = open('b.txt', 'r')
    for line in f17:
        b.append(int(line))
    z = 1
    for i in range(k):
        z = z * v[i]**b[i]
    z = (y ** 2 * z) % n
    #print('z= ', z)
    if z != x:
        return False
    else:
        return True
    return


def check():
    gen_key()
    f1 = open('t (Количество раундов).txt', 'r')
    t = int(f1.read())
    f1.close()
    flag = True
    for i in range(t):
        step1()
        step2()
        step3()
        if step4():
            continue
        else:
            flag = False
    if flag:
        f1 = open('Answer.txt', 'w')
        f1.write('Проверка пройдена')
        f1.close()
    else:
        f1 = open('Answer.txt', 'w')
        f1.write('Проверка не пройдена')
        f1.close()



if __name__ == "__main__":
    check()
    # while True:
    #     action = input(
    #         "Введите 0 - для генерации ключей, 1 - для 1 шага протокола,"
    #         " 2 - для 2 шага протокола, 3 - для 3 шага протокола," + "\n" + "4 - для 4 шага протокола, "
    #         "5 - для выполнения всех шагов проткола, 6 - для выхода:" + "\n")
    #     if action == "0":
    #         gen_key()
    #     elif action == "1":
    #         step1()
    #     elif action == "2":
    #         step2()
    #     elif action == "3":
    #         step3()
    #     elif action == "4":
    #         step4()
    #     elif action == "5":
    #         check()
    #     elif action == "6":
    #         exit()