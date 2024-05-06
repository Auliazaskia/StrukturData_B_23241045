# perbadingan 
# lebih besar >
# lebih kecil <
# lebih besar sama dengan >=
# lebih kecil sama dengan <=
# sama dengan ==
# tidak sama dengan !=
# sama "is"
# tidak sama "is not"

x = 2
y = 4

# lebih besar >
hasil = x > y
print (x, '>', y, 'adalah', hasil)

# lebih kecil <
hasil = x < y
print (x, '<', y, 'adalah', hasil)

# lebih besar sama dengan >=
hasil = x >= 2
print (x, '>=', 2, 'adalah', hasil)
hasil = x >= 4
print (x, '>=', 4, 'adalah', hasil)

# lebih kecil sama dengan <=
hasil = x <= 2
print (x, '<=', 2, 'adalah', hasil)
hasil = x <= 4
print (x, '<=', 4, 'adalah', hasil)

# sama dengan ==
hasil = x == 7
print (x, '==', 7, 'adalah', hasil)

# tidak sama dengan !=
hasil = x != 7
print (x, '!=', 7, 'adalah', hasil)

# sama "is"
hasil = x is 7
print (x, 'is', 7, 'adalah', hasil)

# tidak sama "is not"
hasil = x is not 7
print (x, 'is not', 7, 'adalah', hasil)

# > < >= <= == != ini adalah perbandingan Literal
# x = 4, 4 = literal (tidak memakan memory)
# x = object (memory)
# 
# x = 4 (bisa)
# x is 4 (tidak bisa, karena yang dibandingkan adl literal)
# x is y (bisa, karena yang dibandingkan adalah object)

hasil = x is 4
print (x, 'is', y, 'adalah', hasil)

hasil = x is not 4
print (x, 'is not', 4, 'adalah', hasil)
 