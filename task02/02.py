import heapq

def merge_k_lists(lists):
    # Створюємо мінімальну купу
    min_heap = []
    result = []

    # Додаємо перші елементи всіх списків до купи разом з індексами списку та елементу
    for i, lst in enumerate(lists):
        if lst:  # Перевіряємо, що список не порожній
            heapq.heappush(min_heap, (lst[0], i, 0))

    # Виконуємо злиття списків
    while min_heap:
        # Витягуємо найменший елемент із купи
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        # Якщо в поточному списку є ще елементи, додаємо наступний до купи
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_value, list_index, element_index + 1))

    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)