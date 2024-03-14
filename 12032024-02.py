import math
import random


# a = 10
# b = 20
# c = 30

# Se a è pari, stampo b+c
# Se a è dispari, stampo b-c

# Per verificare se a è pari
# if a % 2 == 0:

# Secondo modo, con & (and)
"""
010101 & 
000001 = 
==========
000001

010100 & 
000001 = 
==========
000000
"""
# if a & 1 == 0:


#######
# Terzo modo
# if math.floor(a/2)*2 == a:

# Non efficiente ma solo per
# dimostrarvi in quanti modi si
# può fare un calcolo
"""
while a>0:
    a=a-2
if a == 0: #test di parità
"""
if False:
    # Supponiamo di aver scelto la tecnica con il modulo
    a = 10
    b = 20
    c = 30

    if a % 2 == 0:
        print(b + c)
    else:
        print(b - c)

    a = 13
    b = 7
    c = 2
    if a % 2 == 0:
        print(b + c)
    else:
        print(b - c)

    a = int(input())
    b = int(input())
    c = int(input())
    if a % 2 == 0:
        print(b + c)
    else:
        print(b - c)


# a = int(input())
# b = int(input())

# if a > b:
#     c = a - b
#     print(a)

# print(c)

if False:
    # Come posso evitare di copiare e copiare e copiare
    # sempre lo stesso pezzo di codice?
    # Le funzioni!!!
    # a,b,c sono parametri formali (il valore sarà assegnato a
    # tempo di chiamata della funzione)
    def Arit(a, b, c):
        # una variabile definita in una
        # funzione, non è visibile dall'esterno
        d = 100
        if a % 2 == 0:
            print(b + c)
        else:
            print(b - c)

    Arit(10, 11, 12)
    Arit(11, 2, 3)
    Arit(101, 1000, 2)
    a, b, c = 10, 20, 30
    Arit(b, c, a)

c = 10


def Cambia(a, b):
    d = 90
    a = b
    c = 30
    print(a)


a = 100
b = 200
Cambia(a, b)
print(a)


def Somma(a, b):
    c = a + b
    return c


print(Somma(1, 2))
print(Somma("a", "b"))


a, b, c = 1, 2, 3


def Divisione(a, b):
    return a // b, a % b


h, i = a // b, a % b


# Scrivere una funzione ColoreCasuale() che torna una stringa
# casuale tra "rosso", "giallo", "verde", "blu", "arancio", "ciano", ...
def ColoreCasuale():
    colori = ["rosso", "giallo", "verde", "blu", "arancio", "ciano", "rosa", "turchese"]
    return colori[random.randint(0, len(colori) - 1)]


print(ColoreCasuale())
print(ColoreCasuale())
print(ColoreCasuale())
print(ColoreCasuale())


def Square(x):
    return x * x


a = Square(1234567890)
print(a)
print(Square(1234567890))


def Sqrt(a):
    return a**0.5


def Maggiore(a, b):
    if a > b:
        return a
    else:
        return b


print(Maggiore(10, 20))


# cerca il più grande elemento di una lista
def Maggiore(lista):
    if type(lista) != "<class 'list'>":
        return None
    if len(lista) == 0:
        return None
    else:
        magg = lista[0]
        for i in lista[1:]:
            if magg < i:
                magg = i
        return magg


print(Maggiore([1, 8, 3, 6, 7, 9, 7, 45, 42, 423, 5, 23]))
print(Maggiore([]))
print(Maggiore("HaHaHA"))
print(type("Ciao"))
print(type(1))
print(type([]))
print(Maggiore(1))


# Ricordate che un digit è uno tra 0,1,2,3,4,5,6,7,8,9
# Problema: scrivere una funzione che costruisce una lista
# contenente tutte le possibili combinazioni di quattro
# digit.
def GeneraListaDigit():
    lista = []
    for i in range(0, 10000):
        s = str(i)
        while len(s) < 4:
            s = "0" + s
        lista.append(s)
    return lista


print(GeneraListaDigit())


# Data una stringa numerica (es: "98123"), convertirla in una lista di digit [9,8,1,2,3]
# def StringDigitsToList(sd):
# ...

# Esempio di utilizzo
# print(StringDigitsToList("918357"))
# Stampa: [9,1,8,3,5,7]


# Modificare la GeneraListaDigit per generare una lista di liste del tipo
# [[0,0,0,0], [0,0,0,1], [0,0,0,2], ..., [9,9,9,8], [9,9,9,9]]
def GeneraListaDigit():
    lista = []
    for i in range(0, 10000):
        s = str(i)
        s = "0" * (4 - len(s)) + s
        # s = s.zfill(4)
        # while len(s) < 4:
        #     s = "0" + s
        lista.append(s)
    return lista


# lista1 = [0, 9, 8, 7, 6]
## lista2 = [0, 9, 8, 7, 6]

# for lista2 in lista1:
#     print(lista2)
