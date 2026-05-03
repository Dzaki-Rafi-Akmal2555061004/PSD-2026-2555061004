def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah lagu: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan judul lagu:")
    for i in range(n):
        while True:
            try:
                lagu = input(f"Lagu ke-{i+1}: ")
                if lagu.strip() == "":
                    raise ValueError
                arr.append(lagu)
                break
            except ValueError:
                print("Input tidak boleh kosong!")

    print(f"\nPlaylist sebelum diurutkan: {arr}")

    insertion_sort(arr, n)

    print("Playlist setelah diurutkan (A-Z):", end=" ")
    for i in range(n):
        print(arr[i], end=" | ")
    print()


if __name__ == "__main__":
    main()