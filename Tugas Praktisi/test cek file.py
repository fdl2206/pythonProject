#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

import os

file_name = "file_list.txt"

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        
        lines = [line.strip() for line in lines]
        
        all_lines = " ".join(lines)
        
        fruits = all_lines.split()
        
        print("List nama buah:", fruits)
else:
    print("File tidak ditemukan.")
