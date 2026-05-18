# Riwayat Browser dari Stack Array

Program tersebut berfungsi untuk mensimulasikan fitur Browser History seperti pada browser nyata, misalnya saat pengguna membuka website, menekan tombol Back, dan Forward. Program dibuat menggunakan bahasa Python dengan dua buah stack, yaitu back stack untuk menyimpan riwayat halaman sebelumnya dan forward stack untuk menyimpan halaman yang dapat dibuka kembali setelah menekan tombol back. Ketika pengguna mengunjungi URL baru, URL tersebut akan dimasukkan ke dalam back stack, sedangkan forward stack akan dikosongkan. Saat tombol back ditekan, halaman saat ini dipindahkan ke forward stack sehingga pengguna dapat kembali menggunakan tombol forward. Program juga menyediakan menu interaktif untuk menampilkan status stack dan halaman aktif yang sedang dibuka.

Algoritma struktur data yang diterapkan pada program ini adalah Stack dengan implementasi menggunakan array. Stack bekerja menggunakan konsep LIFO atau disebut juga Last In First Out, yaitu data yang terakhir masuk akan menjadi data pertama yang keluar. Operasi utama yang digunakan adalah push untuk menambahkan data ke stack, pop untuk mengambil data teratas, dan peek untuk melihat data paling atas tanpa menghapusnya. Struktur data stack sangat cocok digunakan dalam sistem browser history karena proses navigasi halaman web selalu mengakses halaman terakhir yang dibuka terlebih dahulu.

---

## Source Code

<img width="262" height="488" alt="Screenshot 2026-05-18 171941" src="https://github.com/user-attachments/assets/8738f723-9f80-4ffe-9db7-dfb221e8b558" />


<img width="406" height="428" alt="Screenshot 2026-05-18 172004" src="https://github.com/user-attachments/assets/4e084224-0140-4d5d-a7e8-9bf25e6ee4b3" />


<img width="419" height="475" alt="Screenshot 2026-05-18 172034" src="https://github.com/user-attachments/assets/5bf799f4-d1f6-47aa-b7c9-ad772ab971c5" />


<img width="274" height="180" alt="Screenshot 2026-05-18 172048" src="https://github.com/user-attachments/assets/2fca18b0-4671-47b2-8a99-5a05f7daab06" />

