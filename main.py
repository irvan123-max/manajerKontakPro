# DI dalam file: main.py
# --- 1.IMPORT BARU KITA ---
# Ini memberi tahu main.py cara menemukan kode di foldrt lain
from kontak.kontak_class import Kontak
from utils.file_handler import muat_kontak_dari_file, simpan_kontak_ke_file
# --- 2. KODE YANG ANDA SALIN DARI HARI 15 ---
def main():
    daftar_kontak = muat_kontak_dari_file()
    print(f"Berhasil memuat {len(daftar_kontak)} kontak dari file.")
    while True:
        print("\n--- Manajer Kontak (Pro) ---")
        print("1. Tampilkan Semua Kontak")
        print("2. Tambah Kontak Baru")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1-3): ")
        if pilihan == "1":
            print("\n--- Daftar Kontak Anda ---")
            if not daftar_kontak:
                print("Daftar kontak masih kosong.")
            else:
                for kontak in daftar_kontak:
                    kontak.tampilkan()
        elif pilihan == "2":
            print("\n--- Tambahkan Kontak Baru ---")
            nama = input("Masukkan nama: ")
            telepon = input("Masukkan nomor telepon: ")
            kontak_baru = Kontak(nama, telepon) # Menggunakan class ' kontak'
            daftar_kontak.append(kontak_baru)
            print(f"Kontak untuk '{nama}' berhasil ditambahkan.")
        elif pilihan == "3":
            print("\nMenyimpan kontak ke file...")
            simpan_kontak_ke_file(daftar_kontak) # Menggunakan fungsi 'simpan'
            print("Terima kasih! Program ditutup.")
            break
        else:
            print("Pilihan tidak valid.Coba lagi.")
# --- 3. KODE YANG JUGA DISALIN DARI HARI 15 ---
if __name__ == "__main__":
    main()
print("\n--- Hari 20 Selesai ---")