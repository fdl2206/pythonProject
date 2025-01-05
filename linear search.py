#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 15, 30, 70, 80, 20, 60, 90]
target = 80
result = linear_search(arr, target)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")