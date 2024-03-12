# Comprehesion
lista = [1, 2, 3, 4, 5]

lista2 = [x * x for x in lista]
print(lista2)
# Nel modo classico
lista2 = []
for x in lista:
    lista2.append(x * x)

lista = [2, 3, 4]
lista3 = [y for x in lista for y in range(1, x)]
print(lista3)


lista_dispari = [x * 2 + 1 for x in range(0, 5)]
lista_numeri = [x for x in range(0, 5)]
print(lista_numeri)
print(lista_dispari)
print(list(zip(lista_numeri, lista_dispari)))

nomi = ["mario", "blanco", "verde", "nerone"]
cognomi = ["rossi", "bianchi", "verdi", "neri", "blue"]

coppie = list(zip(nomi, cognomi))
print(coppie)
