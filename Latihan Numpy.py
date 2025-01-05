#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

import numpy as np

suhu_celsius = np.array([29.5, 30.2, 28.7, 31.0, 30.8, 29.9, 28.4, 29.7, 30.1, 29.3])

suhu_fahrenheit = suhu_celsius * 9/5 + 32

print("Suhu dalam Celsius:", suhu_celsius)
print("Suhu dalam Fahrenheit:", suhu_fahrenheit)
