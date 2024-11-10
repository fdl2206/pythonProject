#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: 1A

students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}

count_students = {}

for value in students.values():
    if value in count_students:
        count_students[value] += 1
    else:
        count_students[value] = 1

for value, count in count_students.items():
    print(f"prodi {value} sebanyak {count}")


