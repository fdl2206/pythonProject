# Dictionary awal dengan keterangan mobil
mobil = {
    "merk": "Honda",
    "model": "Civic",
    "tahun": 2010,
    "warna": "Hitam"
}

# Menampilkan informasi mobil sebelum diganti
print("Informasi mobil sebelum diganti:")
for key, value in mobil.items():
    print(f"{key.capitalize()}: {value}")

# Mengganti keterangan mobil lama dengan yang baru
mobil["merk"] = "Pagani"
mobil["model"] = "Zonda"
mobil["tahun"] = 2021  # Misalnya tahun mobil baru
mobil["warna"] = "Perak"  # Misalnya warna mobil baru

# Menampilkan informasi mobil setelah diganti
print("\nInformasi mobil setelah diganti:")
for key, value in mobil.items():
    print(f"{key.capitalize()}: {value}")
