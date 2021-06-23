# PRAKTIKUM 3

# Kasus 1 - Cek Error (20 Point)

print('\n')

a = 1
b = 4

print("Hasil a yang pertama : "+str(a))
print("Hasil b yang pertama : "+str(b))

b = a # b adalah 1(a pertama)
a -= b # artinya a = 1(a pertama) - b = 1(a pertama)

print("Hasil a yang kedua : "+str(a))
print("Hasil b yang kedua : "+str(b))

a = b + 1 # a = 1(b kedua) + 1
b = a // b # b = 2(a ketiga) di floor division 1(b kedua) 

print("Hasil a yang ketiga : "+str(a))
print("Hasil b yang ketiga : "+str(b))

print('\n')
print("-----------------------------------------" , '\n')

# Kasus 2 - Aritmatika #1 (25 Point)

x = 0
y = 1
a = 2
b = 5
hasil_k2 = a * x + y * b

print("Hasil dari a * x + y * b = " , hasil_k2)

print('\n')
print("-----------------------------------------" , '\n')

# Kasus 3 - Aritmatika #2 (25 Point)

z = 0.5
a = 1.0
t = 3.0
hasil_k3 = z * a * t

print("Hasil dari z * a * t = " , hasil_k3)

print("\n")
print("-----------------------------------------" , '\n')

# Kasus 4 - Kebut - kebutan! (30 Point)

vt = 21.55
v0 = 0
t = 12.5

a = (vt - v0) / t

print("Hasil dari a = (vt - v0) / t" , " = " , a)

print("\n")
