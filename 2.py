"Напишіть програму для сортування трьох цілих чисел без використання умовних виразів і циклів. Виконав Петюх О.В."

# Введення трьох цілих чисел
a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

# Створення списку з введених чисел
numbers = [a, b, c]

# Використання вбудованої функції сортування для сортування списку
numbers.sort()

# Виведення відсортованих чисел
print("Відсортовані числа:", numbers)
