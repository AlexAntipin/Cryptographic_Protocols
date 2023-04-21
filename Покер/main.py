import random
import sympy
import math
import os
def findN(n):
    l = n // 2
    p = random.getrandbits(l)
    while p.bit_length() != l or not sympy.isprime(p):
        p = random.getrandbits(l)
    q = random.getrandbits(l)
    while q.bit_length() != l or not sympy.isprime(q) or q == p:
        q = random.getrandbits(l)
    return p, q, p * q
def FindObr(e, p):
    p1 = p
    q = []
    q.append(0)
    pn = []
    pn.append(1)
    a = -1
    while a != 0:
        k = p // e
        a = p % e
        q.append(k)
        p = e
        e = a
    pn.append(q[1])
    for i in range(1, len(q) - 1):
        ans = pn[i] * q[i + 1] + pn[i - 1]
        pn.append(ans)
    n = len(q) - 1
    res = (((-1) ** (n - 1)) * pn[n - 1]) % p1
    return res

def generatepq(n1):
    p, q, n = findN(n1)
    with open('Настройки\pq.txt', 'w', encoding="utf-8") as f0:
        pqstr = str(p) + " " + str(q)
        f0.write(pqstr)

def readpq():
    filename1 = os.getcwd() + "\\Настройки\\pq.txt"
    with open(filename1, "r") as f1:
        s = f1.readline()
    p = ""
    q = ""
    while s[0] != " ":
        p += s[0]
        s = s[1:]
    s = s[1:]
    while len(s) != 0:
        q += s[0]
        s = s[1:]
    return int(p), int(q)

def getcurrentplayer():
    filenamecurrentPlayer = "Настройки\Текущий игрок.txt"
    with open(filenamecurrentPlayer, 'r', encoding='utf-8') as f1:
        playername = str(f1.readline()).replace('\n', '')
    return playername


def setcurrentplayer(currentplayerparam):
    filenamecurrentPlayer = "Настройки\Текущий игрок.txt"
    with open(filenamecurrentPlayer, 'w', encoding='utf-8') as f1:
        f1.write(currentplayerparam)


def getplayers():
    filenamePlayers = "Настройки\Игроки.txt"
    with open(filenamePlayers, 'r', encoding='utf-8') as f1:
        playersparam = [str(_).replace('\n', '') for _ in f1.readlines()]
    return playersparam


def getstartplayer():
    filenamePlayers = "Настройки\Раздающий игрок.txt"
    with open(filenamePlayers, 'r', encoding='utf-8') as f1:
        players = [str(_).replace('\n', '') for _ in f1.readlines()]
    return int(players[0]) - 1

def getstartplayername():
    startplayerid = getstartplayer()
    players = getplayers()
    return str(players[startplayerid])


def preparefolders():
    playerfolderkeys= "Ключи\\"
    playerfoldercards= "Карты игрока\\"
    playerfoldercol = "Колода\\"
    if not os.path.exists(playerfolderkeys):
        os.mkdir(playerfolderkeys)
    if not os.path.exists(playerfoldercards):
        os.mkdir(playerfoldercards)
    if not os.path.exists(playerfoldercol):
        os.mkdir(playerfoldercol)


def rsa():
    p, q = readpq()
    n = int(p) * int(q)
    phi = (int(p) - 1) * (int(q) - 1)
    while True:
        e = random.randint(1, phi)
        while math.gcd(e, phi) != 1:
            e = random.randint(1, phi)
        d = FindObr(e, phi)
        if d != -1:
            filename1 = "Ключи\\Открытый ключ.txt"
            filename2 = "Ключи\\Закрытый ключ.txt"
            with open(filename1, 'w') as f1:
                strkey1 = str(e) + " " + str(n)
                f1.write(strkey1)
            with open(filename2, 'w') as f2:
                 strkey2 = str(d) + " " + str(n)
                 f2.write(strkey2)
            break


