import random
import time
import numpy as np
import matplotlib.pyplot as plt

# Рандомізований QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)

# Детермінований QuickSort (pivot - середній елемент)
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)

# Вимірювання часу виконання
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time

# Створення тестових масивів
array_sizes = [10_000, 50_000, 100_000, 500_000]
results = {}

for size in array_sizes:
    random_array = np.random.randint(-100_000, 100_000, size).tolist()
    randomized_times = [measure_time(randomized_quick_sort, random_array) for _ in range(5)]
    deterministic_times = [measure_time(deterministic_quick_sort, random_array) for _ in range(5)]

    results[size] = {
        "randomized": np.mean(randomized_times),
        "deterministic": np.mean(deterministic_times)
    }

# Вивід результатів у консоль
for size, times in results.items():
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {times['randomized']:.4f} секунд")
    print(f"   Детермінований QuickSort: {times['deterministic']:.4f} секунд")
    print()

# Побудова графіку
sizes = list(results.keys())
randomized_times = [results[size]["randomized"] for size in sizes]
deterministic_times = [results[size]["deterministic"] for size in sizes]

plt.figure(figsize=(10, 6))
plt.plot(sizes, randomized_times, marker='o', label='Рандомізований QuickSort')
plt.plot(sizes, deterministic_times, marker='o', label='Детермінований QuickSort')
plt.xlabel('Розмір масиву')
plt.ylabel('Час виконання (секунди)')
plt.title('Порівняльний аналіз ефективності QuickSort')
plt.legend()
plt.grid(True)
plt.show()
