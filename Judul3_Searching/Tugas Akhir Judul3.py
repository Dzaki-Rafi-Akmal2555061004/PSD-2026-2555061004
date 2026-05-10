def interpolation_search(harga_produk, n, target):
    low = 0
    high = n - 1

    while (
        low <= high and
        target >= harga_produk[low] and
        target <= harga_produk[high]
    ):

        if harga_produk[high] == harga_produk[low]:
            if harga_produk[low] == target:
                return low
            break

        pos = low + int(
            ((target - harga_produk[low]) /
            (harga_produk[high] - harga_produk[low]))
            * (high - low)
        )

        print(f"Estimasi posisi produk: {pos}")
        print(f"Harga pada posisi tersebut: Rp{harga_produk[pos]}")

        if target > harga_produk[pos]:
            print("Mencari ke harga yang lebih tinggi...\n")
            low = pos + 1

        elif target < harga_produk[pos]:
            print("Mencari ke harga yang lebih rendah...\n")
            high = pos - 1
        else:
            return pos

    if low < n and harga_produk[low] == target:
        return low

    return -1


def main():

    # Data harga produk e-commerce (harus urut)
    harga_produk = [
        5000, 10000, 15000, 20000,
        25000, 30000, 35000, 40000,
        45000, 50000, 60000, 75000
    ]

    nama_produk = [
        "Pulpen",
        "Buku Tulis",
        "Tempat Pensil",
        "Mouse Pad",
        "Headset",
        "Keyboard",
        "Mouse Gaming",
        "Flashdisk",
        "Speaker",
        "Power Bank",
        "Keyboard Mechanical",
        "Printer"
    ]

    n = len(harga_produk)

    print("=== Daftar Produk E-Commerce ===")

    for i in range(n):
        print(f"{nama_produk[i]} : Rp{harga_produk[i]}")

    while True:
        try:
            target = int(input("\nMasukkan harga produk yang ingin dicari: Rp"))
            break
        except ValueError:
            print("Input tidak valid, masukkan angka!")

    pos = interpolation_search(harga_produk, n, target)

    if pos != -1:
        print("\nProduk ditemukan!")
        print(f"Nama Produk : {nama_produk[pos]}")
        print(f"Harga       : Rp{harga_produk[pos]}")
        print(f"Indeks      : {pos}")

    else:
        print("\nProduk dengan harga tersebut tidak ditemukan")


if __name__ == "__main__":
    main()