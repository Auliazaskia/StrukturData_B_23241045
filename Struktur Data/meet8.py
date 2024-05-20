# Perbandingan Lanjutan  

# +++++3---------9+++++++++
MasukkanUser = float(input("Masukkan Bilangan kurang dari 3 atau lebih dari 9:"))

#-----Cek kurang dari 3
kurDar = (MasukkanUser < 3)
print ("Kurang dari 3=", kurDar)

#------Cek Lebih dari 9
lebDar = (MasukkanUser > 9)
print ( "Lebih dari 9 =", lebDar)

betul = kurDar or lebDar
print ("Pengecekkan final :", betul)



# --------4++++++++14--------
MasukkanUser = float(input("masukkan bilangan antara 4 dan 14 :"))

# -------Cek lebih dari 4
lebDar = (MasukkanUser > 4 )
print ("lebih dari 4 =", lebDar)

# -------Cek kurang dari 14
kurDar = (MasukkanUser < 14)
print ("kurang dari 14 =", kurDar)

betul = kurDar and lebDar
print ("Pengecekkan final :", betul)



# -----------5+++++++++++9----------12+++++++++30-----------pr