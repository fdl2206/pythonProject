#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

total = 0

while True:
    angka = int(input("Masukkan angka (input negatif untuk berhenti): "))
    if angka < 0:
        break
    total += angka

    print("Jumlah dari semua angka yang diinputkan adalah:", total)