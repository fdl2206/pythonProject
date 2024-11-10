#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPL 1A

gender = input("Masukan gender (wanita/pria): ").strip().lower()
umur = int(input("Masukan umur: "))
tinggi_badan = int(input("Masukan tinggi badan (cm): "))
iq = int(input("Masukan IQ: "))

if 18 <= umur <= 25:
    if gender == "wanita" and tinggi_badan >= 170 and iq >= 130:
        print("Selamat, anda memenuhi syarat untuk menjadi model catwalk.")
    elif gender == "pria" and tinggi_badan >= 175 and iq >= 130:
        print("Selamat, anda memenuhi syarat untuk menjadi model catwalk.")
    else:
        print("Maaf, anda tidak memenuhi syarat tinggi badan atau IQ untuk menjadi model catwalk.")
else:
    print("Maaf, anda tidak memenuhi umur untuk menjadi model catwalk.")