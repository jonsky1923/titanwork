#afisare n numere pare
n = int(input("Introduceti numarul n: "))
i = 0
while i < n:
    if i % 2 ==0:
        print(i, end=" ")
    i+=1
print("\n")
print("Scriptul s-a terminat")