#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

arr = [2, 5, 8, 16, 91, 23, 38, 56, 72, 12]
search = 23

def binary_search(search, array_list):
    array_list.sort(reverse=True)
    print(array_list)

    left = 0
    right = len(array_list)-1
    while left <= right:
        mid = (left + right) // 2
        if array_list[mid] == search:
            return mid
        elif array_list[mid] < search:
            left = mid + 1
        else:
            right = mid - 1
    return -1