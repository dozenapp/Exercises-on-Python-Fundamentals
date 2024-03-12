import random

# sapendo che la funzione random.randint(start, end)
# genera un numero intero compreso tra start e end, end compreso,
# costruire una lista di numeri casuali lunga 100 e
# stampare la somma di tutti i suoi numeri

lnc = []
for i in range(100):
    lnc.append(random.randint(1, 10))

# Sommare tutti i valori
totale = 0
for i in lnc:
    totale = totale + i

print("Totale: ", totale)

# Moltiplicare tutti i valori
totale = 1
for i in lnc:
    totale = totale * i
print("Totale: ", totale)


for i in [7, 8, 9]:
    print(i)

for i in [[4, 5, 6], [7, 8, 9]]:
    print(i)

print("Nel mezzo del cammin di nostra vita")
for i in "Nel mezzo del cammin di nostra vita":
    print(chr(ord(i) + 1))


# Costruire due liste, la prima che contiene i numeri pari fino a 1000
# la seconda che contiene i numeri dispari fino a 1000
# a partire dalle prime due liste,
# costruire una terza lista che contiene prima tutti i pari e poi tutti i dispari
lp = []
for n in range(2, 1000, 2):
    lp.append(n)

ld = []
for n in range(1, 1000, 2):
    ld.append(n)

lp = []
ld = []
for i in range(0, 501):
    lp.append(i * 2)
    ld.append(i * 2 + 1)

a = [1, 2, 3]
a.append([4, 5, 6])
print(a)

l3 = lp
for i in ld:
    l3.append(i)

l3 = lp
l3.extend(ld)
