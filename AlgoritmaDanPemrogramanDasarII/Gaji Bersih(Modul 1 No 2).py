def hitung_gaji():
    print("Program Hitung Gaji Bersih")
    while True:
        try:
            gaji = int(input("Masukkan Gaji: "))
            if gaji <= 0:
                print("Error: Masukkan angka yang valid (harus integer positif)!")
            else:
                break
        except ValueError:
            print("Error: Masukkan angka yang valid (harus integer positif)!")

    pajak = gaji * 5 / 100
    bersih = gaji - pajak
    print(f"Gaji Bersih dari gaji yang dimasukkan adalah: {bersih:.0f}")

hitung_gaji()
