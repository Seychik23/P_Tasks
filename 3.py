def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(a, b):
    common_divisor = gcd(a, b)
    return a // common_divisor, b // common_divisor

a = int(input("Input a"))
b = int(input("Input b"))
p, q = simplify_fraction(a, b)

print(f"The simplified fraction of {a}/{b} is {p}/{q}")