Baris 1	Membuat class bernama StackArray untuk implementasi struktur data stack menggunakan array.
Baris 2	Mendefinisikan method __init__ dengan parameter max_size=100, yaitu konstruktor kelas yang dijalankan saat objek dibuat.
Baris 3	Menyimpan kapasitas maksimum stack.
Baris 4	MMembuat array kosong dengan ukuran sesuai kapasitas stack.
Baris 5	Menandai posisi elemen teratas stack. Nilai -1 berarti stack masih kosong.
Baris 7 Fungsi untuk mengecek apakah stack kosong.
Baris 8 Mengembalikan nilai True jika stack kosong.
Baris 10 Fungsi untuk mengecek apakah stack penuh.
Baris 11 Mengembalikan True jika indeks top sudah mencapai batas maksimum array.
Baris 13 Fungsi untuk menambahkan data ke stack.
Baris 14 Mengecek apakah stack penuh.
Baris 15 Menampilkan pesan jika stack penuh.
Baris 16 Menghentikan proses push dan mengembalikan False.
Baris 17 Menambah posisi top satu langkah.
Baris 18 Memasukkan data x ke posisi top stack.
Baris 19 Mengembalikan True jika push berhasil.
Baris 21 Fungsi untuk mengambil data paling atas stack.
Baris 22 Mengecek apakah stack kosong.
Baris 23 Jika kosong maka mengembalikan None.
Baris 24 Menyimpan nilai data paling atas ke variabel val.
Baris 25 Menghapus isi data pada posisi top.
Baris 26 Menurunkan posisi top satu langkah.
Baris 27 Mengembalikan data yang di-pop.
Baris 29 Fungsi untuk melihat data paling atas tanpa menghapusnya.
Baris 30 Mengecek apakah stack kosong.
Baris 31 Mengembalikan None jika kosong.
Baris 32 Mengembalikan nilai data teratas stack.
Baris 34 Fungsi untuk menghitung jumlah data dalam stack.
Baris 35 Mengembalikan jumlah elemen stack.
Baris 37 Fungsi untuk menampilkan isi stack.
Baris 38 Mengecek apakah stack kosong.
Baris 39 Menampilkan tulisan kosong jika stack tidak memiliki data.
Baris 40 Menghentikan proses display.
Baris 41 Perulangan dari data teratas sampai terbawah.
Baris 42 Memberi tanda pada elemen paling atas stack.
Baris 43 Menampilkan isi stack beserta indeksnya.
Baris 45 Membuat class BrowserHistory untuk simulasi riwayat browser.
baris 46 Sebagai constructor class BrowserHistory.
Baris 47 Membuat stack untuk menyimpan riwayat halaman sebelumnya
Baris 48 Membuat stack untuk menyimpan halaman forward.
Baris 50 Fungsi untuk membuka halaman baru.
Baris 52 Selama forward stack tidak kosong.
Baris 53 Menghapus semua isi forward stack.
Baris 54 Memasukkan URL baru ke back stack.
Baris 55 Menampilkan halaman yang dikunjungi.
Baris 56 Menampilkan proses push ke stack.
Baris 58 Fungsi tombol back.
Baris 60 Mengecek apakah hanya ada satu halaman atau tidak ada halaman sebelumnya.
Baris 61 Menampilkan pesan jika back tidak bisa dilakukan.
Baris 62 Menghentikan proses.
Baris 63 Mengambil halaman saat ini dari back stack.
Baris 64 Memindahkan halaman saat ini ke forward stack.
Baris 65 Melihat halaman sebelumnya.
Baris 66 Menampilkan proses back.
Baris 67 Menampilkan halaman aktif sekarang.
Baris 69 Fungsi tombol forward.
Baris 71 Mengecek apakah ada halaman forward.
Baris 72 Menampilkan pesan jika tidak ada halaman forward.
Baris 73 Menghentikan proses.
Baris 74 Mengambil halaman dari forward stack.
Baris 75 Memasukkan kembali halaman ke back stack.
Baris 76 Menampilkan proses forward.
Baris 77 Menampilkan halaman aktif.
Baris 79 Fungsi untuk melihat halaman aktif.
Baris 81 Mengambil halaman paling atas pada back stack.
Baris 82 Mengembalikan halaman aktif atau pesan kosong.
Baris 84 Fungsi untuk menampilkan status browser.
Baris 86 Menampilkan garis pembatas.
Baris 87 Menampilkan halaman aktif.
Baris 88 Menampilkan judul back stack.
Baris 89 Menampilkan isi back stack.
Baris 90 Menampilkan judul forward stack.
Baris 91 Menampilkan isi forward stack.
Baris 92 Mengecek apakah tombol back bisa digunakan.
Baris 93 Mengecek apakah tombol forward bisa digunakan.
Baris 94 Menampilkan status tombol back.
Baris 95 Menampilkan status tombol forward.
Baris 96 Menampilkan garis penutup.
Baris 98-130 Fungsi main() digunakan untuk menjalankan program browser history dan menampilkan menu interaktif kepada pengguna. Di dalamnya terdapat proses input pilihan menu, menjalankan fitur browser seperti membuka URL, back, forward, melihat status stack, serta menangani kesalahan input agar program tetap berjalan dengan baik sampai pengguna memilih keluar.
Baris 132-133 untuk menjalankan program

## Output Program

<img width="172" height="101" alt="Screenshot 2026-05-18 185309" src="https://github.com/user-attachments/assets/62da5445-0486-4f15-b663-166d6e82b680" />

Ketika program pertama kali dijalankan, sistem menampilkan menu utama yang berisi 5 pilihan operasi stack.

<img width="179" height="392" alt="Screenshot 2026-05-18 185432" src="https://github.com/user-attachments/assets/0054bd36-5464-49ba-8acb-430c94201217" />

Ketika pengguna memilih menu 1 Push dan memasukkan sebuah kata, sistem akan mencetak konfirmasi bahwa kata berhasil ditambahkan.

<img width="175" height="125" alt="Screenshot 2026-05-18 185446" src="https://github.com/user-attachments/assets/12e49c95-73f6-4e04-bd0a-b5e5d7429255" />

Ketika pengguna memilih menu 2 back, sistem kembali ke halaman sebelumnya.

<img width="176" height="146" alt="Screenshot 2026-05-18 185842" src="https://github.com/user-attachments/assets/11ebea73-a750-4872-9925-c514d4715e26" />

Ketika pengguna memilih menu 3 forward maju ke halaman berikutnya.

<img width="185" height="274" alt="Screenshot 2026-05-18 185526" src="https://github.com/user-attachments/assets/ac0e33b7-95b7-461a-ad24-c6c71db69662" />

ketika pengguna memilih menu 4 Tampilkan akan menampilkan seluruh isi stack dari atas ke bawah.

<img width="76" height="24" alt="Screenshot 2026-05-18 185535" src="https://github.com/user-attachments/assets/989de662-6815-49be-9540-9301c55d3fdf" />

Ketika pengguna memilih menu 5 mengakhiri program.

## Link Youtube

https://youtu.be/Np6QnWW9sw0?si=Zxr9TR_SUrSkGDEB
