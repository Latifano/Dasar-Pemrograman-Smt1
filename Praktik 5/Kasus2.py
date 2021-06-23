# Kasus 2 - Tukar Tambah (30 Point)

print('\n')

x = int(input("Tahun motor : "))
c = ' Motor harus dibawah tahun 2020'
d = ' Motor Sudah tahun 2020'
e = ' Biaya ditambah Rp'
f = 2020 - x
biaya = f * 2000000

print('\n')

if (f < 0) :
    print(c)
elif (f == 0) :
    print(d) 
elif (f > 0) :
    print(e , biaya)



print('\n' , '---------------------------------------' , '\n')
