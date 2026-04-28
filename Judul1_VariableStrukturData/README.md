# Pengelolaan Data Nilai Mahasiswa

### Deskripsi Singkat

Program tersebut berfungsi sebagai aplikasi sederhana untuk mengelola data nilai mahasiswa menggunakan sebuah array (list1d) berukuran tetap. Melalui menu interaktif, pengguna dapat melihat alamat memori dari array secara keseluruhan maupun setiap elemennya, serta menginput nilai ke dalam array tersebut. Selain itu, program juga dilengkapi dengan validasi input agar hanya menerima angka, sehingga lebih aman dari kesalahan pengguna. Intinya, program ini membantu memahami bagaimana data disimpan dan diakses di dalam memori.

Dari sisi algoritma dan struktur data, program ini menerapkan struktur data array (list 1d) dengan teknik iterasi (perulangan) menggunakan for dan while. Array digunakan untuk menyimpan sekumpulan data dengan indeks tertentu, sedangkan perulangan digunakan untuk mengakses dan mengisi setiap elemen secara berurutan. Selain itu, terdapat percabangan (if-elif) sebagai kontrol alur program berdasarkan pilihan pengguna. Kombinasi ini merupakan dasar dari pengolahan data secara terstruktur dalam pemrograman.


### Source Code

<img width="684" height="552" alt="Screenshot 2026-04-28 075612" src="https://github.com/user-attachments/assets/d0ce80bc-299b-466b-9802-545a7c2f561e" />

<img width="880" height="484" alt="Screenshot 2026-04-28 075632" src="https://github.com/user-attachments/assets/3cc17d5a-38c2-47ee-a5d9-c1e1033ebdd1" />

<img width="406" height="231" alt="Screenshot 2026-04-28 075652" src="https://github.com/user-attachments/assets/0b5987c3-1b50-4a48-929e-a19bc4e1ee03" />


```python
def menu():
    print("1. Tampilkan address data nilai mahasiswa")
    print("2. Tampilkan address dari setiap nilai mahasiswa")
    print("3. Masukkan nilai mahasiswa")
    print("4. Cek Nilai Permahasiswa")
    print("5. Keluar")

```
membuat fungsi menu dan menampilkan menu ke user.

```python
def main():
    a = [0] * 20 
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
```
def main digunakan untuk membuat program utamanya,a = [0] * 20  digunakan untuk membuat list berisi 20 elemen yang dimulai dari 0, running = True digunakan untuk penanda agar program akan terus berjalan, kemudian while running: itu selama running true makan program akan terus mengulang sampai di false kan, menu() sendiri untuk memanggil fungsi menu yang sudah dibuat diawal, try: choice = int(input("Pilihan: ")) digunakan untuk memasukkan pilihan yang ada di menu, dan jika memilih yang tidak ada dimenu akan tertulis "Masukkan angka yang valid", kemudian continue untuk mengulang ke tampilan menu jika error.

