# 03_kelulusan_bersyarat.py
# Program menentukan kelulusan mahasiswa berdasarkan nilai dan kehadiran

nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")
