# PROGRAM KALKULATORKU
# BY ALIF DIO AF'ALLY

# ----- FUNGSI UNTUK KALKULATOR ----- #

# Fungsi Penjumlahan 
def penjumlahan(bil1, bil2):
    jumlah = bil1 + bil2
    print(jumlah)

# Fungsi Pengurangan
def pengurangan(bil1, bil2):
    kurang = bil1 - bil2
    print(kurang)

# Fungsi Perkalian
def perkalian(bil1, bil2):
    kali = bil1 * bil2
    print(kali)

# Fungsi Pembagian
def pembagian(bil1, bil2):
    bagi = bil1 / bil2
    print(bagi)

# ----- MAIN PROGRAM KALKULATOR ----- #

# Greetings!
print("+----------------------------------------------+")
print("Selamat Datang Di KalkulatorKu! :D")
print("+----------------------------------------------+")

# Fungsi Perulangan 
jawab = "ya"
hitung = 0

while(jawab == "ya"):
    hitung +=1

    # Input Bilangan 1, 2, dan pilihan operasi yang ingin dilakukan
    bil1 = int(input("Masukan angka pertama : "))
    bil2 = int(input("Masukan angka kedua : "))
    operasi = int(input("operasi yg ingin dilakukan : "))

    print("+----------------------------------------------+")

    if operasi == 1 :               # Pilih 1 Untuk Melakukan Penjumlahan 
        penjumlahan(bil1, bil2)
    if operasi == 2 :               # Pilih 2 Untuk Melakukan Penjumlahan 
        pengurangan(bil1, bil2)
    if operasi == 3 :               # Pilih 3 Untuk Melakukan Penjumlahan 
        perkalian(bil1, bil2)
    if operasi == 4 :               # Pilih 4 Untuk Melakukan Penjumlahan 
        pembagian(bil1, bil2)
    
    print("+----------------------------------------------+")
    
    # Fitur Untuk Melakukan Penghitungan Kembali
    jawab = input("Ingin Menghitung Lagi? : ")  

    # Note :
    # Format Input : "ya" untuk lanjut menghitung, "tidak" untuk mengakhiri program

    print("+----------------------------------------------+")

    # Kondisi apabila jawaban "tidak"
    if jawab == "tidak" :
        print("Terima kasih Sudah Menggunakan Aplikasi Ini!")
        print()

