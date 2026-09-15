# 04_jenis_segitiga.py
# Program menentukan jenis segitiga berdasarkan panjang sisi

a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

# Periksa syarat terbentuknya segitiga
if a + b > c and a + c > b and b + c > a:
    # Nested if untuk menentukan jenis segitiga
    if a == b and b == c:
        print("Segitiga sama sisi")
    else:
        if a == b or a == c or b == c:
            print("Segitiga sama kaki")
        else:
            print("Segitiga sembarang")
else:
    print("Ketiga sisi tidak membentuk segitiga")
