#Найти наибольший общий делитель трех заданных натуральных чисел, используя
#алгоритм Евклида и учитывая, что НОД(𝑎, 𝑏, 𝑐) = НОД(НОД(𝑎, 𝑏), 𝑐).

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcdofthreenumbers(a, b, c):
    gcd_ab = gcd(a, b)
    gcd_abc = gcd(gcd_ab, c)
    return gcd_abc

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

result = gcdofthreenumbers(a, b, c)
print(f"Наибольший общий делитель чисел {a}, {b} и {c} равен: {result}")

