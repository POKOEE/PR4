# Задание 2. Вариант 5. Разложение cos(x) в ряд Тейлора
import math

x = float(input("Введите x: "))
eps = float(input("Введите точность ε (например, 1e-6): "))

S = 1.0          # сумма ряда, начинаем с 1
term = 1.0       # текущий член ряда
n = 0            # счётчик итераций

while abs(term) >= eps:
    n += 1
    # Следующий член: term_n = term_{n-1} * (-x²) / ((2n-1)(2n))
    term *= -(x * x) / ((2 * n - 1) * (2 * n))
    S += term

print(f"\nРазложение cos({x}) = {S}")
print(f"Значение math.cos({x}) = {math.cos(x)}")
print(f"Разница: {abs(S - math.cos(x))}")
print(f"Количество итераций: {n}")