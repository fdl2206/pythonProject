#Nama: Muhammad Fadil Tallei
#NIM: 2403798
#Kelas: RPl 1A

def hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    waktu_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    waktu_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai
    selisih_detik = waktu_selesai - waktu_mulai
    jam = selisih_detik // 3600
    sisa_detik = selisih_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit, detik

jam_mulai = 8
menit_mulai = 10
detik_mulai = 20

jam_selesai = 9
menit_selesai = 15
detik_selesai = 30

jam, menit, detik = hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)
print("Selisih waktu adalah {} jam, {} menit, {} detik.".format(jam, menit, detik))