# Pengurutan lagu (A-Z)

### Deskripsi Singkat

Program tersebut digunakan untuk mengelola dan mengurutkan playlist lagu yang diinput oleh pengguna agar tersusun rapi berdasarkan urutan alfabet (A–Z). Pengguna memasukkan sejumlah judul lagu, kemudian program menyimpannya dalam sebuah list (array). Setelah itu, program memproses data tersebut dan menampilkan hasil sebelum dan sesudah diurutkan, sehingga memudahkan pengguna dalam melihat perubahan urutan playlist.

Algoritma yang diterapkan adalah Insertion Sort, yaitu metode pengurutan dengan cara mengambil satu elemen data, lalu menyisipkannya ke posisi yang tepat pada bagian data yang sudah terurut sebelumnya. Struktur data yang digunakan adalah array, di mana setiap elemen berupa string.

## Source Code

<img width="483" height="195" alt="Screenshot 2026-05-03 224322" src="https://github.com/user-attachments/assets/27da30d4-c14e-4444-be0f-25f2c11f49f7" />

baris 1 untuk membuat fungsi dari insertion sort
baris 2 untuk membuat perulangan yang dimulai dari indeks ke 1, karna indeks 0 sudah dianggap terurut
baris 3 untuk menyimpan sementara array i
baris 4 untuk menentukan posisi sebelum dibandingkan
baris 5 Selama masih dalam batas array dan lagu sebelumnya lebih besar (secara alfabet), maka lanjutkan pergeseran.
baris 6 untuk menggeser elemen ke kanan
baris 7 untuk mundur ke indeks sebelumnya untuk perbandingan lagi 
baris 8 untuk menempatkan temp ke posisi yang benar

<img width="522" height="146" alt="Screenshot 2026-05-03 224548" src="https://github.com/user-attachments/assets/49655d03-20d9-4c53-bc45-5f3b2a8b0136" />

baris 11 untuk membuat fungsi utama pemrograman
baris 12 dan 13 untuk meminta input jumlah lagu dari user 
baris 14, 15, dan 16 jika inputan bukan angka, dan akan mengulang.

<img width="612" height="609" alt="Screenshot 2026-05-03 224625" src="https://github.com/user-attachments/assets/f2940983-d99a-45d8-9d10-66683ac6abb1" />

baris 18 untuk membuat list kosong untuk menyimpan lagu
baris 19 untuk menampilkan instruksi input
baris 20 untuk perulangan meminta lagu sebanyak n 
baris 21 loop validasi agar input tidak kosong
baris 22 dan 23 untuk meminta judul lagu
baris 24 dan 25 jika kosong dianggap tidak valid
baris 26 untuk menambahkan lagu ke dalam list 
baris 27 untuk Keluar dari loop jika input valid
baris 28 dan 29 untuk Menampilkan pesan jika input tidak valid
baris 31 untuk menampilkan playlist sebelum Sorting 
baris 33 untuk Memanggil fungsi Insertion Sort untuk mengurutkan
baris 35 untuk Menampilkan judul output setelah sorting
baris 36 dan 37 untuk Menampilkan semua lagu yang sudah terurut
baris 38 untuk pindah baris agar output rapi
baris 41 dan 42 untuk Menjalankan fungsi main() jika file dieksekusi langsung


## Output Program

<img width="231" height="29" alt="Screenshot 2026-05-03 224828" src="https://github.com/user-attachments/assets/84ad48d4-5f3f-41c2-83c2-d0b3158f8adc" />

Output diatas ketika program baru dijalankan

<img width="218" height="160" alt="Screenshot 2026-05-03 224944" src="https://github.com/user-attachments/assets/a7c012c4-6ff6-4bfd-98e3-c7514bdf0586" />

Output diatas ketika meminta judul lagu sebanyak 5 karna pengguna meminta 5 lagu 

<img width="730" height="53" alt="Screenshot 2026-05-03 224955" src="https://github.com/user-attachments/assets/7a147132-2668-482d-ac77-fa6194fd4800" />

Output diatas ketika semua lagu sudah di input dan sudah di sorting.

## Link Youtube 

https://youtu.be/P8jky8wKqOY?si=zt0QYDpd3BBEVYgc

