#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

stok_toko = [
    "Buku", "Pensil", "Pulpen", "Penggaris", "Penghapus",
    "Spidol", "Kertas A4", "Kertas A3", "Kalkulator", "Stapler",
    "Map Folder", "Amplop", "Clip Kertas", "Gunting", "Lakban"
]

def linear_search(stok, barang):
    for item in stok:
        if item.lower() == barang.lower():
            return True
    return False

nama_barang = input("Masukkan nama barang yang dicari: ")

if linear_search(stok_toko, nama_barang):
    print("Barang '{}' tersedia di stok.".format(nama_barang))
else:
    print("Barang '{}' tidak tersedia di stok.".format(nama_barang))