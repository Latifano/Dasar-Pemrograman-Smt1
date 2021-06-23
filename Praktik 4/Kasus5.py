# Kasus 5 - Sengketa Lahan ( 25 Point )
print('\n')
print("Program Menghitung Luas Tanah")
print('\n')

x = int(input("Panjang Tanah : ")) 
print('next')
y = int(input("Lebar Tanah : "))
z = input("Setuju / Tidak Setuju : ")
L = x * y
samarata = L / 2
a = 'Setuju'
b = 'Tidak Setuju'

print("-----------------------------------------" , '\n')
print("Luas Tanah Pak Eko : " , L , "m")
print('\n')
print("Luas Tanah Pak Joni: " , int(samarata) , "m")
print('\n')
print("Luas Tanah Pak Soni: " , int(samarata) , "m")
print('\n')
if x != y :
    print(a)
elif x == y :
    print(b)
print('\n')