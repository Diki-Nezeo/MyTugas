def hitung_rata_rata():
    angka_list = []
    print("Program Hitung Rata-Rata")
    while True:
        angka = input("Masukkan angka (atau ketik 'n' untuk mengakhiri): ").strip()
        if angka.lower() == 'n':
            break
        try:
            angka_float = float(angka)
            angka_list.append(angka_float)
        except ValueError:
            print("Masukkan angka yang valid!")

    if not angka_list:
        print("Tidak ada angka yang dimasukkan.")
        return

    rata_rata = sum(angka_list) / len(angka_list)
    print(f"Rata-rata dari angka yang dimasukkan adalah: {rata_rata:.2f}")

hitung_rata_rata()
