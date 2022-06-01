class Kendaraan:
    nama = ""
    jenis = "mobil"
    warna = ""
    nilai = 1000.00
    def deskripsi(self):
        penjelasan = "%s jenis %s warna %s harganya Rp.%.2f." % (self.nama, self.jenis, self.warna, self.nilai)
        return penjelasan

# your code goes here
car1 = Kendaraan()
car1.nama = "Kijang"
car1.warna = "putih"
car1.jenis = "innova"
car1.nilai = 600000000.00

car2 = Kendaraan()
car2.nama = "Jazz"
car2.warna = "hitam"
car2.jenis = "honda"
car2.nilai = 150000000.00

# test code
print(car1.deskripsi())
print(car2.deskripsi())