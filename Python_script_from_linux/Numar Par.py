#se verifica paritatea unui numar
a = float(input("Introduceti valoarea lui a: "))
if a % 2 == 0 and a != 0:
    print("Este numar par")
elif a == 0:
    print("Numarul introdus este 0")
else:
    print("Nu este numar par")