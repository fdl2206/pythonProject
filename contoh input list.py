# Daftar nilai murid, misal ada 10 murid dengan nilai acak
nilai_murid = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]

# Menampilkan daftar nilai murid (nomor urut dan nilai)
print("Daftar nilai murid:")
for i, nilai in enumerate(nilai_murid, start=1):
    print(f"Nomor urut {i}: Nilai {nilai}")

# Meminta input nomor urut murid dari guru
try:
    nomor_urut = int(input("\nMasukkan nomor urut murid untuk melihat nilainya (1-10): "))
    
    # Memeriksa apakah nomor urut valid
    if 1 <= nomor_urut <= len(nilai_murid):
        print(f"Nilai murid dengan nomor urut {nomor_urut}: {nilai_murid[nomor_urut - 1]}")
    else:
        print("Nomor urut yang dimasukkan tidak valid. Silakan masukkan nomor urut antara 1-10.")

except ValueError:
    print("Input tidak valid. Masukkan nomor urut berupa angka.")
