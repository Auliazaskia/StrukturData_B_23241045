# input dari user
# aritmatika

# Belajar Inputan
aulia = input ("masukkan kata:")
print("isi dari aulia :", aulia, "bertipe data :",type(aulia))

# belajar aritmatika dasar
x = 3
y = 4

# penjumlahan +
hasil = x + y
print ("x + y =", hasil)

# pengurangan -
hasil = x - y
print ("x - y =", hasil)

# perkalian *
hasil = x * y
print ("x * y =", hasil)

# pembagian /
hasil = x / y
print ("x / y =", hasil)

# XOR ^
hasil = x ^ y
print ("x ^ y =", hasil)

# modulus %
hasil = x % y
print ("x mod y =", hasil)

# floor division (pembulatan kebawah) //
hasil = x // y
print ("x // y =", hasil)

# aritmatika prioritas
# (), exponen, perkalian/pembaagian, penjumlahan/pengangguran
x = 3
y = 4
z = 5

hasil = ( x ** y * z + x / y - z % x // y)
print (hasil)