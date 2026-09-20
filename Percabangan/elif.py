# elif

nilai = int(input("Masukkan Nilai Anda : "))
if nilai < 0 or nilai > 100:
    print("Nilai yang Anda Masukkan Tidak Valid :(")
elif nilai >= 80 :
    print("Selamat Anda Mendapatkan Nilai A :)")
elif nilai >= 70:
    print("Selamat Anda Mendapatkan Nilai B :)")
elif nilai >= 60:
    print("Selamat Anda Mendapatkan Nilai C :)")
elif nilai >= 50:
    print("Selamat Anda Mendapatkan Nilai D :)")
elif nilai >= 40:
    print("Selamat Anda Mendapatkan Nilai E :)")
else:
    print("Maaf Anda Tidak Lulus :(")

    
