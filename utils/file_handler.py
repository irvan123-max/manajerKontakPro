# Di dalam file: utils/file_handler.py
import json
# TAMBAHKAN IMPORT INI di Baris 4:
from kontak.kontak_class import Kontak
NAMA_FILE = "kontak_hari20.json" # Kita ganti nama file jadi baru
# Ini adalah fungsi yang Anda salin dari hari15.py
def muat_kontak_dari_file():
    """Memuat daftar kontak dari file JSON. Mengembalikan list kosong jika file tidak ada."""
    try:
        with open(NAMA_FILE, "r") as file:
            data_json =json.load(file)
            # Penting: Ubah data dictionary kembali menjadi objek 'kontak'
            daftar_kontak_objek = []
            for data_kontak in data_json:
                # Fungsi ini perlu tau 'kontak'
                kontak = Kontak(data_kontak['nama'], data_kontak['telepon'])
                daftar_kontak_objek.append(kontak)
            return daftar_kontak_objek
    except (FileNotFoundError, json.JSONDecodeError):
        return [] # Kembalikan list kosong jika file rusak/kosong
# Ini adalah fungsi kedua yang Anda salin dari hari15.py
def simpan_kontak_ke_file(daftar_kontak):
    """Menyimpan daftar objek kontak ke file JSON."""
    data_json = []
    for kontak in daftar_kontak:
        data_json.append({'nama': kontak.nama, 'telepon': kontak.telepon})
        with open(NAMA_FILE, "w") as file:
            json.dump(data_json, file,indent=4)