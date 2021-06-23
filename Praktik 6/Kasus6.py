# Kasus 6 - Uang Anak Kost Part II ( 25 Point )

print('\n')

saldo = int(input("Saldo awal : "))
while (True):
    buy = int(input("Pengeluaran Soni hari ini (-1 untuk keluar): "))
    if buy == -1 :
        print('\n',"Sisa saldo : ", saldo)
        break
    saldo -= buy
    if saldo < 0:
        print('\n',"Saldo tidak cukup")
        print('\n',"Sisa saldo : ", saldo + buy)
        break

print('\n')