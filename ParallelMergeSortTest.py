# Testowanie równoległej metody sortowania z różnymi rozmiarami danych wejściowych oraz liczbą procesów.

import multiprocessing
import random
import time
import matplotlib.pyplot as plt


def merge_sort(array):
    # Sortowanie przez scalanie (rekurencyjnie)
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    # Funkcja scalająca dwie posortowane listy
    merged_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    return merged_array


def parallel_merge_sort(array, pool):
    # Funkcja sortująca z wykorzystaniem puli procesów
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = pool.apply_async(merge_sort, args=(left,))
    right = pool.apply_async(merge_sort, args=(right,))
    left = left.get()
    right = right.get()

    return merge(left, right)


def test_parallel_merge_sort(processes, sizes):
    # Funkcja testująca czas wykonania sortowania z różnymi ustawieniami
    times = []
    for size in sizes:
        arr = [random.randint(0, 100) for _ in range(size)]
        pool = multiprocessing.Pool(processes)
        start = time.time()
        parallel_merge_sort(arr, pool)
        end = time.time()
        times.append(end - start)
    return times


if __name__ == "__main__":
    processes = [1, 5, 10, 20]
    sizes = [100, 1000, 100000, 1000000, 10000000]

    # Rysowanie wykresu wyników testów
    for process in processes:
        times = test_parallel_merge_sort(process, sizes)
        plt.plot(sizes, times, label=f'{process} processes')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Size of data')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

# Opis algorytmu:
# Ten kod testuje równoległą wersję sortowania przez scalanie przy użyciu wielu procesów.
# Funkcja `parallel_merge_sort` wykonuje sortowanie na podzielonych fragmentach
# listy z użyciem puli procesów. Funkcja `test_parallel_merge_sort` zbiera czas
# wykonania dla różnych rozmiarów danych oraz różnych liczb procesów, a wyniki są
# przedstawione na wykresie dla analizy wydajności.
