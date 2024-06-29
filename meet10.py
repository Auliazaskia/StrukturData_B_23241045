# LATIHAN MEET KE-10

App = input("ketik 1 untuk penjumlahan, ketik 2 untuk pengurangan :")

if App == "1":
    print("Mulai Penjumlahan...")
    x = input("Masukkan bilangan Pertama :")
    y = input("Masukkan bilangan ke-dua :")

    # konversi input ke integral
    x = int(x)
    y = int(y)

    hasil = x + y
    print (x, "+", y, "=", hasil)
elif App == "2":
    print("Muliai pengurangan....")
    x = input("Masukkan bilangan petama :")
    y = input("Masukkan bilangan ke-dua :")

    # konversi input ke integral
    x = int(x)
    y = int(y)

    hasil = x - y
    print (x, "-", y, "=", hasil)
