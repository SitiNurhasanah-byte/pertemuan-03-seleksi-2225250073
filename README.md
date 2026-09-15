# Pertemuan 03 Seleksi Python
Nama: Siti Nurhasanah  
NIM: 2225250073  
Kelas: 3B  

---

## 🎯 Tujuan
Menulis program seleksi `if`, `if-else`, kondisi majemuk, dan `nested if` untuk berbagai kasus sederhana.

---

## 🚀 Cara Menjalankan
Setiap program dijalankan dari terminal dengan perintah:

Folder latihan
python3 latihan/01_genap_ganjil.py
python3 latihan/02_bandingkan_dua_bilangan.py
python3 latihan/03_kelulusan_bersyarat.py
python3 latihan/04_jenis_segitiga.py

Folder tugas
python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas

1. Program membaca input koefisien `a`, `b`, dan `c` sebagai bilangan float.
2. Periksa apakah `a = 0`.  
   - Jika ya, tampilkan pesan "Bukan persamaan kuadrat".
3. Jika `a ≠ 0`, hitung diskriminan `D = b ** 2 - 4 * a * c`.
4. Gunakan nested if untuk memeriksa nilai D:
   - Jika `D > 0`, hitung dua akar real berbeda dengan rumus:
     - `x1 = (-b + (D ** 0.5)) / (2 * a)`
     - `x2 = (-b - (D ** 0.5)) / (2 * a)`
   - Jika `D = 0`, hitung akar kembar dengan rumus:
     - `x = -b / (2 * a)`
   - Jika `D < 0`, tampilkan pesan "Tidak ada akar real".
5. Semua hasil ditampilkan dengan format dua angka di belakang koma.
# analisis_persamaan_kuadrat.py
# Program untuk menganalisis persamaan kuadrat ax^2 + bx + c = 0
# Termasuk dokumentasi hasil pengujian

print("Analisis Persamaan Kuadrat")

a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    D = b ** 2 - 4 * a * c
    print(f"Diskriminan = {D:.2f}")

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print(f"Dua akar real berbeda: x1 = {x1:.2f}, x2 = {x2:.2f}")
    else:
        if D == 0:
            x = -b / (2 * a)
            print(f"Akar real kembar: x = {x:.2f}")
        else:
            print("Tidak ada akar real.")

# Dokumentasi hasil pengujian
print("\n=== Hasil Pengujian ===")
print("| a | b  | c | D   | Output yang Diharapkan | Output Aktual | Status |")
print("|---|----|---|-----|------------------------|---------------|--------|")
print("| 1 | -5 | 6 | 1   | Dua akar real: 3 dan 2 | Dua akar real: 3.00 dan 2.00 | ✅ |")
print("| 1 | 2  | 1 | 0   | Akar kembar: -1        | Akar kembar: -1.00           | ✅ |")
print("| 1 | 0  | 1 | -4  | Tidak ada akar real    | Tidak ada akar real          | ✅ |")
print("| 0 | 2  | 3 | -   | Bukan persamaan kuadrat| Bukan persamaan kuadrat      | ✅ |")

# Refleksi:

Kesalahan logika yang pernah ditemukan adalah lupa menambahkan tanda kurung pada penyebut (2*a).
Awalnya ditulis (-b + D**0.5) / 2 * a, sehingga hasil akar salah karena pembagian hanya dengan 2 lalu dikali a.
Perbaikan dilakukan dengan menuliskan rumus lengkap (-b ± (D**0.5)) / (2*a).
Dengan perbaikan ini, hasil akar sesuai teori persamaan kuadrat.
