print("program pyhton menghitung luas ruangan ")
print("hitunglah sebuah ruangan ini!")
#keterangan:
#P merupakan panjang ruangan
#L merupakan lebar ruangan

p = float(input("masukkan panjang ruangan = "))
l = float(input("Masukkan lebar ruangan = "))
r = input("Pilih satuan(meter/inci) = ")

if (r == 'meter') :
    a = p * l
elif (r == 'inci') :
    a = p * l * 39.37
else : print("Maaf, hanya bisa meter atau inci")

print ("panjang ruangan = ", p)
print ("lebar ruangan = ", l)
print ("luas ruangan = ",a,r)