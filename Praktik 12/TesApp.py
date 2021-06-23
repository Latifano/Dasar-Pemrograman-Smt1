from MyLib import *

print('\n')


def main():
    N = int(input('Masukan Batas Array : '))
    x = [float]*N
    for i in range(N):
        x[i] = float(input())

    print('\n')

    HitunganSum(x)
    RataRata(x, N)
    Median(x, N)
    Min(x)
    Max(x)


main()
