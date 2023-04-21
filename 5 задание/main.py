def Alisa():
    koloda = []
    for i in range(1, 11):
        suit = ['worms', 'bubi', 'blame', 'cross']
        for j in range(4):
            card = str(i) + " " +  suit[j]
            koloda.append(card)
    print(koloda)

Alisa()