import random
import timeit

# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Генерація наборів даних
def generate_data(size):
    random_data = [random.randint(0, 10000) for _ in range(size)]
    sorted_data = sorted(random_data)
    partially_sorted_data = sorted(random_data[:size // 2]) + random_data[size // 2:]
    return random_data, sorted_data, partially_sorted_data

# Функція для заміру часу
def measure_time(func, arr):
    return timeit.timeit(lambda: func(arr.copy()), number=1)

# Функція для проведення тестів
def run_tests():
    sizes = [1000, 5000, 10000]  # Розміри масивів для тестування
    for size in sizes:
        random_data, sorted_data, partially_sorted_data = generate_data(size)

        print(f"\n--- Результати для масиву розміру {size} ---")

        # Тестування сортування вставками
        print("\nСортування вставками: =>")
        print("Випадковий масив:", measure_time(insertion_sort, random_data))
        print("Частково відсортований масив:", measure_time(insertion_sort, partially_sorted_data))
        print("Вже відсортований масив:", measure_time(insertion_sort, sorted_data))

        # Тестування сортування злиттям
        print("\nСортування злиттям:  =>")
        print("Випадковий масив:", measure_time(merge_sort, random_data))
        print("Частково відсортований масив:", measure_time(merge_sort, partially_sorted_data))
        print("Вже відсортований масив:", measure_time(merge_sort, sorted_data))

        # Тестування Timsort (вбудовані sorted або sort)
        print("\nTimsort:  =>")
        print("Випадковий масив:", measure_time(sorted, random_data))
        print("Частково відсортований масив:", measure_time(sorted, partially_sorted_data))
        print("Вже відсортований масив:", measure_time(sorted, sorted_data))

# Запуск тестів
run_tests()
