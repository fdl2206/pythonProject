#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

stored_password = "Latihan"

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    entered_password = input("Masukkan password: ")
    if entered_password == stored_password:
        print("Login berhasil")
        break
    else:
        attempts += 1
        print("Password salah. Anda memiliki", max_attempts - attempts, "kesempatan lagi.")
        if attempts == max_attempts:
            print("Login gagal. Anda telah melebihi batas percobaan.")