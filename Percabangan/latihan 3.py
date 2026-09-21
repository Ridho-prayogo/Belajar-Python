# latihan 3

nilai = int(input("Masukkan nilai: "))

if nilai >= 75 and nilai <= 100:
    print("Selamat, Anda lulus!")
elif nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
else:
    print("Maaf, Anda tidak lulus.")