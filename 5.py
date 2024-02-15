import random
import math

# Создаем исходный массив с случайными значениями
array = [random.randint(-10, 10) for _ in range(10)]
print("Исходный массив:", array)

# Сортируем исходный массив, чтобы сначала шли отрицательные элементы, затем остальные
sorted_array = sorted(array, key=lambda x: x >= 0)

print("Новый массив:", sorted_array)
