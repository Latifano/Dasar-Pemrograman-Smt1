'''
Praktikum 8
kasus "Refresh"
'''

print('\n')
art = int(input("Masukan angka pertama untuk aritmatika : "))
art2 = int(input("Masukan angka kedua untuk aritmatika : "))
persegi = float(input("Masukan sisi persegi : "))
a, t = map(float, input("Masukan sisi segitiga : ").split())
print('\n')


def aritmatika(art, art2):
    global tambah, kurang, kali, bagi
    tambah = art + art2
    kurang = art - art2
    kali = art * art2
    bagi = art / art2


def sisi_persegi(persegi):
    global luas_P
    luas_P = persegi * persegi


def sisi_segitiga(a, t):
    global luas_S
    luas_S = 1/2 * a * t


aritmatika(art, art2)
sisi_persegi(persegi)
sisi_segitiga(a, t)
print("Hasil Penjumlahan : ", tambah)
print("Hasil Penjumlahan : ", kurang)
print("Hasil Penjumlahan : ", kali)
print("Hasil Penjumlahan : ", bagi)
print("Luas Persegi : ", int(luas_P))
print("Luas segitiga : ", int(luas_S))

print('\n')
