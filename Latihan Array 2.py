#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

import numpy as np

nilai_ujian = np.random.randint(0, 101, 30)
nilai_ujian_sorted = np.sort(nilai_ujian)[::-1]

print("Nilai ujian (terurut dari terbesar ke terkecil):")
print(nilai_ujian_sorted)

nilai_tertinggi = nilai_ujian_sorted[:5]
print("\n5 nilai tertinggi:")
print(nilai_tertinggi)