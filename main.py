#Задание 1
#подключаем библиотеку для генерации случайных чисел
"""import random
#ввод данных
n = int(input("Введите размер списка -> "))
#создание и заполнение списка размера N
numbers = [random.randint(1,100) for _ in range(n)]
#вывод данных о списке
print(f"Исходный список: {numbers}")
print(f"Cумма: {sum(numbers)}")
print(f"Среднее: {sum(numbers) / len(numbers):.2f}")
print(f"Минимум: {min(numbers)}")
print(f"Максимум: {max(numbers)}")
#сортировка списка
numbers.sort()
print(f"Отсортированный список: {numbers}")
#Удаление дубликатов в списке (с сохранением порядка)
unique = list(dict.fromkeys(numbers))
print(f"Без дубликатов: {unique}")

#Задание 2
#создание списка
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
#через словать с подсчетом
from collections import Counter
counts = Counter(numbers)
dublicates = [num for num, count in counts.items() if count > 1]
#вывод дубликатов
print(f"Дубликаты: {dublicates}")

#через множества
seen = set()
dublicates2 = set()
for num in numbers:
    if num in seen:
        dublicates2.add(num)
    seen.add(num)
#вывод дубликатов
print(f"Дубликаты через множества: {list(dublicates2)}")

#Задание 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#через zip
transposed = [list(row) for row in zip(*matrix)]
#вывод
print(f"Исходная матрица: ")
for row in matrix:
    print(row)
print(f"Транспонированная матрица: ")
for row in transposed:
    print(row)"""

#Задание 4
students = [
    ("Иван", 25, 4.5),
    ("Мария", 22, 4.8),
    ("Петр", 30, 4.2),
    ("Анна", 20, 4.9),
]
# самый старший
oldest = max(students, key=lambda s: s[1])
print(f"Самый старший: {oldest[0]}, {oldest[1]} лет")
# с самым высоким баллом
best = max(students, key=lambda s: s[2])
print(f"Лучший студент: {best[0]}, {best[2]}")
# средний возраст
avg_age = sum(s[1] for s in students) / len(students)
print(f"Средний возраст: {avg_age:.1f} лет")
# сортировка по баллу (убывание)
sorted_students = sorted(students, key=lambda s: s[2], reverse=True)
print("По баллу:")
for name, age, grade in sorted_students:
    print(f"{name}: {grade}")