```python
        if choice == 1:
            print(f"Address data nilai mahasiswa: {id(a)}")
        elif choice == 2:
            for i in range(20):
                print(f"Address nilai mahasiswa ke-{i}: {id(a[i])}")
        elif choice == 3:
            print("Masukkan 20 nilai mahasiswa:")
            for i in range(20):
                while True:
                    try:
                        a[i] = int(input(f"Nilai mahasiswa ke-{i} = "))
                        break
                    except ValueError:
                        print("Input tidak valid, silakan masukkan angka!")
            print(f"Data nilai mahasiswa sekarang: {a}")
        elif choice == 4: 
            try:
                Nilai_Mahasiswa = int(input("Ingin mengecek Nilai Mahasiswa ke berapa? "))
                
                if 0 <= Nilai_Mahasiswa < len(a):
                    print(f"Nilai pada Mahasiswa tersebut adalah: {a[Nilai_Mahasiswa]}")
                else:
                    print("Peringatan: Nomor Mahasiswa di luar jangkauan!")
            except ValueError:
                print("Masukkan angka yang valid!")
                
        elif choice == 5:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")
```
- if choice == 1: print(f"Address data nilai mahasiswa: {id(a)}") jika memilih pilihan pertama dan akan menampilkan alamat memori dari list. 
- elif choice == 2: for i in range(20): jika memilih pilihan kedua dan akan mengloop dari index 0 sampai 19, print(f"Address nilai mahasiswa ke-{i}: {id(a[i])}") menampilkan alamat memori tiap elemen. 
- elif choice == 3: print("Masukkan 5 nilai mahasiswa:") jika memilih pilihan 3 dan meminta inputan dari user, for i in range(20): digunakan untuk mengloop untuk mengisi 20 data, while True: mengloop validasi inputannya, try: a[i] = int(input(f"Nilai mahasiswa ke-{i} = ")) break digunakan untuk menginput data yang akan disimpan ke array dan break akan memberhentikan loop jika selesai,
except ValueError: print("Input tidak valid, silakan masukkan angka!") jika error atau inputan tidak sesuai maka akan mengulang, print(f"Data nilai mahasiswa sekarang: {a}") menampilkan isi array terbaru.
- elif choice == 4: try: Nilai_Mahasiswa = int(input("Ingin mengecek Nilai Mahasiswa ke berapa? ")) jika memilih pilihan ke 4 dan meminta inputan dari user, except ValueError: print("Masukkan angka yang valid!") digunakan kalau input tidak sesuai akan menghasilkan peringatan kesalahan, if 0 <= Nilai_Mahasiswa < len(a): mengecek apakah index valid atau tidak, print(f"Nilai pada Mahasiswa tersebut adalah: {a[Nilai_Mahasiswa]}") untuk menampilkan index yang dipilih, else: print("Peringatan: Nomor Mahasiswa di luar jangkauan!") jika inputan tidak sesuai akan memunculkan peringatan.
- elif choice == 5: running = False print("Program selesai.") jika memilih pilihan 5 maka loopingan akan selesai dan memunculkan tulisan program selesai.
- else: print("Pilihan tidak valid!") jika pilihan bukan dari 1 sampai 5.

```python
if __name__ == "__main__":
    main()
```
yang terakhir logika diatas untuk mengecek apakah file dijalankan langsung atau bisa disebut untuk menjalankan program.

## Output Program


<img width="441" height="106" alt="Screenshot 2026-04-28 142613" src="https://github.com/user-attachments/assets/f78ff794-fc5c-4edc-9aa9-498589231e00" />

output diatas ketika menampilkan menu utama

<img width="442" height="154" alt="Screenshot 2026-04-28 142711" src="https://github.com/user-attachments/assets/1ae218c9-58ee-4e61-8943-712b1156637b" />

output diatas ketika memilih pilihan 1

<img width="445" height="572" alt="Screenshot 2026-04-28 142754" src="https://github.com/user-attachments/assets/67fe6f37-5dbe-46ce-9c52-987756e51784" />

output diatas ketika memilih pilihan ke 2

<img width="264" height="162" alt="Screenshot 2026-04-28 142840" src="https://github.com/user-attachments/assets/3f4dcdf4-303f-4d04-ba71-fc654f9c0176" />

output diatas ketika memilih pilihan 3 dan menginput nilai mahasiswa

<img width="994" height="659" alt="Screenshot 2026-04-28 142925" src="https://github.com/user-attachments/assets/5b70e91d-44dc-4b18-83d9-5017bfe80b94" />

ketika sudah selesai menginput akan menampilkan nilai hasil inputan

<img width="450" height="176" alt="Screenshot 2026-04-28 143117" src="https://github.com/user-attachments/assets/d7e6305b-0306-4f33-902e-ee4f451c0237" />

ketika memilih pilihan 4 akan meminta inputan berupa mahasiswa ke berapa dan menampilkan nilai mahasiswa yang dipilih

<img width="450" height="155" alt="Screenshot 2026-04-28 143201" src="https://github.com/user-attachments/assets/09acba25-6911-4f1b-8a7b-055193533f65" />

outputan diatas menjelaskan ketika memilih selain dari pilihan 1 sampai 5

<img width="155" height="46" alt="Screenshot 2026-04-28 143255" src="https://github.com/user-attachments/assets/036f99fc-9787-4c5f-832d-586c78e382a7" />

outputan diatas ketika memilih pilihan 5 dan akan memberhentikan loop

## Link Youtube

https://youtu.be/zDMIfziTzqs?si=6SakK79MKP6bstly
