#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

daftar_mahasiswa = sorted([
    "Anaqi Ahza", "Bintang Kurniawan", "Dwi Cahyo","Dzaky Alfiansyah", "Erik Klaus",
    "Fadhil Anwar", "Fikri Raditya", "Hafizh Iltizam", "Harmoni Natanael", "Ikhsan Nurul", 
    "Juan Rezel", "Luthfil Hadi", "Muhammad Fadil", "Muhammad Firdiansyah", "Muhammad Ilham",
    "Muhammad Nawwaf", "Muhammad Yasir", "Nabil Rizky", "Nandana Rafi", "Zahran Faiz"
])

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

nama_yang_dicari = input("Masukkan nama mahasiswa yang dicari: ")

index = binary_search(daftar_mahasiswa, nama_yang_dicari)

if index != -1:
    print("Mahasiswa '{}' ditemukan di daftar mahasiswa pada indeks {}.".format(nama_yang_dicari, index))
else:
    print("Mahasiswa '{}' TIDAK ditemukan dalam daftar mahasiswa.".format(nama_yang_dicari))