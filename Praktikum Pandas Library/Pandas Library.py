import pandas as pd

list1 = {"Andi", "Budi", "Caca", "Deni"}
list2 = {"RPL", "Multimedia", "PGSD", "PGPAUD"}
list3 = {3.0, 3.4, 3.8, 4.0}

dataframeList = pd.DataFrame(list(zip(list1, list2, list3)), columns=['Nama', 'Prodi', 'IPK'])
print(dataframeList)