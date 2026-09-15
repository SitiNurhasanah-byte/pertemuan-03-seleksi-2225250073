# 01_genap_ganjil.py
# Program untuk menentukan apakah bilangan bulat genap atau ganjil

bilangan = int(input("Masukkan bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")
