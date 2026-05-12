# PROGRAM DECISION TREE SEDERHANA - PRESENSI MAHASISWA
# NAMA : MOSYAROFAH
# Mata Kuliah: Kecerdasan Komputasional
# Konsep: IF-ELSE (tanpa library machine learning)

# ============ DATA MAHASISWA ============
# Fitur tambahan: "Keaktifan" (nilai: Aktif / Cukup / Kurang)
# Data baru: mahasiswa bernama "MUSYA"

data_mahasiswa = [
    {"nama": "Vanesa", "kehadiran": "Tinggi", "tugas": "Lengkap", "keaktifan": "Aktif"},
    {"nama": "Ninda", "kehadiran": "Rendah", "tugas": "Tidak Lengkap", "keaktifan": "Kurang"},
    {"nama": "Gloria", "kehadiran": "Tinggi", "tugas": "Tidak Lengkap", "keaktifan": "Cukup"},
    {"nama": "Sinta", "kehadiran": "Rendah", "tugas": "Lengkap", "keaktifan": "Kurang"},
    {"nama": "Musya", "kehadiran": "Tinggi", "tugas": "Lengkap", "keaktifan": "Aktif"}  # data baru
]

# FUNGSI DECISION TREE (IF-ELSE) 
def tentukan_status(kehadiran, tugas, keaktifan):
    if kehadiran == "Tinggi":
        status = "Aktif"
    else:
        status = "Tidak Aktif"
    
    if kehadiran == "Tinggi" and tugas == "Lengkap":
        keterangan = "Mahasiswa Disiplin"
    elif kehadiran == "Tinggi" and tugas == "Tidak Lengkap":
        keterangan = "Perbaiki tugas"
    elif kehadiran == "Rendah" and tugas == "Lengkap":
        keterangan = "Tingkatkan kehadiran"
    else:
        keterangan = "Perbaiki kehadiran dan tugas"
    
    if keaktifan == "Aktif" and status == "Aktif":
        keterangan += " + Keaktifan baik"
    elif keaktifan == "Kurang" and status == "Aktif":
        keterangan += " + Keaktifan perlu ditingkatkan"
    
    return status, keterangan

# TAMPILKAN SEMUA DATA 
def tampilkan_semua_data():
    print("\n" + "="*80)
    print("                   DATA MAHASISWA")
    print("="*80)
    
    for i, mhs in enumerate(data_mahasiswa, start=1):
        status, keterangan = tentukan_status(
            mhs["kehadiran"], 
            mhs["tugas"], 
            mhs["keaktifan"]
        )
        
        print(f"\n--- Mahasiswa ke-{i} ---")
        print(f"Nama       : {mhs['nama']}")
        print(f"Kehadiran  : {mhs['kehadiran']}")
        print(f"Tugas      : {mhs['tugas']}")
        print(f"Keaktifan  : {mhs['keaktifan']} (Fitur Tambahan)")
        print(f"Status     : {status}")
        print(f"Keterangan : {keterangan}")
    
    print("\n" + "="*80)

# TAMPILKAN RINGKASAN 
def tampilkan_ringkasan():
    print("\n" + "="*80)
    print("                   RINGKASAN STATUS")
    print("="*80)
    
    aktif = 0
    tidak_aktif = 0
    disiplin = 0
    
    for mhs in data_mahasiswa:
        status, _ = tentukan_status(mhs["kehadiran"], mhs["tugas"], mhs["keaktifan"])
        if status == "Aktif":
            aktif += 1
        else:
            tidak_aktif += 1
        
        if mhs["kehadiran"] == "Tinggi" and mhs["tugas"] == "Lengkap":
            disiplin += 1
    
    print(f"Total Mahasiswa   : {len(data_mahasiswa)}")
    print(f"Mahasiswa Aktif   : {aktif}")
    print(f"Mahasiswa Tidak Aktif : {tidak_aktif}")
    print(f"Mahasiswa Disiplin    : {disiplin}")
    print("="*80)

# PROGRAM UTAMA 
def main():
    while True:
        print("\n" + "="*50)
        print("   PROGRAM KLASIFIKASI PRESENSI")
        print("      DECISION TREE (IF-ELSE)")
        print("="*50)
        print("1. Tampilkan Semua Data Mahasiswa")
        print("2. Tampilkan Ringkasan Status")
        print("3. Keluar")
        
        pilihan = input("\nPilih menu (1/2/3): ")
        
        if pilihan == "1":
            tampilkan_semua_data()
            input("\nTekan Enter untuk kembali...")
        elif pilihan == "2":
            tampilkan_ringkasan()
            input("\nTekan Enter untuk kembali...")
        elif pilihan == "3":
            print("\nTerima kasih! Program selesai.\n")
            break
        else:
            print("\nPilihan tidak valid! Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

# Jalankan program
if __name__ == "__main__":
    main()