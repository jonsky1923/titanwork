# Inversarea unui numar
a = str(input("introduceti numarul dorit:"))
if str.isdigit(a):
    print("Numarul invers este:", a[::-1])
else:
    print("Numarul nu este format din cifre")
