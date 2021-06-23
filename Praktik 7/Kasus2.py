'''
PRAKTIKUM 7
Kasus 2 - Copy Cat #2 ( 10 Point )
'''
print('\n')

n = int(input("Masukan angka : "))

for i in range(n):
    t = int(input())
    for num in range(t + 1):
        for j in range(num):
            print(num, end=" ")
        print('\n')

print('\n')
