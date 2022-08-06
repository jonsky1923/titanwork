#verificare lungime string cu numar intreg
a = str(input("Introduceti valoarea unui string: "))
b = int(input("Introduceti valoarea unui numar intreg: "))
if len(a) == b and b != 0:
    print("Lungimea stringului este egala cu numarul intreg")
else:
    print("Lungimea stringului nu este egala cu numarul intreg")