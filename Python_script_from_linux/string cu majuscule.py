#String cu majuscule && daca este format si din cifre
a = input("Va rog introduceti un string pt a:")
b = input("Va rog introduceti un string pt b:")
print("Se afiseaza stringul cu majuscule:", str.upper(a))
print("Se afiseaza daca stringul este doar din cifre", str.isdigit(b))