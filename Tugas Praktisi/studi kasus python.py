#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

import os

file_name = "nilai_siswa.txt"

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        total = 0
        count = 0
        
        for line in lines:
            try:
                name, score = line.strip().split(":")
                score = int(score.strip())
                total += score
                count += 1
            except ValueError:
                print(f"Format salah pada baris: {line}")
        
        if count > 0:
            avg = total / count
            print(f"Nilai rata-rata kelas: {avg:.2f}")
        else:
            print("Tidak ada data nilai yang valid.")
else:
    print("File nilai_siswa.txt tidak ditemukan.")
