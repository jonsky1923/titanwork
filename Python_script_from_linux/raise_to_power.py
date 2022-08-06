a = float(input("Scrieti o baza:"))
b = int(input("va rog sa scrieti o putere:"))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(a, b))