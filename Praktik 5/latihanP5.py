a = ' Input Tidak Valid'
b = ' Uang Tidak Cukup'
c = ' Bisa Menonton Dengan Tempat Duduk Biasa'
d = ' Bisa Menonton Dengan Tempat VIP'
w = int(input("Masukan Uang Kamu : "))

print('\n')

if w >= 2200000 :
    print(d)  
elif 1700000 <= w < 2200000 :
    print(c)
elif 1200000 <= w < 1700000 :
    print(b)
elif w < 1200000 :
    print(a)