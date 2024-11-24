print("#NOMOR 3")
def cek_kelulusan(nilai):
    if nilai >= 70:
        return "lulus"
    else :
        return "gagal"
    
nilai_saya = 90
status = cek_kelulusan(nilai_saya)
print(f"nilai:{nilai_saya}, status: {status}")
nilai_kamu = 60
status = cek_kelulusan(nilai_kamu)
print(f"nilai:{nilai_kamu}, status: {status}")

