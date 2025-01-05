import pandas as pd

tuple1 = ("Harry Potter", 20)
tuple2 = ("Detective Conan", 4)
tuple3 = ("Naruto", 10)
dataframeTuple = pd.DataFrame([tuple1, tuple2, tuple3], columns=['Judul Buku', 'Stok Buku'])

print(dataframeTuple)