# Równoległa metoda sortowania z wykorzystaniem pakietu multiprocessing.

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


def parallel_sort(array, processes):
    # Funkcja sortująca równolegle
    with multiprocessing.Pool(processes) as pool:
        chunk_size = len(array) // processes
        chunks = [array[i * chunk_size:(i + 1) * chunk_size] for i in range(processes)]
        sorted_chunks = pool.map(merge_sort, chunks)
    return merge_sort([item for sublist in sorted_chunks for item in sublist])


def test_parallel_sort(processes, sizes):
    # Funkcja testująca wydajność sortowania
    times = []
    for size in sizes:
        arr = [random.randint(0, 100) for _ in range(size)]
        start = time.time()
        parallel_sort(arr, processes)
        end = time.time()
        times.append(end - start)
    return times


if __name__ == "__main__":
    processes = [1, 2, 4, 8]
    sizes = [100, 1000, 10000]

    # Rysowanie wykresu wyników testów
    for process in processes:
        times = test_parallel_sort(process, sizes)
        plt.plot(sizes, times, label=f'{process} processes')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Size of data')
    plt.ylabel('Time (s)')
    plt.legend()
    plt.show()

# Opis algorytmu:
# Program implementuje równoległe sortowanie przez scalanie (merge sort)
# z użyciem multiprocessing. Funkcja `merge_sort` dzieli dane na mniejsze części
# i sortuje je rekurencyjnie, a funkcja `parallel_sort` dzieli dane na segmenty,
# które są sortowane równolegle. Na końcu testowana jest wydajność przy różnych
# rozmiarach danych oraz liczbach procesów, a wyniki są przedstawiane na wykresie.
