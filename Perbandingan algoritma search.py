#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

import time

array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38,
         40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74,
         75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def measure_time(search_func, arr, target, iterations=1000):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        search_func(arr, target)
        end_time = time.time()
        total_time += (end_time - start_time)
    
    average_time = (total_time / iterations) * 1e6
    return average_time

target = 60

iterations = 10000

linear_time = measure_time(linear_search, array, target, iterations)

binary_time = measure_time(binary_search, array, target, iterations)

print(f"Linear Search: Average Execution Time: {linear_time:.2f} microseconds over {iterations} iterations")
print(f"Binary Search: Average Execution Time: {binary_time:.2f} microseconds over {iterations} iterations")
