import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cables)
    total_cost = 0

    # Об'єднуємо два найменших кабелі доти, доки в купі залишиться один кабель
    while len(cables) > 1:
        # Виймаємо два найменших елементи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Витрати на з'єднання
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
result = min_cost_to_connect_cables(cables)
print("Мінімальні загальні витрати на з'єднання кабелів:", result)