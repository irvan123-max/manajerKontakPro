# Di dalam file: Kontak/Kontak_class.py
class Kontak:
    def __init__(self, nama, telepon):
        self.nama = nama
        self.telepon = telepon
    def tampilkan(self):
        print(f"  - Nama: {self.nama}, Telepon: {self.telepon}")