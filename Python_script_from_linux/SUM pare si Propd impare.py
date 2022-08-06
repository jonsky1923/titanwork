#2. Sa se scrie o secventa de cod care calculeaza suma numerelor pare si produsul
# numerelor impare pana la o limita n citita de la tastatura.
import math
n = int(input("Introduceti limita n:"))
s = 0
p = 1
while n:
    n -= 1
    if n % 2 == 0:
        s = s + n
    elif n % 2 != 0:
        p = p * n
print("Suma numerelor pare este:", s)
print("Produsul numerelor impare este:", p)
