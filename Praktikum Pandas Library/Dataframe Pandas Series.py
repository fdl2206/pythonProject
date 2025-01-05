import pandas as pd

series1 = ("Harry Potter", "Detective Conan", "Naruto")
series2 = (20, 4, 10)
series3 = ("Available", "Available", "Not Available")
dataframeSeries = pd.DataFrame({"Judul Buku": series1, "Stok Buku": series2, "Status": series3})

print(dataframeSeries)