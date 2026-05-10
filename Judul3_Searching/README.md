# Sistem E-Commerce menggunakan Interpolation Binary Search

Program tersebut merupakan simulasi pencarian produk pada sistem e-commerce berdasarkan harga produk. Program menampilkan daftar nama produk beserta harganya, kemudian pengguna dapat memasukkan harga tertentu yang ingin dicari. Setelah itu, sistem akan mencari data dan menampilkan produk yang sesuai apabila ditemukan. Program ini bertujuan untuk mempermudah proses pencarian data secara cepat dan efisien pada kumpulan data yang sudah terurut.

Algoritma yang diterapkan pada program adalah Interpolation Binary Search dengan struktur data berupa array/list. Interpolation Binary Search bekerja dengan memperkirakan posisi data berdasarkan nilai target yang dicari sehingga proses pencarian dapat lebih cepat dibanding pencarian biasa pada data numerik yang terurut dan memiliki distribusi merata. Algoritma ini sering digunakan dalam sistem pencarian data seperti harga produk, ID barang, stok gudang, maupun database pada aplikasi e-commerce seperti Tokopedia dan Shopee.


## Source Code

<img width="359" height="331" alt="Screenshot 2026-05-10 175048" src="https://github.com/user-attachments/assets/1a2212c4-7701-41b5-a00a-2bac015fe3f0" />

<img width="321" height="117" alt="Screenshot 2026-05-10 175109" src="https://github.com/user-attachments/assets/6e8c4bea-82a4-4746-a97f-03a1eaa83269" />

<img width="308" height="335" alt="Screenshot 2026-05-10 180346" src="https://github.com/user-attachments/assets/23357812-6ff2-4570-b3b1-10751af0e8e4" />

<img width="419" height="254" alt="Screenshot 2026-05-10 180400" src="https://github.com/user-attachments/assets/6572890b-2cc1-4a7b-9d49-0ea4f9e83e46" />

Baris 1 digunakan untuk membuat fungsi interpolation binary Search
baris 2 digunakan untuk membuat variabel low sebagai indeks awal array
baris 3 digunakan untuk membuat variabel high sebagai indeks akhir array
baris 5 digunakan untuk membuat perulangan
baris 6, 7, 8 digunakan untuk perulangannya jikalau low belum melewati high, dan target masih berada dalam rentang nilai array
baris 11 digunakan untuk mengecek apakah nilai paling awal dan akhir sama
baris 12 digunakan jika nilai tersebut sama dengan target
baris 13 digunakan untuk mengembalikan indeks
baris 14 menghentikan perulangan
baris 16 sampai 20 digunakan sebagai rumus pencarian interpolation binary Search
baris 22 menampilkan estimasi posisi dari produk
baris 23 menampilkan Harga pada posisi tersebut
baris 25 digunakan untuk mengecek apakah target lebih besar dari nilai pada posisi sekarang
baris 26 Menampilkan informasi bahwa pencarian dilanjutkan ke kanan
baris 27 Menggeser batas bawah ke kanan
baris 29 digunakan untuk mengecek apakah target lebih kecil dari nilai pada posisi sekarang
baris 30 menampilkan informasi bahwa pencarian dilanjutkan ke kiri
baris 31 Menggeser batas bawah ke kiri
baris 32 jika target sama dengan data pada posisi tersebut
baris 33 maka indeks dikembalikan
baris 35 digunakan untuk pengecekan terakhir apakah target ditemukan
baris 36 digunakan untuk mengembalikan indeks target
baris 38 Jika target tidak ditemukan, fungsi mengembalikan -1
baris 41 digunakan untuk membuat fungsi utama
baris 42 sampai 46 membuat list harga produk 
baris 48 sampai 61 digunakan untuk membuat list nama produk
baris 63 digunakan untuk menghitung jumlah data produk
baris 65 menampilkan judul program
baris 67 perulangan untuk menampilkan seluruh produk
baris 68 menampilkan nama dan harga produk
baris 70 digunakan untuk perulangan input agar pengguna tidak salah memasukkan data
baris 71 mencoba menjalankan input angka
baris 72 kmeminta pengguna memasukkan harga produk yang dicari 73 keluar dari perulangan jika input benar
baris 74 menangani error jika input bukan angka
baris 75 menampilkan pesan kesalahan input
baris 77 memanggil fungsi pencarian Interpolation Search yang sudah dibuat diawal
baris 79 mengecek apakah produk ditemukan
baris 80 menampilkan pesan bahwa produk ditemukan
baris 81 menampilkan nama produk
baris 82 menampilkan harga produk
baris 83 menampilkan posisi indeks produk
baris 85 jika produk tidak ditemukan
baris 86 menampilkan pesan bahwa data tidak ditemukan
baris 87 dan 88 untuk untuk menjalankan fungsi main() jika file dieksekusi langsung

## Output Program

<img width="208" height="170" alt="Screenshot 2026-05-10 185410" src="https://github.com/user-attachments/assets/f489e3d5-1583-49c1-9f00-688f03c42867" />

<img width="224" height="178" alt="Screenshot 2026-05-10 185445" src="https://github.com/user-attachments/assets/eb047807-5c9d-4d20-aa67-1e1230e19ec0" />

Output diatas ketika program baru dijalankan dan sistem langsung meminta harga dari produk yang dicari user


Output diatas ketika user telah menginput harga produk dan sistem langsung mencari produk yang dicari oleh user

## Link Youtube

https://youtu.be/uCy2MNCF1iI?si=LGo0NhfmRzsqYVHI<img width="359" height="331" alt="Screenshot 2026-05-10 175048" src="https://github.com/user-attachments/assets/c73f1c72-b0c5-402b-b024-678a8fa0a677" />
