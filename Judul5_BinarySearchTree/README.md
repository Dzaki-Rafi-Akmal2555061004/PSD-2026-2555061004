# Leaderboard Game Menggunakan BST (Binary Search Tree)

Program ini merupakan aplikasi leaderboard game sederhana berbasis terminal yang menggunakan struktur data Binary Search Tree (BST) untuk menyimpan dan mengelola skor pemain. Melalui menu interaktif, pengguna dapat menambahkan skor pemain baru, menampilkan leaderboard secara terurut dari skor tertinggi ke terendah, menghapus skor tertentu berdasarkan nilainya, serta mencari skor tertinggi secara efisien. Program juga dilengkapi dengan validasi input agar hanya menerima angka, sehingga lebih aman dari kesalahan pengguna.
 
Dari sisi algoritma dan struktur data, program ini menerapkan Binary Search Tree (BST) sebagai struktur utama penyimpanan data skor. Setiap node pada BST menyimpan skor dan nama pemain, di mana skor yang lebih kecil ditempatkan di subtree kiri dan skor yang lebih besar di subtree kanan. Traversal in-order secara menurun digunakan untuk menghasilkan urutan skor dari tertinggi ke terendah. Operasi penghapusan node menggunakan teknik penggantian dengan nilai maksimum dari subtree kiri (in-order predecessor). Kombinasi ini memungkinkan pengelolaan data skor yang efisien dan terstruktur.

---

##  Source Code

<img width="683" height="689" alt="Screenshot 2026-05-23 010153" src="https://github.com/user-attachments/assets/a65cac48-a066-4746-9035-6071de3b65a6" />

<img width="647" height="859" alt="Screenshot 2026-05-23 010214" src="https://github.com/user-attachments/assets/8720182a-3984-45fa-a6dd-86c64a06871a" />

<img width="644" height="282" alt="Screenshot 2026-05-23 010229" src="https://github.com/user-attachments/assets/ed65ad3b-bbb4-4990-a04f-3068d1d31299" />

<img width="753" height="953" alt="Screenshot 2026-05-23 010247" src="https://github.com/user-attachments/assets/b9bcb449-6431-4c06-9015-a4a72dc58f18" />

<img width="765" height="47" alt="Screenshot 2026-05-23 010259" src="https://github.com/user-attachments/assets/3a43c944-b85a-41ff-bc69-4407e6b4a624" />

Baris 1 Mendefinisikan class bernama `Node` sebagai blueprint untuk setiap elemen/simpul di BST.
Baris 2 Fungsi untuk mengisi data node saat object dibuat.
Baris 3 Menyimpan skor pemain.
Baris 4 Menyimpan nama pemain.
Baris 5 Pointer ke subtree kiri BST.
Baris 6 Pointer ke subtree kanan BST.
Baris 8 Membuat Class utama BST untuk leaderboard game.
Baris 9 Fungsi BST.
Baris 10 Root awal BST kosong.
Baris 12 Function rekursif untuk menambah data ke BST.
Baris 13 Jika root kosong.
Baris 14 Akan mengembalikan node.
Baris 15 Jika posisi kosong.
Baris 16 Masukkan ke subtree kiri.
Baris 17 Jika skor lebih besar dari root.
Baris 18 Masukkan ke subtree kanan.
Baris 19 Jika skor sama.
Baris 20 Menampilkan pesan skor sudah ada.
Baris 21 Mengembalikan node root.
Baris 23 Function utama insert yang dipanggil user.
Baris 24 Memulai insert dari root BST.
Baris 26 Function mencari nilai terbesar.
Baris 27 Selama masih ada child kanan.
Baris 28 Berpindah ke kanan.
Baris 29 Mengembalikan node terbesar.
Baris 31 Function menampilkan leaderboard.
Baris 32 List untuk menyimpan hasil traversal.
Baris 33 Traversal descending dari BST.
Baris 34 Jika leaderboard kosong.
Baris 35 Menampilkan pesan kosong.
Baris 36 Jika ada data.
Baris 37 Menampilkan judul leaderboard.
Baris 38 Inisialisasi ranking.
Baris 39 Loop seluruh data pemain.
Baris 40 Menampilkan ranking pemain.
Baris 41 Menambah ranking.
Baris 43 Membuat Fungsi Descending
Baris 44 Jika node kosong.
Baris 45 Menghentikan rekursi.
Baris 46 Kunjungi subtree kanan dulu.
Baris 47 Simpan data pemain dan skor.
Baris 48 Kunjungi subtree kiri.
Baris 50 Function rekursif menghapus node.
Baris 51 Jika node kosong.
Baris 52 Kembalikan node.
Baris 53 Jika skor lebih kecil.
Baris 54 Hapus di subtree kiri.
Baris 55 Jika skor lebih besar.
Baris 56 Hapus di subtree kanan.
Baris 57 Jika node ditemukan.
Baris 58 Jika tidak punya anak kiri.
Baris 59 Ganti dengan anak kanan.
Baris 60 Jika tidak punya anak kanan.
Baris 61 Ganti dengan anak kiri.
Baris 62 Cari predecessor terbesar di kiri.
Baris 63 Ganti skor node.
Baris 64 Ganti nama pemain.
Baris 65 Hapus node predecessor lama.
Baris 66 Kembalikan root.
Baris 68 Function utama delete.
Baris 69 Memulai delete dari root.
Baris 71 Function mencari skor tertinggi.
Baris 72 Jika root kosong.
Baris 73 Menampilkan pesan kosong.
Baris 74 Menghentikan function.
Baris 75 Mulai dari root.
Baris 76 Selama ada child kanan.
Baris 77 Berpindah ke kanan.
Baris 78 Menampilkan judul.
Baris 79 Menampilkan pemain dengan skor tertinggi.
Baris 81-120 Membuat program utamanya untuk menampilkan dari ke-5 menu dan jika tidak dari 5 tersebut maka tidak valid.
Baris 122-123 Menjalankan program utama

