def menu():
    print("1. Tampilkan address data nilai mahasiswa")
    print("2. Tampilkan address dari setiap nilai mahasiswa")
    print("3. Masukkan nilai mahasiswa")
    print("4. Cek Nilai Permahasiswa")
    print("5. Keluar")


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


if __name__ == "__main__":
    main()