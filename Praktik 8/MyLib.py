# Input & Fungsi

print('\n')


def main():
    global tambah, kurang, kali, bagi, luas_persegi, luas_segitiga
    angka1 = int(input("Masukan angka pertama : "))
    angka2 = int(input("Masukan angka kedua : "))
    s = float(input("Masukan sisi persegi : "))
    a, t = map(float, input("Masukan a dan t : ").split())

    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    luas_persegi = s * s
    luas_segitiga = 1/2 * a * t


main()
