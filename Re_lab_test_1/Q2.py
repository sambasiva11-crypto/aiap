import time
import random

# -------------------------------
# Bubble Sort
# -------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# -------------------------------
# Insertion Sort
# -------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# -------------------------------
# Generate random list
# -------------------------------
size = 2000   # you can increase size to see bigger difference
data = [random.randint(1, 5000) for _ in range(size)]

# Copy list for both algorithms
data_bubble = data.copy()
data_insertion = data.copy()


# -------------------------------
# Measure Bubble Sort time
# -------------------------------
start = time.time()
bubble_sort(data_bubble)
bubble_time = time.time() - start


# -------------------------------
# Measure Insertion Sort time
# -------------------------------
start = time.time()
insertion_sort(data_insertion)
insertion_time = time.time() - start


# -------------------------------
# Print Results
# -------------------------------
print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
