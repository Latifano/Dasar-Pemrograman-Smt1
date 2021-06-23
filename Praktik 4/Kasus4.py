# Kasus 4 - Luas Persegi atau persegi panjang ? ( 25 Point)
print('\n')

a = float(input("Masukan Panjang : "))
print('next')
b = float(input("Masukan Lebar : "))
c = int(a * b)
print('\n' , "Luasnya adalah : " , c , "cm" )
if ( a == b ) :
    print('\n' , "ini Persegi")
elif ( a != b ) :
    print('\n' , "ini Persegi Panjang")

print("-----------------------------------------" , '\n')