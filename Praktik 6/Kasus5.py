# Kasus 5 - Bilangan Prima ( 25 point )

print('\n')

n = int(input('Masukan angka : '))

if n < 2:
    print('\n' , "Bukan angka prima")
else:
    for i in range(2,n):
        if n % i == 0 :
            print('\n' , "Bukan angka Prima" , '\n')
            break
    else:
        print('\n' , "Bilangan Prima")

print('\n')