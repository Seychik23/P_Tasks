# Написать программу вычисления значений функции
import math;
x = float(input("Введите x"))
y = float(input("Введите y"))
def calculate_z (x,y):
    q = 3 * math.cos(math.pi * x) - abs(2 - y)
    num = q+((2+q)/(q*q+3))
    den = 1/math.sqrt(q*q+8)
    z = num / den
    return z

z_value = calculate_z(x, y)

print("Значение функции z при x =",x,"y =",y, "равно:", z_value)

