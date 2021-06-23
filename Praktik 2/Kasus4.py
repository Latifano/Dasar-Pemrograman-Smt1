# Kasus 4-Cek error (30 Point)
#Kamus
a = 1
b = 4

#Algoritma
print("Hasil a yang pertama:" , a)
print("Hasil b yang pertama:", str(b))

b = a + 1 # artinya b = 1(a pertama) + 1 = 2
a -= b # artinya a = 1(a pertama) - 2(b pertama) = -1
print("Hasil a yang kedua:" , a)
print("Hasil b yang kedua:" , b)

a = b + 2 # artinya a = 2(b kedua) + 2 = 4
b = a * b # artinya b = 4(a ketiga) dikali 2(b kedua) = 8
print("Hasil a yang ketiga:" ,format(a))
print("Hasil b yang ketiga: %f" % (b))

c = a
a = b # varivael a = 8 (b ketiga)
b = c # variabel b sama dengan c = 4 (a ketiga) 
print("Hasil a yang keempat: {}" .format(a))
print("Hasil b yang keempat: {}" .format(b))

print("\n")