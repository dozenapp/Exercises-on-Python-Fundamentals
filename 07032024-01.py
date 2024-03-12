import random
import time

if False:
    # Costruzione della lista
    start = time.time_ns()
    lista = []
    for v in range(1, 10000000):
        lista.append(random.randint(1, 1000000000))
    end = time.time_ns()

    print(f"Il tempo richiesto è: {(end-start)/1000000000}")

    # Ricerca nella lista
    start = time.time_ns()
    trovati = 0
    for v in range(1, 10):
        if random.randint(1, 1000000000) in lista:
            trovati += 1
    end = time.time_ns()

    print(
        f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}"
    )

if False:
    #####################################################################à
    # Costruzione del set
    start = time.time_ns()
    aSet = set()
    for v in range(1, 10000000):
        aSet.add(random.randint(1, 1000000000))
    end = time.time_ns()

    print(f"Il tempo richiesto è: {(end-start)/1000000000}")

    # Ricerca nella lista
    start = time.time_ns()
    trovati = 0
    for v in range(1, 10000000):
        if random.randint(1, 1000000000) in aSet:
            trovati += 1
    end = time.time_ns()

    print(
        f"Il tempo richiesto per cercare è: {(end-start)/1000000000} e ne ha trovati {trovati}"
    )

print(hash("Ciao"))
print(hash("Cioa"))
print(hash("3"))

print(hash("Mario") % 17)
print(hash("Rossi") % 17)
print(hash("Verdi") % 17)
print(hash("Bianchi") % 17)
print(hash("Neri") % 17)
print(hash("Bianchini") % 17)
print(hash("Rossini") % 17)
print(hash("Verdini") % 17)
print(hash("Giallini") % 17)
print(hash("Nerini") % 17)
