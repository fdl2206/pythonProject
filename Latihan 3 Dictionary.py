#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: 1A

student_info = {
    "Alice": {"age": 20, "major": "Computer Science"},
    "Bob": {"age": 21, "major": "Mathematics"},
    "Charlie": {"age": 19, "major": "Physics"}
}

student_name = input("Inputkan nama siswa: ")

if student_name in student_info:
    info = student_info[student_name]
    print(f"Umur {student_name} adalah {info['age']} dan Prodi nya adalah {info['major']}")
else:
    print(f"Siswa {student_name} tidak ditemukan")