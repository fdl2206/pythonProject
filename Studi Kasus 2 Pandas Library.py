#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

import pandas as pd

data = {
    "Tanggal": [
        "2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01",
        "2023-06-01", "2023-07-01", "2023-08-01", "2023-09-01", "2023-10-01",
        "2023-11-01", "2023-12-01"
    ],
    "Produk": [
        "Produk A", "Produk B", "Produk C", "Produk A", "Produk B",
        "Produk C", "Produk A", "Produk B", "Produk C", "Produk A",
        "Produk B", "Produk C"
    ],
    "Kategori": [
        "Elektronik", "Pakaian", "Makanan", "Elektronik", "Pakaian",
        "Makanan", "Elektronik", "Pakaian", "Makanan", "Elektronik",
        "Pakaian", "Makanan"
    ],
    "Harga": [
        1000000, 200000, 50000, 1200000, 210000,
        60000, 1100000, 190000, 55000, 1300000,
        220000, 65000
    ],
    "Jumlah": [
        5, 20, 50, 6, 15,
        55, 4, 25, 60, 7,
        18, 53
    ]
}

df = pd.DataFrame(data)
df["Total"] = df["Harga"] * df["Jumlah"]

print("Dataset Penjualan:")
print(df)

df["Bulan"] = pd.to_datetime(df["Tanggal"]).dt.month
total_per_bulan = df.groupby("Bulan")["Total"].sum()
print("\nTotal pendapatan setiap bulan:")
print(total_per_bulan)

rata_rata_pendapatan = df["Total"].mean()
print("\nRata-rata pendapatan tahun 2023:", rata_rata_pendapatan)

pendapatan_min = df["Total"].min()
pendapatan_max = df["Total"].max()
print("\nPendapatan paling sedikit:", pendapatan_min)
print("Pendapatan paling banyak:", pendapatan_max)

produk_terlaris = df.groupby("Produk")["Jumlah"].sum().idxmax()
print("\nProduk terlaris adalah:", produk_terlaris)