def clearfiles():
    filename1 = os.getcwd() + "\\Карты игрока\\"
    filename2 = os.getcwd() + "\\Колода\\"
    filename3 = os.getcwd() + "\\Ключи\\"
    for i in range(1, 53):
        p = filename1 + f"{i}.txt"
        if os.path.exists(p):
            os.remove(p)
        p = filename2 + f"{i}.txt"
        if os.path.exists(p):
            os.remove(p)
    p = filename1 + "Карты.txt"
    if os.path.exists(p):
        os.remove(p)
    p = filename3 + "Открытый ключ.txt"
    if os.path.exists(p):
        os.remove(p)
    p = filename3 + "Закрытый ключ.txt"
    if os.path.exists(p):
        os.remove(p)

def EnText(ftext):
    fa = open("Настройки\\alph.txt", "r")
    ft = open(ftext, "r")
    print(ftext)
    text = ""
    tmptext = []
    tmptext1 = []
    symb = {}
    for line in fa:
        key, value = line.split('=')
        symb[key] = value.rstrip()
    print(symb)
    for line in ft.readlines():
        tmptext.append(line)
    print(tmptext)
    for i in tmptext:
        j = 0
        while j < len(i):
            tmptext1.append(symb.get(i[j]))
            j = j + 1
    print(tmptext1)
    for i in tmptext1:
        text = text + str(i)
    print(text)
    ft.close()
    fa.close()
    return text


def genstr():
    n = " 12345"
    return n
def lengenstr():
    n = 5
    return n

def shuffledeck():
    col = getdeckordered()
    filename1 = os.getcwd() + "\\Колода\\"
    for i in range(0, 52):
        randstr = genstr()
        p = filename1 + f"{i + 1}.txt"
        with open(p, "w") as f1:
            f1.write(str(col[i]) + randstr)


def getdeckordered():
    col = ["2D", "2H", "2C", "2S", "3D", "3H", "3C", "3S", "4D", "4H", "4C", "4S",
           "5D", "5H", "5C", "5S", "6D", "6H", "6C", "6S", "7D", "7H", "7C", "7S",
           "8D", "8H", "8C", "8S", "9D", "9H", "9C", "9S", "10D", "10H", "10C", "10S",
           "JD", "JH", "JC", "JS", "QD", "QH", "QC", "QS", "KD", "KH", "KC", "KS",
           "AD", "AH", "AC", "AS"]
    return col


def gendeck():
    col = getdeckordered()
    random.shuffle(col)
    filename1 = os.getcwd() + "\\Колода\\"
    for i in range(0, 52):
        randstr = genstr()
        p = filename1 + f"{i + 1}.txt"
        with open(p, "w") as f1:
            f1.write(str(col[i]) + randstr)


def readopenkey():
    filename1 = os.getcwd() + "\\Ключи\\Открытый ключ.txt"
    with open(filename1, "r") as f1:
        s = f1.readline()
        f1.close()
    e = ""
    n = ""
    while s[0] != " ":
        e += s[0]
        s = s[1:]
    s = s[1:]
    while len(s) != 0:
        n += s[0]
        s = s[1:]
    return int(e), int(n)


def readkey():
    filename1 = os.getcwd() + "\\Ключи\\Закрытый ключ.txt"
    with open(filename1, "r") as f1:
        s = f1.readline()
    e = ""
    n = ""
    while s[0] != " ":
        e += s[0]
        s = s[1:]
    s = s[1:]
    while len(s) != 0:
        n += s[0]
        s = s[1:]
    return int(e), int(n)


def StartingCh():
    e, n = readopenkey()
    filename1 = os.getcwd() + "\\Колода\\"
    for i in range(0, 52):
        p = filename1 + f"{i + 1}.txt"
        mes = EnText(p)
        print(mes)
        newval = pow(int(mes), e, n)
        with open(p, "w") as f1:
            f1.write(str(newval))

