# readme_output.py
# Program untuk menampilkan isi README Pertemuan 03 Seleksi Python

def main():
    print("# Pertemuan 03 Seleksi Python")
    print("Nama: Siti Nurhasanah")
    print("NIM: 2225250073")
    print("Kelas: 3B\n")

    print("## Tujuan")
    print("Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.\n")

    print("## Cara Menjalankan")
    print("python3 tugas/analisis_persamaan_kuadrat.py\n")

    print("## Algoritma Tugas")
    print("1. Baca input dari pengguna.")
    print("2. Gunakan seleksi if atau nested if sesuai kebutuhan.")
    print("3. Tentukan kondisi yang harus dipenuhi (misalnya genap/ganjil, syarat segitiga, syarat kelulusan).")
    print("4. Hitung nilai tambahan jika diperlukan (misalnya diskriminan).")
    print("5. Tampilkan hasil sesuai cabang kondisi.\n")

    print("## Hasil Pengujian")
    print("| Program | Input | Output yang Diharapkan | Output Aktual | Status |")
    print("|---------|-------|-------------------------|---------------|--------|")
    print("| 01_genap_ganjil | 8 | 8 adalah bilangan genap | 8 adalah bilangan genap | ✅ |")
    print("| 01_genap_ganjil | 13 | 13 adalah bilangan ganjil | 13 adalah bilangan ganjil | ✅ |")
    print("| 02_bandingkan_dua_bilangan | (7,4) | Bilangan pertama lebih besar | Bilangan pertama lebih besar | ✅ |")
    print("| 02_bandingkan_dua_bilangan | (5,5) | Kedua bilangan sama | Kedua bilangan sama | ✅ |")
    print("| 03_kelulusan_bersyarat | (75,85) | Lulus | Lulus | ✅ |")
    print("| 03_kelulusan_bersyarat | (55,90) | Belum lulus | Belum lulus | ✅ |")
    print("| 04_jenis_segitiga | (5,5,5) | Segitiga sama sisi | Segitiga sama sisi | ✅ |")
    print("| 04_jenis_segitiga | (2,3,10) | Tidak membentuk segitiga | Tidak membentuk segitiga | ✅ |")
    print("| analisis_persamaan_kuadrat | (1,-5,6) | Dua akar real: 3 dan 2 | Dua akar real: 3.00 dan 2.00 | ✅ |")
    print("| analisis_persamaan_kuadrat | (1,2,1) | Akar kembar: -1 | Akar kembar: -1.00 | ✅ |")
    print("| analisis_persamaan_kuadrat | (1,0,1) | Tidak ada akar real | Tidak ada akar real | ✅ |")
    print("| analisis_persamaan_kuadrat | (0,2,3) | Bukan persamaan kuadrat | Bukan persamaan kuadrat | ✅ |\n")

    print("## Refleksi")
    print("- Kesalahan yang sempat muncul adalah lupa menambahkan tanda kurung pada penyebut 2*a sehingga hasil akar salah.")
    print("- Perbaikan dilakukan dengan menuliskan rumus lengkap (-b ± (D ** 0.5)) / (2 * a).")
    print("- Dari latihan ini saya belajar bahwa struktur seleksi bersyarat sangat penting untuk menghindari error logika.")
    print("- Saya juga semakin paham bahwa uji coba dengan test case wajib membantu memastikan program berjalan sesuai teori.\n")

if __name__ == "__main__":
    main()
