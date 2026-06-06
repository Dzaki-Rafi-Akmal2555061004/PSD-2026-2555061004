# Sistem Manajemen Loker Sekolah Berbasis Hash Map Open Adressing

Program ini merupakan simulasi sistem manajemen loker sekolah yang memanfaatkan struktur data Hash Map untuk menyimpan dan mengelola data kepemilikan loker oleh siswa. Setiap loker diidentifikasi dengan nomor unik dan dikaitkan dengan nama satu siswa. Program mendukung tiga operasi utama: menambahkan data loker, mencari data berdasarkan nomor loker, serta menghapus data loker menggunakan pendekatan Lazy Deletion.

Algoritma yang diterapkan adalah Linear Probing, yaitu teknik penanganan tabrakan (collision) pada Hash Table. Ketika dua nomor loker menghasilkan nilai hash yang sama, program akan mencari slot berikutnya secara linear hingga menemukan slot yang kosong atau dihapus. Pendekatan ini menjaga efisiensi penyimpanan sekaligus mempertahankan urutan pencarian agar data tetap dapat ditemukan dengan benar meski terjadi collision.

---

## Source Code

<img width="312" height="344" alt="Screenshot 2026-06-06 140029" src="https://github.com/user-attachments/assets/454e1f77-79d0-4477-b35e-448b90ee6d37" />

<img width="334" height="367" alt="Screenshot 2026-06-06 140055" src="https://github.com/user-attachments/assets/d01b5ae5-904c-4407-9d56-44ac5b616918" />

<img width="326" height="208" alt="Screenshot 2026-06-06 140106" src="https://github.com/user-attachments/assets/3582acdd-c7dd-4f36-af34-9474af4e79cc" />

Baris 1 Mendefinisikan kelas yang berfungsi sebagai enumerasi konstanta untuk merepresentasikan status tiap slot pada hash table.

Baris 2 Konstanta bernilai 0, menandakan slot belum pernah diisi sama sekali.

Baris 3 Konstanta bernilai 1, menandakan slot sedang terisi data aktif.

Baris 4 Konstanta bernilai 2, menandakan slot pernah berisi data namun sudah dihapus secara logis.

Baris 6 Mendefinisikan kelas yang merepresentasikan satu slot/entri di dalam hash map.

Baris 7 Constructor yang dipanggil otomatis setiap kali objek Entry baru dibuat.

Baris 8 Atribut untuk menyimpan nomor loker, diinisialisasi None karena slot masih kosong.

Baris 9 Atribut untuk menyimpan nama pemilik loker, diinisialisasi None.

Baris 11 Status awal slot diset EMPTY (0), menandakan slot ini belum pernah digunakan.

Baris 12 Kelas utama yang mengimplementasikan seluruh logika sistem manajemen loker berbasis hash table.

Baris 13 Constructor dengan parameter size default 10, menentukan kapasitas hash table.

Baris 14 Menyimpan ukuran tabel ke atribut instance agar bisa diakses oleh semua method.

Baris 15 Membuat list berisi SIZE objek Entry menggunakan list comprehension, Semua slot awalnya berstatus EMPTY.

Baris 17 Mendefinisikan fungsi hash yang menghitung indeks target dari sebuah nomor loker.

Baris 18 Mengembalikan hasil modulo nomor loker dengan ukuran tabel.

Baris 20 Mendefinisikan method untuk menambahkan data loker baru ke dalam hash table.

Baris 21 Menghitung indeks awal menggunakan fungsi hash.

Baris 22 Melakukan iterasi maksimal sebanyak SIZE langkah menelusuri seluruh tabel jika perlu untuk mencari slot yang tersedia.

Baris 23 Menghitung indeks aktual dengan menambahkan offset step ke indeks awal, lalu modulo untuk memastikan pencarian melingkar agar tidak keluar batas array.

Baris 24 Mengecek apakah slot saat ini tidak sedang terisi. Slot EMPTY maupun DELETED sama-sama bisa dipakai untuk menyimpan data baru.

Baris 25 Menyimpan nomor loker ke slot yang ditemukan.

Baris 26 Menyimpan nama siswa ke slot yang sama.

Baris 27 Mengubah status slot menjadi OCCUPIED untuk menandai bahwa slot kini terisi data aktif.

Baris 28 Mengembalikan True sebagai tanda bahwa penambahan data berhasil.

Baris 29 Baris ini hanya tercapai jika seluruh iterasi selesai tanpa menemukan slot kosong, artinya tabel penuh mengembalikan False sebagai tanda gagal.

Baris 31 Mendefinisikan method untuk mencari entri berdasarkan nomor loker.

Baris 32 Menghitung indeks awal pencarian menggunakan fungsi hash yang sama.

Baris 33 Iterasi maksimal SIZE langkah untuk menelusuri tabel secara linear.

Baris 34 Menghitung indeks aktual dengan wrap-around, sama seperti pada tambah_loker.

Baris 35 Jika slot berstatus EMPTY, pencarian dihentikan dan langsung return None. Logikanya: jika slot ini kosong dan belum pernah terisi, maka data yang dicari tidak mungkin ada di slot berikutnya.

Baris 36 Mengembalikan None menandakan data tidak ditemukan.

Baris 37 dan 38 Mengecek dua kondisi sekaligus: slot harus OCCUPIED dan nomor loker harus cocok. Slot DELETED dilewati begitu saja sehingga pencarian tetap berlanjut — inilah inti dari lazy deletion.

