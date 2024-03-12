import math


a = 10
b = 20
c = 30

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

# Supponiamo di aver scelto la tecnica con il modulo
a = 10
b = 20
c = 30

if a % 2 == 0:
    print(b + c)
else:
    print(b - c)
