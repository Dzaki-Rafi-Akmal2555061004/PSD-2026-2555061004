class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2

class Entry:
    def __init__(self):
        self.nomor_loker = None
        self.nama_siswa = None
        self.state = SlotState.EMPTY

class SistemLokerSekolah:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, nomor_loker):
        return nomor_loker % self.SIZE

    def tambah_loker(self, nomor_loker, nama_siswa):
        idx = self.hash_function(nomor_loker)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state != SlotState.OCCUPIED:
                self.table[i].nomor_loker = nomor_loker
                self.table[i].nama_siswa = nama_siswa
                self.table[i].state = SlotState.OCCUPIED
                return True
        return False

    def cari_loker(self, nomor_loker):
        idx = self.hash_function(nomor_loker)
        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE
            if self.table[i].state == SlotState.EMPTY:
                return None
            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].nomor_loker == nomor_loker):
                return self.table[i]
        return None

    def hapus_loker(self, nomor_loker):
        data = self.cari_loker(nomor_loker)
        if data:
            data.state = SlotState.DELETED
            return True
        return False

    def tampilkan(self):
        print("\nDATA LOKER SEKOLAH")
        for i in range(self.SIZE):
            print(f"Slot {i}: ", end="")
            if self.table[i].state == SlotState.EMPTY:
                print("Kosong")
            elif self.table[i].state == SlotState.DELETED:
                print("Sudah Dihapus")
            else:
                print(
                    f"Loker {self.table[i].nomor_loker} "
                    f"- {self.table[i].nama_siswa}"
                )

def main():
    loker = SistemLokerSekolah()
    loker.tambah_loker(1, "Andi")
    loker.tambah_loker(11, "Budi")
    loker.tambah_loker(21, "Citra")
    loker.tambah_loker(2, "Dewi")
    loker.tampilkan()

    hasil = loker.cari_loker(11)
    if hasil:
        print(f"\nLoker 11 dimiliki oleh {hasil.nama_siswa}")
    loker.hapus_loker(11)
    print("\nSetelah loker 11 dikosongkan:")
    loker.tampilkan()

if __name__ == "__main__":
    main()