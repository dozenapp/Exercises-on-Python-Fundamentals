import copy


print(10 / 3)
print(10 // 3)

# 10 = (10 // 3) * 3 + (10 % 3)
# ????
lista = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
lista.append(100)
print(lista)
print(lista[2])

lista[2] = 10
print(lista[2])

lista = list((1, 2, 3))
print(lista)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for v in thislist:
    print(v)


l1 = [1, 2]
l2 = ["aaaa", "bbb"]
l1.append(l2)

print(l1)
l2[1] = "ccc"

print(l1)
l1.clear()
print(l2)
l3 = l2

l2[0] = 10
print(l3)


L1 = [1, 2, 3]
L2 = L1
L1[1] = 100
print(L2)

L1 = [4, 5, 6]
print(L2)

L3 = [L1, 2, 3, 4]
L4 = [L3, L1, 5]

print("L4: ", L4)
# L5 = copy.copy(L4)
L5 = copy.deepcopy(L4)
print("L5: ", L5)
L3.append(10)
L1.append(1)
L4[2] = 100
print("L4: ", L4)
print("L5: ", L5)
L5[0][0][1] = 200
print("L5: ", L5)
L6 = L5[0][0]

L6.append("Ciao Ciao")
print("L5: ", L5)
