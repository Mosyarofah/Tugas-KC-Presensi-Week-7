# Tugas-KC-Presensi-Week-7

# kelompok-1-pemrograman-web

**OUTPUT:**
==================================================
   PROGRAM KLASIFIKASI PRESENSI
      DECISION TREE (IF-ELSE)
==================================================
1. Tampilkan Semua Data Mahasiswa
2. Tampilkan Ringkasan Status
3. Keluar

Pilih menu (1/2/3): 

**PENJELASAN:**
Program menampilkan menu utama dengan 3 pilihan: lihat semua data, lihat ringkasan, atau keluar. Saat pengguna memilih menu 1, ditampilkan 5 mahasiswa (Vanesa, Ninda, Gloria, Sinta, Musya). Status ditentukan dari kehadiran: jika Tinggi maka Aktif, jika Rendah maka Tidak Aktif. Keterangan disesuaikan dari tugas dan fitur tambahan (Keaktifan). Saat pengguna memilih menu 2, ditampilkan ringkasan: total 5 mahasiswa, 3 aktif, 2 tidak aktif, dan 2 disiplin. Saat pengguna memilih menu 3, program selesai. Program ini menggunakan logika IF-ELSE tanpa library machine learning.




**OUTPUT:**
Pilih menu (1/2/3): 1

================================================================================
                   DATA MAHASISWA
================================================================================

--- Mahasiswa ke-1 ---
Nama       : Vanesa
Kehadiran  : Tinggi
Tugas      : Lengkap
Keaktifan  : Aktif (Fitur Tambahan)
Status     : Aktif
Keterangan : Mahasiswa Disiplin + Keaktifan baik

--- Mahasiswa ke-2 ---
Nama       : Ninda
Kehadiran  : Rendah
Tugas      : Tidak Lengkap
Keaktifan  : Kurang (Fitur Tambahan)
Status     : Tidak Aktif
Keterangan : Perbaiki kehadiran dan tugas

--- Mahasiswa ke-3 ---
Nama       : Gloria
Kehadiran  : Tinggi
Tugas      : Tidak Lengkap
Keaktifan  : Cukup (Fitur Tambahan)
Status     : Aktif
Keterangan : Perbaiki tugas

--- Mahasiswa ke-4 ---
Nama       : Sinta
Kehadiran  : Rendah
Tugas      : Lengkap
Keaktifan  : Kurang (Fitur Tambahan)
Status     : Tidak Aktif
Keterangan : Tingkatkan kehadiran

--- Mahasiswa ke-5 ---
Nama       : Musya
Kehadiran  : Tinggi
Tugas      : Lengkap
Keaktifan  : Aktif (Fitur Tambahan)
Status     : Aktif
Keterangan : Mahasiswa Disiplin + Keaktifan baik

================================================================================

Tekan Enter untuk kembali...


**PENJELASAN:**
Saat pengguna memilih menu 1, program menampilkan semua data mahasiswa yang berjumlah 5 orang yaitu Vanesa, Ninda, Gloria, Sinta, dan Musya. Status mahasiswa ditentukan dari kehadiran: jika kehadiran Tinggi maka status Aktif, jika kehadiran Rendah maka status Tidak Aktif. Keterangan diperoleh dari kombinasi kehadiran dan tugas, misalnya kehadiran Tinggi dan tugas Lengkap mendapat keterangan "Mahasiswa Disiplin", sementara fitur tambahan berupa Keaktifan (Aktif, Cukup, Kurang) juga mempengaruhi keterangan seperti pada Vanesa dan Musya yang mendapat tambahan "Keaktifan baik". Hasilnya, Vanesa dan Musya berstatus Aktif dengan keterangan Mahasiswa Disiplin + Keaktifan baik, Gloria berstatus Aktif dengan keterangan Perbaiki tugas, Ninda berstatus Tidak Aktif dengan keterangan Perbaiki kehadiran dan tugas, serta Sinta berstatus Tidak Aktif dengan keterangan Tingkatkan kehadiran. Setelah itu program menunggu pengguna menekan Enter untuk kembali ke menu utama.



**OUTPUT:**
Pilih menu (1/2/3): 2

================================================================================
                   RINGKASAN STATUS
================================================================================
Total Mahasiswa   : 5
Mahasiswa Aktif   : 3
Mahasiswa Tidak Aktif : 2
Mahasiswa Disiplin    : 2
================================================================================


**PENJELASAN:**
Saat pengguna memilih menu 2, program menampilkan ringkasan status dari seluruh data mahasiswa. Total mahasiswa sebanyak 5 orang. Dari jumlah tersebut, mahasiswa yang berstatus Aktif ada 3 orang yaitu Vanesa, Gloria, dan Musya, sedangkan yang berstatus Tidak Aktif ada 2 orang yaitu Ninda dan Sinta. Mahasiswa yang termasuk kategori Disiplin (kehadiran Tinggi dan tugas Lengkap) ada 2 orang yaitu Vanesa dan Musya. Setelah itu program kembali ke menu utama.



**OUTPUT:**
Pilih menu (1/2/3): 3

Terima kasih! Program selesai.


**PENJELASAN:**
Saat pengguna memilih menu 3, program menampilkan pesan "Terima kasih! Program selesai." lalu program berhenti. Ini adalah menu keluar yang mengakhiri seluruh program.