## Output Program

<img width="289" height="205" alt="Screenshot 2026-05-23 010322" src="https://github.com/user-attachments/assets/fb520038-0645-439d-a028-dbbf9f3aa5ac" />

Outputan di atas menunjukkan tampilan menu utama program saat pertama dijalankan

<img width="292" height="95" alt="Screenshot 2026-05-23 010409" src="https://github.com/user-attachments/assets/90f8b297-595c-4811-b1d8-b670526dc4ed" />

Outputan di atas menunjukkan hasil ketika pengguna memilih menu 1 maka sistem meminta inputan dari user untuk mengisi nama pemain dan nilai skor.

<img width="281" height="205" alt="Screenshot 2026-05-23 010546" src="https://github.com/user-attachments/assets/68c94135-ef10-4575-bad5-2680ec7045b6" />

Outputan di atas menunjukkan hasil ketika pengguna memilih menu 2. Program melakukan traversal reverse inorder pada BST sehingga menghasilkan daftar pemain yang diurutkan dari skor tertinggi ke terendah secara otomatis.

<img width="314" height="160" alt="Screenshot 2026-05-23 010614" src="https://github.com/user-attachments/assets/9acab556-fdd0-498d-9c9e-7f6509adc348" />

Outputan di atas menunjukkan proses penghapusan data ketika pengguna memilih menu 3. Pengguna memasukkan nilai skor yang ingin dihapus.

<img width="347" height="121" alt="Screenshot 2026-05-23 010639" src="https://github.com/user-attachments/assets/40df0f38-b539-4a77-bd37-173bbd0385a8" />

Outputan di atas menunjukkan hasil ketika pengguna memilih menu 4. Program menelusuri node paling kanan pada BST untuk menemukan skor tertinggi, lalu menampilkan nama pemain beserta nilai skornya.

<img width="284" height="243" alt="Screenshot 2026-05-23 010708" src="https://github.com/user-attachments/assets/71cd8f61-dbf5-4e4b-bc99-93aa2d99e387" />

Outputan di atas menunjukkan kondisi ketika pengguna memilih menu 5. Program mencetak pesan Program selesai, sehingga loop berhenti dan program berakhir secara normal.

<img width="314" height="56" alt="Screenshot 2026-05-23 010656" src="https://github.com/user-attachments/assets/9eb8b8f5-070d-445f-b4b6-5826f04d5b08" />

Outputan di atas menjalankan kondisi ketika pengguna memasukkan pilihan selain angka 1 sampai 5.

## Link Youtube

https://youtu.be/ue0Dm9f4oJE?si=RzhEO4HOdlS9o1yQ
