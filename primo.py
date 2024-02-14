from math import asin, cos, radians, sin, sqrt

print("Hello world")
print(3**1001)
print(sqrt(10))


# Esercizio per casa
# dato un triangolo rettangolo i cui cateti sono lunghi rispettivamente
# 10.123 e 30.456
# calcolare la lunghezza dell'ipotenusa
print("Ipotenusa = ", sqrt(10.123**2 + 30.456**2))
print("Esercizi terminati")

lat_o = 59.9
long_o = 10.8
lat_v = 49.3
long_v = -123.1

lat_o = radians(lat_o)
long_o = radians(long_o)
lat_v = radians(lat_v)
long_v = radians(long_v)

r = 6371

el1 = sin(1 / 2 * (lat_v - lat_o)) ** 2
el2 = cos(lat_o) * cos(lat_v) * sin(1 / 2 * (long_v - long_o)) ** 2
d = 2 * r * asin(sqrt(el1 + el2))
print("Distanza: ", d)
