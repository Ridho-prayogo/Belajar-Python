# latihan 

umur = int(input("Masukkan umur anda: "))

if umur <= 0 or umur > 120:
    print("Umur tidak valid")
elif umur >= 18:
    print("Dewasa")
else:
    print("Belum Dewasa")