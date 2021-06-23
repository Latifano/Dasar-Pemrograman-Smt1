'''
PRAKTIKUM 7
Kasus 1 - Copy Cat #1 ( 10 Point )
'''
print('\n')

n = int(input("Masukan angka : "))

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")

print('\n')
