#Задание 1
#подключаем библиотеку для генерации случайных чисел
import random
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