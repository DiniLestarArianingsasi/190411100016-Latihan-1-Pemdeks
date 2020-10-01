"""
Nama : Dini Lestari Arianingsasi
NIM : 190411100016
Kelas : Pemrogramab Dekstop 3C
"""
#1 Mencari Rata-rata dengan 5 variabel

print("Menghitung Rata-Rata 5 Variabel")
uh1 = 80
print("uh1 =", uh1)
uh2 = 85
print("uh2 =", uh2)
tugas = 90
print("tugas =", tugas)
uts = 87
print("uts =", uts)
uas = 85
print("uas =", uas)
rata = ((uh1)+(uh2)+(tugas)+(uts)+(uas))/5
print("Rata-Rata Nilai Anda Adalah :", rata)

print("")
print("")

#2 Menghitung Luas dan Keliling Bangun Datar

print("Menghitung Luas dan Keliling Persegi Panjang")
panjang = float(input("Masukkan panjang = "))
lebar = float(input("Masukkan Lebar = "))
keliling = 2*(panjang+lebar)
luas = panjang * lebar
print("Keliling persegi panjang adalah", keliling)
print("Luas persegi panjang adalah",  luas)

print("")
print("")

#3 Menghitung Index Massa Tubuh/BMI (Body Mess Index)

print("Menghitung BMI (Body mass index)")
tinggi = float(input("Masukkan Tinggi Badan Anda(m) :"))
berat = float(input("Masukkan Berat Badan Anda(kg) :"))
bmi = berat/(tinggi)**2
print("BMI anda adalah :", bmi)
if bmi<18.5 :
    print("Berat Badan Kurang")
elif bmi >= 18.5 and bmi <= 22.9:
    print("Berat Badan Normal")
elif bmi >23 and bmi <= 29.9:
    print("Berat Badan Berlebihan (Cenderung Obesitas)")
elif bmi >30:
    print("Obesitas")
else:
    print("over Obesitas")

print("")
print("")

#4 Menentukan Nilai Maksimum dan Nilai Minimum

print ("Mencari Nilai Minimum dan Maksimum")
data = int(input("Masukkan jumlah data :"))
angka=[]
for i in range (data):
    nip= int(input("Masukkan angka :"))
    angka.append(nip)
min = angka[0]
max = angka[len(angka)-1]
for j in angka:
    if min > j:
        min=j
    if max < j:
        max=j
angka.sort()
print ("List data", angka)
print ("Nilai Maksimumnya yaitu :", max)
print ("nilai Minimun Yaitu :", min)

print("")
print("")

#5 Validasi Username dan Password

print("Mengecek Username dan Passwod")
username = "Dini"
password = "2001"
for i in range(3):
    user=input("Masukkan username anda :")
    pwd=input("Masukkan password anda :")
    j=3
    if user==username and pwd==password:
        print("Anda berhasil masuk")
        break
    else:
        print("Username/Password anda salah", j-i)
        continue
print("\n Coba Lagi")

