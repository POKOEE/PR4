# Задание 3. Вариант 5. Расписание автобусного маршрута

def parse_time(s):
    """Преобразует строку "HH:MM" в минуты от начала суток"""
    h, m = map(int, s.split(":"))
    return h * 60 + m

def format_time(minutes):
    """Преобразует минуты в строку "HH:MM" """
    h = (minutes // 60) % 24
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

# Ввод
print("Начало работы маршрута (HH:MM):")
start_str = input("  Начало: ")              # например 6:00
end_str = input("  Конец: ")                 # например 24:00

route_time = int(input("Протяжённость маршрута в одну сторону (минут): "))
rest = int(input("Время отдыха на конечной остановке (минут): "))

# Преобразуем
start = parse_time(start_str)
end = parse_time(end_str)

# Расписание
current = start
point = "A"  # начальный пункт
schedule = []

while current <= end:
    schedule.append((format_time(current), point))
    # Автобус едет в другой конец и отдыхает
    current += route_time + rest
    point = "B" if point == "A" else "A"

# Вывод
print("\n========== РАСПИСАНИЕ ==========")
print(f"Маршрут: A ↔ B, время в пути: {route_time} мин, отдых: {rest} мин")
print(f"Работа: с {start_str} до {end_str}\n")
print(f"{'№':<5}{'Время':<10}{'Пункт'}")
print("-" * 25)
for i, (t, p) in enumerate(schedule, 1):
    print(f"{i:<5}{t:<10}{p}")