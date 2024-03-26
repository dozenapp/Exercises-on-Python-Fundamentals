import random


l1 = []

for i in range(5):
    l1.append(random.randrange(10))

print(l1)
for v in l1:
    print(v)

# Stampa i numeri da 0 a 6
for v in range(7):
    print(v)

for v in range(len(l1)):
    print(l1[v])


# Esercizio
# Stampare la tabellina del 23
for i in range(10):
    print(23 * (i + 1), end=" ")
print()

for i in range(1, 11):
    print(23 * i, end=" ")
print()

t = 23
for i in range(10):
    print(t, end=" ")
    t = t + 23
print()

for i in range(23, 23 * 11, 23):
    print(i, end=" ")
print()

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([i * 23 for i in v])

print(list(map(lambda i: i * 23, v)))
