#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")
print(buah[2:6])
x = list(buah)
x.pop(3)
buah = tuple(x)
print(buah)
x = list(buah)
x.insert(2, "manggis")
buah = tuple(x)
print(buah)