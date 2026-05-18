# Riwayat Browser dari Stack Array

Program tersebut berfungsi untuk mensimulasikan fitur Browser History seperti pada browser nyata, misalnya saat pengguna membuka website, menekan tombol Back, dan Forward. Program dibuat menggunakan bahasa Python dengan dua buah stack, yaitu back stack untuk menyimpan riwayat halaman sebelumnya dan forward stack untuk menyimpan halaman yang dapat dibuka kembali setelah menekan tombol back. Ketika pengguna mengunjungi URL baru, URL tersebut akan dimasukkan ke dalam back stack, sedangkan forward stack akan dikosongkan. Saat tombol back ditekan, halaman saat ini dipindahkan ke forward stack sehingga pengguna dapat kembali menggunakan tombol forward. Program juga menyediakan menu interaktif untuk menampilkan status stack dan halaman aktif yang sedang dibuka.

Algoritma struktur data yang diterapkan pada program ini adalah Stack dengan implementasi menggunakan array. Stack bekerja menggunakan konsep LIFO atau disebut juga Last In First Out, yaitu data yang terakhir masuk akan menjadi data pertama yang keluar. Operasi utama yang digunakan adalah push untuk menambahkan data ke stack, pop untuk mengambil data teratas, dan peek untuk melihat data paling atas tanpa menghapusnya. Struktur data stack sangat cocok digunakan dalam sistem browser history karena proses navigasi halaman web selalu mengakses halaman terakhir yang dibuka terlebih dahulu.

---

## Source Code

Baris 1	Mendefinisikan kelas StackArray yang merepresentasikan struktur data Stack berbasis array.
Baris 2	Mendefinisikan method __init__ dengan parameter max_size=10, yaitu konstruktor kelas yang dijalankan saat objek dibuat.
Baris 3	Menetapkan nilai MAX sebagai kapasitas maksimum stack dari parameter max_size.
Baris 4	Membuat array dengan ukuran MAX yang diisi nilai None sebagai representasi slot kosong.
Baris 5	Menginisialisasi top_idx = -1, menandakan stack kosong karena belum ada elemen yang dimasukkan.
Baris 7-8 mengembalikan True jika top_idx bernilai -1, yang berarti stack tidak memiliki elemen.
Baris 10-11	Method is full mengembalikan True jika top_idx sudah sama dengan MAX-1, menandakan stack sudah penuh.
Baris 13-19 menambahkan elemen ke stack. Jika stack penuh mencetak pesan error, jika tidak top_idx dinaikkan lalu elemen disimpan di posisi top_idx.
Baris 21-26 menghapus elemen teratas. Jika stack kosong mencetak pesan underflow, jika tidak mencetak elemen yang dihapus dan menurunkan top_idx.
Baris 28-32 menampilkan elemen teratas tanpa menghapusnya. Jika stack kosong mencetak pesan kosong.
Baris 34-41 menampilkan semua elemen stack dari atas ke bawah menggunakan perulangan dari top_idx ke 0.
Baris 43-45 mereset top_idx ke -1 sehingga seluruh isi stack dianggap terhapus, lalu mencetak konfirmasi.
Baris 48-50 mendefinisikan objek stack dan variabel pilih=0 untuk menyimpan pilihan menu pengguna.
Baris 51-57	Loop while berjalan selama pilih != 6, menampilkan menu utama dengan 6 pilihan operasi stack.
Baris 58-62	Blok try-except membaca input pilihan menu dari pengguna dan menangani error jika input bukan angka.
Baris 63-76	Blok if-elif menangani setiap pilihan menu: push 1, pop 2, peek 3, display 4, clear 5, keluar 6, dan pilihan tidak valid.
Baris 78-79	Guard __name__ == '__main__' memastikan fungsi main hanya dipanggil saat file dieksekusi langsung, bukan saat diimpor.

## Output Program

Ketika program pertama kali dijalankan, sistem menampilkan menu utama yang berisi 6 pilihan operasi stack.

Ketika pengguna memilih menu 1 Push dan memasukkan sebuah kata, sistem akan mencetak konfirmasi bahwa kata berhasil ditambahkan. Ketika pengguna memilih menu 1 Push dan memasukkan sebuah kata, sistem akan mencetak konfirmasi bahwa kata berhasil ditambahkan.

Ketika pengguna memilih menu 2 Pop/Undo, sistem mencetak kata yang berhasil dihapus dari posisi teratas stack.

Ketika pengguna memilih menu 3 Peek menampilkan kata terakhir tanpa menghapusnya.

ketika pengguna memilih menu 4 Tampilkan akan menampilkan seluruh isi stack dari atas ke bawah.

Ketika pengguna memilih menu 5 Clear All akan mengosongkan seluruh stack.

Ketika pengguna memilih menu 6 mengakhiri program.

## Link Youtube

https://youtu.be/Np6QnWW9sw0?si=Zxr9TR_SUrSkGDEB
