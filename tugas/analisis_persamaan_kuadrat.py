# analisis_persamaan_kuadrat.py
# Program untuk menganalisis persamaan kuadrat ax^2 + bx + c = 0

print("Analisis Persamaan Kuadrat")

a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    diskriminan = b ** 2 - 4 * a * c
    print(f"Diskriminan = {diskriminan:.2f}")

    if diskriminan > 0:
        x1 = (-b + diskriminan ** 0.5) / (2 * a)
        x2 = (-b - diskriminan ** 0.5) / (2 * a)
        print(f"Dua akar real berbeda: x1 = {x1:.2f}, x2 = {x2:.2f}")
    else:
        if diskriminan == 0:
            x = -b / (2 * a)
            print(f"Akar real kembar: x = {x:.2f}")
        else:
            print("Tidak ada akar real.")
