# Daftar barang pada bulan Maret
barang_maret = ["kemeja", "seragam", "celana", "kaus kaki"]

# Menampilkan daftar barang dan jumlah pada bulan Maret
print("Daftar barang pada bulan Maret:")
for barang in barang_maret:
    print(f"- {barang}")
print("Jumlah barang pada bulan Maret:", len(barang_maret))

# Update daftar barang untuk bulan selanjutnya
barang_bulan_selanjutnya = barang_maret.copy()  # Copy daftar Maret
barang_bulan_selanjutnya.remove("kaus kaki")    # Menghapus kaus kaki
barang_bulan_selanjutnya.extend(["jaket", "jas"])  # Menambahkan jaket dan jas

# Menampilkan daftar barang dan jumlah pada bulan selanjutnya
print("Daftar barang pada bulan selanjutnya:")
for barang in barang_bulan_selanjutnya:
    print(f"- {barang}")
print("Jumlah barang pada bulan selanjutnya:", len(barang_bulan_selanjutnya))
