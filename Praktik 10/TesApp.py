import MyLib
print('\n')


def main():
    # input
    data = "balonku ada lima , rupa-rupa warnanya"
    c1 = input('Masukan karakter yang dicari : ')
    c2 = input('Masukan karakter yang dihitung frekuensi : ')
    p = input('Masukan string pengecekan palindrom/tidak palindrom : ')

    print('\n')

    MyLib.panjangString(data)
    MyLib.cariKarakter(c1, data)
    MyLib.frekuensiKarakter(c2, data)
    cek = MyLib.cekPalindrom(p)
    if cek:
        print("Palindrom")
    else:
        print("Bukan Palindrom")


if __name__ == '__main__':
    main()

print('\n')
