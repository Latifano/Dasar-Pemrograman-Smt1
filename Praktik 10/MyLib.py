import Globals


def panjangString(s):
    panjang = len(s)
    print('Panjang String (', s, ') =', panjang)


def cariKarakter(c1, data):
    while Globals.x:
        if c1 in data:
            print("ada")
        elif c1 not in data:
            print("tidak ada")
        break


def frekuensiKarakter(c2, data):
    karakter = data.count(c2)
    print('Frekuensi karakter (', c2, ') pada (', data, ') = ', karakter)


def cekPalindrom(p):
    return p == p[-1:-(len(p)+1):-1]