def getnextplayername():
    playerslist = getplayers()
    currentplayer = getcurrentplayer()
    currentplayerindex = list(playerslist).index(currentplayer)
    nextplayerindex = (currentplayerindex + 1) % len(playerslist)
    return list(playerslist)[nextplayerindex]


def givealldeck(player):
    currentplayer = getcurrentplayer()
    nextplayername = player
    playerslist = []
    playerslist = getplayers()
    filename1 = os.getcwd() + "\\" + currentplayer + "\\Колода\\"
    filename2 = os.getcwd() + "\\" + nextplayername + "\\Колода\\"
    for i in range(0, 52):
        p = filename1 + f"{i + 1}.txt"
        p1 = filename2 + f"{i + 1}.txt"
        if os.path.exists(p):
            os.replace(p, p1)
    setcurrentplayer(nextplayername)


def shufflefilenames():
    s = []
    filename1 = os.getcwd() + "\\Колода\\"
    for i in range(0, 52):
        p = filename1 + f"{i + 1}.txt"
        with open(p, "r") as f1:
            s.append(f1.readline())

    random.shuffle(s)
    for i in range(0, 52):
        p = filename1 + f"{i + 1}.txt"
        with open(p, "w") as f2:
            f2.write(s[i])


def ChooseCards1(numcards):
    filename1 = os.getcwd() + "\\Колода\\"
    cards = []
    for i in range(1, 53):
        if os.path.exists(filename1 + f"{i}.txt"):
            cards.append(i)
    totalnumcards = len(cards)
    if numcards > totalnumcards:
        numcards = totalnumcards
    nind = []
    for i in range(0, numcards):
        tmp = random.randint(1, totalnumcards)
        while tmp in nind:
            tmp = random.randint(1, totalnumcards)
        nind.append(tmp)
    n1 = []
    for i in range(0, len(nind)):
        n1.append(cards[nind[i] - 1])
    filename1 = os.getcwd() + "\\Колода\\"
    filename2 = os.getcwd() + "\\Карты игрока\\"
    for i in n1:
        p2 = filename1 + f"{i}.txt"
        p3 = filename2 + f"{i}.txt"
        os.replace(p2, p3)
    pk = filename2 + "Карты.txt"
    with open(pk, 'w') as f:
        for i in n1:
            f.write(str(i))
            f.write(" ")


def Encrypt():
    e, n = readopenkey()
    p = os.getcwd() + "\\Карты игрока\\Карты.txt"
    with open(p, "r") as f:
        cardstoencrypt = f.readline().split()
    for card in cardstoencrypt:
        p = os.getcwd() + "\\Карты игрока\\" + f"{int(card)}.txt"
        with open(p, "r") as f:
            mes = int(f.readline())
        newval = pow(mes, e, n)
        with open(p, 'w') as f:
            f.write(str(newval))


def GetBackChoosenCards(player):
    startingplayername = getstartplayername()
    d, n = readkey(startingplayername)
    filename1 = os.getcwd() + "\\" + startingplayername + "\\Карты игроков\\" + player + "\\"
    filename2 = os.getcwd() + "\\" + player + "\\Карты игрока\\"
    for i in range(0, 52):
        p = filename1 + f"{i + 1}.txt"
        if os.path.exists(p):
            with open(p, "r") as f:
                mes = int(f.readline())
            newval = pow(mes, d, n)
            with open(p, "w") as f:
                f.write(str(newval))
            p1 = filename2 + f"{i + 1}.txt"
            os.replace(p, p1)


def Decrypt():
    d, n = readkey()
    p = os.getcwd() + "\\Карты игрока\\Карты.txt"
    with open(p, "r") as f:
        cardstodecrypt = f.readline().split()
    for card in cardstodecrypt:
        p = os.getcwd() + "\\Карты игрока\\" + f"{int(card)}.txt"
        with open(p, "r") as f:
            mes = int(f.readline())
        newval = pow(mes, d, n)
        with open(p, 'w') as f:
            f.write(str(newval))


