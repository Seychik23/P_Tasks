def palindrome_check(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num1 = int(input("Введите первое натуральное число: "))
num2 = int(input("Введите второе натуральное число: "))

if palindrome_check(num1) or palindrome_check(num2):
    print("Хотя бы одно из чисел является палиндромом!")
else:
    print("Ни одно из этих чисел не является палиндромом!")