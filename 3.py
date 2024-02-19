#Даны натуральные числа а и b, обозначающие соответственно числитель и знаменатель
#дроби. Сократить дробь, т. е. найти такие натуральные числа р и q, не имеющие общих
#делителей, что p/q = a/b

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplifyfraction(a, b):
    common_divisor = gcd(a, b)
    return a // common_divisor, b // common_divisor

a = int(input("Input a"))
b = int(input("Input b"))
p, q = simplifyfraction(a, b)

print(f"The simplified fraction of {a}/{b} is {p}/{q}")