'''
PRAKTIKUM 7
Kasus 3 - Copy Cat #3 ( 5 Point )
'''
print('\n')

n = int(input("Masukan angka : "))

for i in range(n):
    t = int(input('\n'))
    r = 1
    i = 2
    while i <= t:
        r *= i
        i += 1
    print(r)
