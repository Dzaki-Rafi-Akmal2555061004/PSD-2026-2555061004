class Node:
    def __init__(self, score, player):
        self.score = score
        self.player = player
        self.left = None
        self.right = None

class BSTLeaderboard:
    def __init__(self):
        self.root = None

    def _insert(self, root, score, player):
        if root is None:
            return Node(score, player)
        if score < root.score:
            root.left = self._insert(root.left, score, player)
        elif score > root.score:
            root.right = self._insert(root.right, score, player)
        else:
            print(f"[!] Skor {score} sudah ada.")
        return root

    def insert(self, score, player):
        self.root = self._insert(self.root, score, player)

    def _find_max(self, root):
        while root.right:
            root = root.right
        return root

    def tampilkan_leaderboard(self):
        result = []
        self._descending(self.root, result)
        if not result:
            print("\nLeaderboard kosong.")
        else:
            print("\n===== LEADERBOARD GAME =====")
            rank = 1
            for player, score in result:
                print(f"{rank}. {player} - {score} poin")
                rank += 1

    def _descending(self, root, result):
        if root is None:
            return
        self._descending(root.right, result)
        result.append((root.player, root.score))
        self._descending(root.left, result)

    def _delete(self, root, score):
        if root is None:
            return root
        if score < root.score:
            root.left = self._delete(root.left, score)
        elif score > root.score:
            root.right = self._delete(root.right, score)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._find_max(root.left)
            root.score = temp.score
            root.player = temp.player
            root.left = self._delete(root.left, temp.score)
        return root

    def delete(self, score):
        self.root = self._delete(self.root, score)

    def cari_skor_tertinggi(self):
        if self.root is None:
            print("Leaderboard kosong.")
            return
        current = self.root
        while current.right:
            current = current.right
        print(f"\nSkor tertinggi:")
        print(f"{current.player} - {current.score} poin")

def main():
    bst = BSTLeaderboard()
    pilih = 0 
    while pilih != 5:
        print("\n==============================")
        print("      LEADERBOARD GAME")
        print("==============================")
        print("1. Tambah skor pemain")
        print("2. Tampilkan leaderboard")
        print("3. Hapus skor pemain")
        print("4. Tampilkan skor tertinggi")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("[!] Input harus angka.")
            continue
        if pilih == 1:
            try:
                nama = input("Nama pemain: ")
                skor = int(input("Skor pemain: "))
                bst.insert(skor, nama)
                print("[OK] Data berhasil ditambahkan.")
            except ValueError:
                print("[!] Skor harus angka.")
        elif pilih == 2:
            bst.tampilkan_leaderboard()
        elif pilih == 3:
            try:
                skor = int(input("Masukkan skor yang ingin dihapus: "))
                bst.delete(skor)
                print("[OK] Data berhasil dihapus.")
            except ValueError:
                print("[!] Input harus angka.")
        elif pilih == 4:
            bst.cari_skor_tertinggi()
        elif pilih == 5:
            print("\nProgram selesai.")
        else:
            print("[!] Pilihan tidak valid.")

if __name__ == "__main__":
    main()