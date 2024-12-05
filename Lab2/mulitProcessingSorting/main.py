import multiprocessing as mp
from typing import List
import time
import random
import matplotlib.pyplot as plot



def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def mergeSort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    mid = len(array) // 2  # Floor divide

    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    return merge(left, right)


def parallelMergeSort(array: List[int], processes: int = None) -> List[int]:

    if processes is None:
        processes = mp.cpu_count()

    chunk_size = len(array) // processes

    chunks = [array[i:i + chunk_size] for i in range(0, len(array), chunk_size)]

    with mp.Pool(processes=processes) as pool:
        sorted_chunks = pool.map(mergeSort, chunks)

    while len(sorted_chunks) > 1:
        paired_chunks = [(sorted_chunks[i], sorted_chunks[i+1])
                             for i in range(0, len(sorted_chunks)-1,2)]

        if len(sorted_chunks) % 2 != 0:
            paired_chunks.append((sorted_chunks[-1], []))

        sorted_chunks = [merge(left, right) for left, right in paired_chunks]


    return sorted_chunks[0]


def main():
    test_list = [10, 1000, 100_000, 500_000, 1_000_000, 10_000_000]
    s_test_results = []
    mp_test_results = []

    whole_time_start = time.time()
    for unit in test_list:
        print(f"Iteration {unit}")
        unsorted = [random.randint(0, 1000000) for _ in range(unit)]

        # Seq time measure
        s_time_start = time.time()
        sorted = mergeSort(unsorted)
        s_time_stop = time.time()

        # Pararralel time measue
        mp_time_start = time.time()
        mp_sorted = parallelMergeSort(unsorted)
        mp_time_stop = time.time()

        s_test_results.append(s_time_stop - s_time_start)
        mp_test_results.append(mp_time_stop - mp_time_start)

    whole_time_stop = time.time()
    print(f"Computing time: {whole_time_stop - whole_time_start}")
    fig, ax = plot.subplots(figsize=(12,8))
    x = [str(s) for s in test_list]

    #ax.plot(test_list, s_test_results)
    #ax.plot(test_list, mp_test_results)

    ax.set_xlabel("Rozmiar danych")
    ax.set_ylabel("Czas wykonania [s]")

    plot.bar([str(x) for x in test_list], s_test_results, align='center', color='dodgerblue', width=0.4)
    plot.bar([str(x) for x in test_list], mp_test_results, align='center', color='gold', width=0.2)

    plot.grid(True)
    plot.grid(axis='x')

    plot.legend(['Sortowanie sekwencyjne','Sortowanie równoległe'])
    plot.show()


if __name__ == "__main__":
    main()
