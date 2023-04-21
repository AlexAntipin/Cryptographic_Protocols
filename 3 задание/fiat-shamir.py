import sympy
import random
import hashlib
import sys


def gen_general_parametres():
    p = random.randint(100, 10000)
    while not sympy.isprime(p):
        p = random.randint(100, 10000)

    q = random.randint(100, 1000)
    while not sympy.isprime(p):
        q = random.randint(100, 1000)
    n = p * q

    f = open('Простые числа.txt', 'w')
    f.write(str(p) + ' ' + str(q))
    f.close()

    f = open('Число n.txt', 'w')
    f.write(str(n))
    return n


def gen_individual_parametres(k, t):
    f = open('Число n.txt', 'r')
    n = int(f.read())
    f.close()

    s = []
    b = []
    for i in range(k):
        num_generation = random.randint(1, n - 1)
        s.append(num_generation)
        bit_generation = random.randint(0, 1)
        b.append(bit_generation)

    f = open('Секретный ключ.txt', 'w')
    for i in s:
        f.write(str(i) + '\n')
    f.close()

    v = []
    # while True:
    #     print('Мы в цикле')
    #     flag = True
    #     for i in range(k):
    #         try:
    #             t = pow(pow(s[i], 2, n), -1, n)
    #             print('Верно')
    #         except ValueError:
    #             print('Ошибка')
    #             for i in range(k):
    #                 num_generation = random.randint(1, n - 1)
    #                 s.append(num_generation)
    #                 bit_generation = random.randint(0, 1)
    #                 b.append(bit_generation)
    #             flag = False
    #     if flag:
    #         break

    for i in range(k):
        v.append(pow(pow(s[i], 2, n), -1, n))
    f = open('Публичный ключ.txt', 'w')
    for i in v:
        f.write(str(i) + '\n')
    f.close()



def generation_signatures(t, m):

    f = open('Число n.txt', 'r')
    n = int(f.read())
    f.close()

    f = open('Секретный ключ.txt', 'r')
    s = list(map(int, input().split('\n')))
    f.close()

    print(s)
    r = []
    x = []
    for i in range(t):
        r_num = random.randint(1,n-1)
        r.append(r_num)
        x_num = r_num ** 2 % n
        x.append(x_num)

    tmp = bin(int(hashlib.md5((str(m) + "".join(str(i) for i in x)).encode()).hexdigest(), 16))[2:]
    print(tmp)
    h = []
    for i in range(t):
        e = []
        for _ in range(k):
            e.append(int(tmp[0]))
            tmp = tmp[1:]
        h.append(e)
    print(h)

    y = []
    for i in range(len(h)):
        s_mul = (s[0] ** h[i][0]) % n
        # print(s_mul)
        for j in range(1, len(h[i])):
            s_mul *= (s[j] ** h[i][j]) % n
            s_mul = s_mul % n
        num_y = (r[i] * s_mul) % n
        # print (r_lst[i], s_mul, n)
        y.append(num_y)
    return m, h, y


def check_signatures(m, h, y, v):

    z = []
    for i in range(t):
        v_mul = (v[0] ** h[i][0]) % n
        for j in range(1, len(h[i])):
            v_mul *= (v[j] ** h[i][j]) % n
            v_mul = v_mul % n
        num_z = (y[i] ** 2 * v_mul) % n
        z.append(num_z)

    # H_ = h(m, z, k, t)
    tmp = bin(int(hashlib.md5((str(m) + "".join(str(i) for i in z)).encode()).hexdigest(), 16))[2:]
    h_chec = []
    for i in range(t):
        s = []
        for j in range(k):
            s.append(int(tmp[0]))
            tmp = tmp[1:]
        h_chec.append(s)

    print(h_chec)
    print(h)
    if h_chec == h:
        print('Подпись верна!')
    else:
        print('Подпись не верна!')



print("Введите количество случайных бит = ", end = '')
k = int(input())
print("Введите количество раундов = ", end = '')
t = int(input())
print("Введите сообщение = ", end = '')
m = input()


#n = gen_general_parametres()
#print(n)
#s, v = gen_individual_parametres(n, k, t)

#m, h, y = generation_signatures(n, t, s, m)

#check_signatures(m, h, y, v)


if __name__ == "__main__":
    while True:
        action = input("Введите 0 - для генерации общих параметров, 1 - для генерации индивидуальных параметров"
                       ",2 - генерация подписи, 3 - Проверка подписи, 4 - для выхода: ")
        if action == "0":
            gen_general_parametres()
        elif action == "1":
            gen_individual_parametres(k, t)
        elif action == "2":
            m, h, y = generation_signatures(t, m)
        # elif action == "3":
        #     check_signatures(m, h, y, v)
        # elif action == "2":
        #     sys.exit(-1)