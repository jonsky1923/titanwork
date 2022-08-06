#verificare string de la tastatura
a = input("Introduceti un string de la tastatura:")
if  str.isdigit(a):
    print("Stringul se transforma in numar intreg",int(a))
else:
    print("Numarul nu este format doar din cifre")