import time
import random
import os

# Insertion Sort
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    return merge(L, R)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Radix Sort
def radix_sort(arr):
    a = arr.copy()
    RADIX = 10
    maxLength = False
    tmp, placement = -1, 1
    while not maxLength:
        maxLength = True
        buckets = [[] for _ in range(RADIX)]
        for i in a:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False
        a = [item for sublist in buckets for item in sublist]
        placement *= RADIX
    return a

# Dataset generation
def generate_datasets(sizes):
    for size in sizes:
        data = [random.randint(0, 2_147_483_647) for _ in range(size)]
        with open(f"input_{size}.txt", "w") as f:
            f.write("\n".join(map(str, data)))

# Read data
def read_input_file(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.readlines()))

# Time algorithm
def time_algorithm(algorithm, data):
    times = []
    for _ in range(5):
        start = time.time()
        algorithm(data)
        end = time.time()
        times.append(end - start)
    times.remove(max(times))
    return sum(times) / 4

# Run everything
def run_tests():
    sizes = [1000, 10000, 100000]
    algorithms = {
        "Insertion Sort": insertion_sort,
        "Bubble Sort": bubble_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
        "Radix Sort": radix_sort,
    }

    for size in sizes:
        print(f"\nTesting with dataset size: {size}")
        data = read_input_file(f"input_{size}.txt")
        for name, func in algorithms.items():
            if name in ["Insertion Sort", "Bubble Sort"] and size > 10000:
                print(f"{name}: > 20 minutes (skipped)")
                continue
            avg_time = time_algorithm(func, data)
            print(f"{name}: {avg_time:.4f} seconds")

if __name__ == "__main__":
    sizes = [1000, 10000, 100000]
    if not all(os.path.exists(f"input_{s}.txt") for s in sizes):
        generate_datasets(sizes)
        print("Datasets generated.")
    run_tests()