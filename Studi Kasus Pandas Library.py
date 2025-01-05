#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

import pandas as pd

file_path = "Daftar_Mahasiswa_2018.csv"
df = pd.read_csv(file_path)

print("10 data teratas:")
print(df.head(10))

df_sorted = df.sort_values(by="Nama")
print("\nData setelah sorting berdasarkan nama:")
print(df_sorted)

columns_to_show = ["NIM", "Nama", "L/P", "Status", "SKS", "IPK", "Lama Studi(Smt)"]
df_selected = df_sorted[columns_to_show]
print("\nData dengan Kolom yang Dipilih:")
print(df_selected.head(10))

average_ipk = df["IPK"].mean()
print(f"\nRata-Rata IPK Mahasiswa: {average_ipk:.2f}")

gender_count = df["L/P"].value_counts()
print("\nJumlah Mahasiswa Laki-laki dan Perempuan:")
print(gender_count)

female_registered = df[(df["L/P"] == "P") & (df["Status"] == "Terdaftar")]
print("\nData Mahasiswa Perempuan dengan Status 'Terdaftar':")
print(female_registered)

not_registered = df[df["Status"] != "Terdaftar"]
print("\nData Mahasiswa dengan Status Bukan 'Terdaftar':")
print(not_registered)