Baris 39 Mengembalikan objek Entry yang ditemukan jika kedua kondisi terpenuhi.

Baris 40 Jika seluruh iterasi selesai tanpa menemukan data yang cocok, kembalikan None.

Baris 42 Mendefinisikan method untuk menghapus data loker secara logis.

Baris 43 Mencari entri yang ingin dihapus menggunakan method cari_loker. Hasilnya disimpan di variabel data.

Baris 44 Mengecek apakah data ditemukan (bukan None).

Baris 45 Mengubah status slot menjadi DELETED. Data nomor loker dan nama siswa masih ada di memori, tapi slot ini tidak akan dianggap aktif. Ini adalah teknik Lazy Deletion, slot tidak dikembalikan ke EMPTY agar rantai linear probing tidak putus.

Baris 46 Mengembalikan True sebagai tanda penghapusan berhasil.

Baris 47 Jika data tidak ditemukan, kembalikan False.

Baris 49 Mendefinisikan method untuk menampilkan seluruh isi hash table ke layar.

Baris 50 Mencetak header/judul tampilan dengan baris kosong di atasnya.

Baris 51 Iterasi dari slot 0 hingga slot terakhir untuk menampilkan setiap slot.

Baris 52 Mencetak label slot beserta nomornya. Parameter end="" mencegah baris baru agar kelanjutan teks berada di baris yang sama.

Baris 53 Mengecek apakah slot berstatus kosong.

Baris 54 Mencetak teks "Kosong" untuk slot yang belum pernah terisi.

Baris 55 Mengecek apakah slot berstatus telah dihapus.

Baris 56 Mencetak teks "Sudah Dihapus" untuk slot yang datanya telah dihapus secara lazy deletion.

Baris 57 Kondisi terakhir, artinya slot berstatus OCCUPIED.

Baris 58, 59, 60 Mencetak detail loker berupa nomor dan nama pemiliknya.

Baris 63 Fungsi utama sebagai entry point program untuk mendemonstrasikan semua operasi.

Baris 64 Membuat objek sistem loker dengan ukuran default 10 slot.

Baris 65 Menambahkan loker 1 milik Andi.

Baris 66 Menambahkan loker 11 milik Budi.

Baris 67 Menambahkan loker 21 milik Citra.

Baris 68 Menambahkan loker 2 milik Dewi.

Baris 69 Menampilkan seluruh isi tabel setelah keempat data dimasukkan.

Baris 71 Mencari loker nomor 11, hasilnya disimpan di variabel hasil.

Baris 72 Mengecek apakah pencarian berhasil menemukan data.

Baris 73 Mencetak nama pemilik loker 11 jika ditemukan.

Baris 74 Menghapus loker 11 secara lazy deletion (status slot diubah menjadi DELETED).

Baris 75 Mencetak keterangan sebelum menampilkan tabel hasil penghapusan.

Baris 76 Menampilkan kembali seluruh isi tabel untuk membuktikan slot 2 kini berstatus "Sudah Dihapus".

Baris 78 Kondisi standar Python untuk memastikan main() hanya dijalankan ketika file ini dieksekusi langsung, bukan saat diimpor sebagai modul.

Baris 79 Memanggil fungsi main() untuk menjalankan program.


## Output Program

<img width="114" height="128" alt="Screenshot 2026-06-06 140126" src="https://github.com/user-attachments/assets/e39dc358-f7f3-49ea-9269-75e719e402f5" />

Tampilan pertama memperlihatkan hasil penempatan data setelah empat operasi tambah_loker. Loker 1 (Andi) menempati Slot 1 sesuai hasil hash 1 % 10 = 1. Loker 11 (Budi) juga menghasilkan hash yang sama yaitu slot 1, namun karena slot 1 sudah terisi, linear probing menggesernya ke Slot 2. Demikian pula Loker 21 (Citra) dengan hash slot 1, digeser ke Slot 3 karena slot 1 dan 2 sudah terisi. Loker 2 (Dewi) mendapat hash 2 % 10 = 2, namun slot 2 sudah terisi Budi sehingga digeser ke Slot 4. Slot 0 dan slot 5–9 tetap kosong karena tidak ada data yang ditempatkan di sana.

<img width="131" height="18" alt="Screenshot 2026-06-06 140229" src="https://github.com/user-attachments/assets/bfe77862-a5e0-475d-a10a-7614285eff58" />

Hasil pencarian menunjukkan bahwa cari_loker(11) berhasil menemukan Budi di Slot 2 meski hash awalnya menunjuk ke Slot 1, membuktikan bahwa linear probing berjalan dengan benar dalam penelusuran.

<img width="137" height="143" alt="Screenshot 2026-06-06 140240" src="https://github.com/user-attachments/assets/5372df64-c1c6-4def-9df6-e1559975df21" />

Tampilan kedua setelah penghapusan loker 11 menunjukkan bahwa Slot 2 kini berstatus "Sudah Dihapus" (bukan "Kosong"). Ini membuktikan mekanisme Lazy Deletion bekerja dengan benar — Slot 3 (Citra) masih bisa ditemukan karena rantai pencarian melewati slot DELETED tanpa berhenti, berbeda jika slot tersebut berstatus EMPTY.

## Link Youtube

https://youtu.be/diAVbAUrIWg?si=hft5-_HpX89Xv0Zo
