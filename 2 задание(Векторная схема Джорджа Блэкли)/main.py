import random
import galois
import numpy as np
import sys
import sympy
import os
#p - количество сторон, которые могут восстановить секрет
#n - общее количество сторон
#mod - поле
#m - секрет m

#class Point:
#    def __init__(self, m, points):
#        self.m = m
#        self.points = points

def open_point():
    f = open('Сгенерированная точка.txt', 'r')
    point = list(map(int, f.read().split()))
    return point

def open_sistem_equation(n):
    side = []
    # f = open('Система уравнений.txt', 'r')
    # text = f.read()
    # text = text.split('\n')
    # for i in range(len(text)):
    #     side.append(list(map(int, text[i].split())))
    # return side

    for i in range(n):
        if os.path.exists(f'{i}_доля.txt'):
            f = open(f'{i}_доля.txt', 'r')
            text = f.read()
            text = text.strip().split('\n')
            f.close()
            for i in range(len(text)):
                side.append(list(map(int, text[i].split())))
    return side



def write_sistem_equation(side):
    f = open('Система уравнений.txt', 'w')
    for i in range(len(side)):
        for j in range(len(side[i])):
            f.write(str(side[i][j]) + ' ')
        f.write('\n')
    f.close()



def write_secret_side(result_secret, side):
    f = open('Секреты сторон.txt', 'w')
    f.write("Секреты сторон:" + '\n')
    for i in result_secret:
        f.write(str(i) + '\n')
    f.close()
    print(side)
    for i in range(len(side)):
        f = open(f'{i}_доля.txt', 'w')
        for j in range(len(side[i])):
            f.write(str(side[i][j]))
            f.write(' ')
    f.close()



def gen_side_equation():
    side = []
    for i in range(n):
        side.append([])
        for j in range(p):
            num_generation = random.randint(0, mod - 1)
            side[i].append(num_generation)
    return side

def gen_side_equation_full(side, point):
    result_secret = []
    for i in side:
        result = 0
        for j in range(len(i)):
            result += i[j] * point[j]
        result = -result % mod
        result_secret.append(result)
        i.append(result)
    return side, result_secret

def decide_system_equation(mod, p, side):
    GF = galois.GF(mod)
    side_secret = []
    side_x = []
    i = 0
    while i < p:
        lin_side = random.choice(side)
        if not lin_side in side_secret and lin_side != []:
            side_secret.append(lin_side)
            i += 1

    for i in range(len(side_secret)):
        side_x.append(side_secret[i][-1])
        side_secret[i] = side_secret[i][:-1]
    side_x = [(i * -1) % mod for i in side_x]

    A = GF(side_secret)
    b = GF(side_x)
    print(side_secret)
    print(side_x)
    try:
        x = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return [False]
    return x

def write_encrypt_message(x):
    f = open('Зашифрованное Сообщение.txt', 'w')
    str_n = int(x[0])
    str_n = str_n.to_bytes((str_n.bit_length() + 7) // 8, 'big').decode('utf8')
    f.write(str(str_n) + '\n')

#----------------------------------------

def generation_point(m, p, mod):
    point = [m]
    for i in range(p - 1):
        num_generation = random.randint(0, mod - 1)
        point.append(num_generation)
    print(f'Сгенерированная точка = {point}', end = '\n\n')
    f = open('Сгенерированная точка.txt', 'w')
    for i in point:
        f.write(str(i) + ' ')



def generation_dol(n, p, mod):

    point = open_point()
    side = gen_side_equation()
    print(f'Выводим уравнения {side}', end = '\n\n')
    print(f'{mod}')
    side, result_secret = gen_side_equation_full(side, point)

    write_sistem_equation(side)
    write_secret_side(result_secret, side)

    #A = np.matrix(side)
    #print(f'Выводим ранг матрицы {np.linalg.matrix_rank(A)}')
    #B = np.matrix(side)
    #print(f'Выводим ранг матрицы {np.linalg.matrix_rank(B)}')


#print(generation_dol(4, 3, 11, [6, 4, 2]))


def restoring_the_secret(mod, p, n):

    side = open_sistem_equation(n)
    x = decide_system_equation(mod, p, side)
    if x[0] == False:
        print("Линейнозависимые вектора")
        generation_dol(n, p, mod)
        restoring_the_secret(mod, p, n)
        sys.exit(-1)

    #Rang_A = np.matrix(side_secret)
    #print(side_secret)
    #print(f'Выводим ранг матрицы {np.linalg.matrix_rank(Rang_A)}')
    #print()
    str_n = int(x[0])

    print(f'Наш секрет равен = {x[0]}', end = '\n\n')
    print(str_n.to_bytes((str_n.bit_length() + 7) // 8, 'big').decode('utf8'))
    write_encrypt_message(x)




#print("Введите модуль = ", end ='')
#f = open('Поле.txt', 'r')
#mod = int(f.read())
#f.close()



print("Введите количество сторон, которые могут восстановить секрет = ", end= '')
p = int(input())
print("Введите общее количество сторон = ", end ='')
n = int(input())

f = open('Изначальное сообщение.txt', 'r')
#print("Введите секрет = ", end ='')
m = f.read()
bin_result = ''.join(format(ord(x), '08b') for x in m)
bin_result = int(bin_result, 2)
m = bin_result



f.close()

f = open('Поле.txt', 'w')
while True:
    mod = random.randint(m + 1, m + 1000000000)
    if sympy.isprime(mod):
        break
f.write(str(mod))
f.close()



#1 шаг мы создаем точку в пространстве
#point = generation_point(m, p, mod)
#2 шаг мы создаем уравнения системы
#side = generation_dol(n, p, mod, point)
#restoring_the_secret(side, mod, p)

if __name__ == "__main__":
    while True:
        action = input(f"Введите 0 - для создания точки, 1 - для составление гиперплоскостей, 2 - для нахождения "
                       f"секрета по {p} сторонам, 3 - для выхода: ")
        if action == "0":
            generation_point(m, p, mod)
        elif action == "1":
            generation_dol(n, p, mod)
        elif action == "2":
            restoring_the_secret(mod, p, n)
        elif action == "3":
            sys.exit(-1)