def DecryptDecode():
    d, n = readkey()
    p = os.getcwd() + "\\Карты игрока\\Карты.txt"
    with open(p, "r") as f:
        cardstodecrypt = f.readline().split()
    for card in cardstodecrypt:
        p = os.getcwd() + "\\Карты игрока\\" + f"{int(card)}.txt"
        with open(p, "r") as f:
            mes = int(f.readline())
        newval = pow(mes, d, n)
        with open(p, 'w') as f:
            ftext = DecText(newval)
            f.write(str(ftext))

def GetCards(player, num):
    currentplayer = getcurrentplayer()
    if not player == currentplayer:
        givealldeck(player)
    currentplayer = getcurrentplayer()
    ChooseCards(currentplayer, num)
    if not player == getstartplayername():
        GetBackChoosenCards(currentplayer)
    Decrypt(currentplayer)
def get_key(d, value):
    for k, v in d.items():
        if int(v) == int(value):
            return k
def DecText(c4):
    fa = open("Настройки\\alph.txt", "r")
    finalTexttmp = ([str(c4)[i:i + 2] for i in range(0, len(str(c4)), 2)])
    finalTexttmp1 = []
    finaltext = ""
    symb = {}
    for line in fa:
        key, value = line.split('=')
        symb[key] = value.rstrip()
    for i in finalTexttmp:
        finalTexttmp1.append(get_key(symb, int(i)))
    for i in finalTexttmp1:
        finaltext = finaltext + str(i)
    fa.close()
    return finaltext

def printCards():
    n = lengenstr()
    p = os.getcwd() + "\\Карты игрока\\"
    cards = []
    for i in range(1, 53):
        p1 = p + f"{int(i)}.txt"
        if os.path.exists(p1):
            with open(p1, 'r') as f:
                temp = f.readline()
                # temp = temp[0:-n]
                cards.append(temp)
    print("Карты игрока : ", cards)


def printKeys():
    p = os.getcwd() + "\\Ключи\\"
    p1 = p + "Открытый ключ.txt"
    if os.path.exists(p1):
        with open(p1, 'r') as f:
            temp = f.readline()
    print("Открытый ключ : ", temp)
    p2 = p + "Закрытый ключ.txt"
    if os.path.exists(p2):
        with open(p2, 'r') as f:
            temp = f.readline()
    print("Закрытый ключ : ", temp)


def main():
    print("""Введите номер шага:
         1. Генерация p и q
         2. Сгенерировать ключи
         3. Генерировать колоду
         4. Шифровать колоду
         5. Перемешать имена файлов
         6. Отобрать 5 карт
         7. Зашифровать выбранные карты
         8. Расшифровать выбранные карты
         9. Расшифровать и декодировать выбранные карты
         10. Открыть карты
         11. Открыть ключи
         """)
    ch = int(input())
    if ch == 1: #Сгенерировать p q
        preparefolders()
        clearfiles()
        print("Введите число бит: ")
        n = int(input())

        generatepq(n)
    if ch == 2: #Сгенерировать ключи
        rsa()
    if ch == 3: #Сгенерировать колоду
        gendeck()
    if ch == 4: #Шифровать колоду
        StartingCh()
    if ch == 5: #Перемешать имена файлов
        shufflefilenames()
    if ch == 6: #Отобрать 5 карт
        ChooseCards1(5)
    if ch == 7: #Зашифровать выбранные карты
        Encrypt()
    if ch == 8: #Расшифровать выбранные карты
        Decrypt()
    if ch == 9:  # Расшифровать и декодировать выбранные карты
        DecryptDecode()
    if ch == 10:  #Открыть карты
        printCards()
    if ch == 11:  #Открыть ключи
        printKeys()


if __name__ == '__main__':
    main()