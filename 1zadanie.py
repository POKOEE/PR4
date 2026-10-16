# Задание 1. Сумма чисел от A до B
A = int(input("Введите A: "))
B = int(input("Введите B (B > A): "))

if A >= B:
    print("Ошибка: A должно быть меньше B!")
else:
    S = 0
    for i in range(A, B + 1):
        S += i
    print(f"Сумма чисел от {A} до {B} = {S}")