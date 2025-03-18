class MyInput:
    def baca_string(self):
        return input("Masukkan teks: ")

    def baca_int(self):
        while True:
            try:
                return int(input("Masukkan angka: "))
            except ValueError:
                print("Harus angka! Coba lagi.")

# Contoh penggunaan
mi = MyInput()

teks = mi.baca_string()
print("Teks:", teks)

angka = mi.baca_int()
print("Angka:", angka)

