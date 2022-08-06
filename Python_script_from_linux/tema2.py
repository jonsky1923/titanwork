#Sa se scrie o secventa de cod care afiseaza toate numerele de tip palindrom, pana la o limita citita de la tastatura
'''
a = input("Introduceti stringul:")
if a == a[::-1]:
    print("Stringul este palindorm")
else:
    print("Nu este palindrom")
'''
n = int(input(" Please Enter the Maximum Value : "))
for i in range(1, n + 1):
    init = i
    rast = 0
    while (init > 0):
        rast = (rast * 10) + (init % 10)
        init = init // 10
    if (i == rast):
        print(i, end='  ')


