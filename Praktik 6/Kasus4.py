# Kasus 4 - Rata - rata ( 20 point )

print('\n')

sum = 0
i = 0
a = int(input("Masukan Jumlah Nilai: "))
while i < a:
    n = int(input("Masukkan nilai - {} : ".format(i + 1)))
    i += 1
    sum += n
rata_rata = sum // i
print(str(rata_rata))

print('\n')