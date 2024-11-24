print("#NOMOR 2")
def genap_ganjil(bilangan):
    hitung = bilangan % 2 ==0
    return hitung

angka1 = 4
hasil = genap_ganjil(angka1)
print(f"bilangan {angka1} bernilai {hasil}")
angka2 = 7
hasil = genap_ganjil(angka2)
print(f"bilangan {angka2} bernilai {hasil}")
