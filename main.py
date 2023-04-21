import os
import sys
import hashlib
import random

def skey_write_in_file(name, dict_hash):
    f = open(name + '/Сервер.txt', 'w')
    f.write(dict_hash[0])
    f.close()

    f = open(name + '/Клиент-Одноразовые_Пароли.txt', 'w')
    for i in range(1, len(dict_hash)):
        f.writelines(dict_hash[i] + '\n')
    f.close()

def skey_write_key_in_file(name, key):
    f = open(name + '/Клиент-Ключ.txt', 'w')
    f.write(key)
    f.close()

def skey_generation_key(len_key):
    key = str(random.getrandbits(len_key))
    return key


def skey_generation(name):
    os.mkdir(name)
    dict_hash = []
    print("Введите количество одноразовых паролей: ", end = '')
    count_password = int(input())
    print("Введите случайное число: ", end = '')
    #len_key = int(input())
    #key = skey_generation_key(len_key)
    key = input()
    skey_write_key_in_file(name, key)

    for i in range(count_password):
        key = hashlib.md5(key.encode("utf8")).hexdigest()
        dict_hash.append(key)
    dict_hash = dict_hash[::-1]
    skey_write_in_file(name, dict_hash)


def skey_registr():
    print("Введите имя пользователя: ", end = '')
    name = input()
    if os.path.exists(name):
        print("Пользователь с таким именем уже существует")
        sys.exit(-1)
    skey_generation(name)



def skey_login():
    print("Введите ваше имя: ", end = '')
    name = input()
    if not os.path.exists(name):
        print("Вас нет в регистрационной базе")
        sys.exit(-1)
    print("Введите пароль: ", end='')
    password = input()
    if os.stat(name +"/Клиент-Одноразовые_Пароли.txt").st_size == 0:
        print("Необходимо обновить регистрационную базу")
        sys.exit(-1)

    f = open(name + '/Сервер.txt', 'r')
    host_password = f.readline()
    f.close()

    password_hash = hashlib.md5(password.encode("utf8")).hexdigest()


    if password_hash == host_password:
        print("Вы успешно зашли!")

        f = open(name + '/Сервер.txt', 'w')
        f.write(password)
        f.close()

        lines = []
        f = open(name + '/Клиент-Одноразовые_Пароли.txt', 'r')
        for i in f.readlines():
           i = i[:-1]
           lines.append(i)
        f.close()

        z = open(name + '/Клиент-Одноразовые_Пароли.txt', 'w')
        for i in range(1, len(lines)):
            z.writelines(lines[i] + '\n')
        z.close()
    else:
        print("Пароль неверный!")
        sys.exit(-1)


if __name__ == "__main__":
    while True:
        action = input("Введите 0 - для регистрации пользователя, 1 - для аутентификации пользователя, 2 - для выхода: ")
        if action == "0":
            skey_registr()
        elif action == "1":
            skey_login()
        elif action == "2":
            sys.exit(-1)


