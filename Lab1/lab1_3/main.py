import random

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key, j = arr[i], i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1], j = arr[j], j - 1
        arr[j + 1] = key
    return arr

def main():
    numbers = [random.randint(0, 1000) for _ in range(20)]
    print("Original:", numbers)
    print("Bubble sort:", bubble_sort(numbers.copy()))
    print("Insertion sort:", insertion_sort(numbers.copy()))
    print("Built-in sort:", sorted(numbers))

if __name__ == "__main__":
    main()