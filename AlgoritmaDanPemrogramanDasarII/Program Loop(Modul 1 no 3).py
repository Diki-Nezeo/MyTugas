print("Program Pengulangan Sederhana")

n = 16

def while_loop():
    i = 1
    while i < n:
        print(i)
        i += 1

def do_while_loop(): 
    i = 1 
    while True:
        print(i)
        i += 1
        if i >= n:
            break

def for_loop():
    for i in range(1, n): 
        print(i)

print("Menggunakan while loop:")
while_loop()

print("Menggunakan do-while loop:")
do_while_loop()

print("Menggunakan for loop:")
for_loop()