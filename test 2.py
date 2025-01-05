import os
filename = "file_list.txt"
if not os.path.isfile(filename): print("File tidak ditemukan")

with open(filename, 'r') as file:
    lines = file.readlines()
    lines = str(lines[0]).split(" ")
print(lines)