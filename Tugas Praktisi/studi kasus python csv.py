#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

import csv
import os

file_name = "inventaris_barang.csv"

if os.path.exists(file_name):
    barang = []
    with open(file_name, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            nama_barang, jumlah = row[0], int(row[1])
            barang.append([nama_barang, jumlah])
    
    print("Data inventaris sebelum update:")
    print(barang)

    pengurangan_stok = {
        "Laptop": 2,
        "Printer": 3,
        "Mouse": 5,
        "Monitor": 1,
        "RAM": 10,
    }

    for item in barang:
        nama_barang = item[0]
        if nama_barang in pengurangan_stok:
            item[1] -= pengurangan_stok[nama_barang]

    print("Data inventaris setelah update:")
    print(barang)
    
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(barang)
else:
    print("File inventaris_barang.csv tidak ditemukan.")
