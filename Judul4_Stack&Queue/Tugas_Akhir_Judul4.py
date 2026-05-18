class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Stack penuh")
            return False
        self.top_idx += 1
        self.st[self.top_idx] = x
        return True

    def pop(self):
        if self.is_empty():
            return None
        val = self.st[self.top_idx]
        self.st[self.top_idx] = None
        self.top_idx -= 1
        return val

    def peek(self):
        if self.is_empty():
            return None
        return self.st[self.top_idx]

    def size(self):
        return self.top_idx + 1

    def display(self):
        if self.is_empty():
            print("  (kosong)")
            return
        for i in range(self.top_idx, -1, -1):
            marker = " <-- TOP" if i == self.top_idx else ""
            print(f"  [{i}] {self.st[i]}{marker}")

class BrowserHistory:
    def __init__(self):
        self.back_stack = StackArray()
        self.forward_stack = StackArray()

    def visit(self, url):
        """Kunjungi URL baru: push ke back stack, kosongkan forward stack."""
        while not self.forward_stack.is_empty():
            self.forward_stack.pop()
        self.back_stack.push(url)
        print(f"\n>>> Mengunjungi: {url}")
        print(f"    push('{url}') ke back stack")

    def back(self):
        """Tombol BACK: pop dari back stack, push ke forward stack."""
        if self.back_stack.size() <= 1:
            print("\n[BACK] Tidak ada halaman sebelumnya.")
            return
        current = self.back_stack.pop()
        self.forward_stack.push(current)
        prev = self.back_stack.peek()
        print(f"\n<<< BACK: '{current}' -> forward stack")
        print(f"    Halaman saat ini: {prev}")

    def forward(self):
        """Tombol FORWARD: pop dari forward stack, push ke back stack."""
        if self.forward_stack.is_empty():
            print("\n[FORWARD] Tidak ada halaman berikutnya.")
            return
        next_url = self.forward_stack.pop()
        self.back_stack.push(next_url)
        print(f"\n>>> FORWARD: '{next_url}' -> back stack")
        print(f"    Halaman saat ini: {next_url}")

    def current_page(self):
        """Halaman yang sedang dibuka."""
        page = self.back_stack.peek()
        return page if page else "(tidak ada halaman)"

    def show_status(self):
        """Tampilkan status kedua stack."""
        print("\n" + "=" * 40)
        print(f"  Halaman saat ini: {self.current_page()}")
        print(f"\n  Back Stack (top -> bawah):")
        self.back_stack.display()
        print(f"\n  Forward Stack (top -> bawah):")
        self.forward_stack.display()
        back_available  = "Ya" if self.back_stack.size() > 1 else "Tidak"
        fwd_available   = "Ya" if not self.forward_stack.is_empty() else "Tidak"
        print(f"\n  Tombol Back   : {back_available}")
        print(f"  Tombol Forward: {fwd_available}")
        print("=" * 40)

def main():
    browser = BrowserHistory()
    pilih = 0
    while pilih != 5:
        print("\n=== BROWSER HISTORY (Stack) ===")
        print(f"  Halaman aktif : {browser.current_page()}")
        print("-------------------------------")
        print("1. Kunjungi URL baru")
        print("2. Tombol Back  (<-)")
        print("3. Tombol Forward (->)")
        print("4. Tampilkan status stack")
        print("5. Keluar")
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            url = input("Masukkan URL: ").strip()
            if url:
                browser.visit(url)
            else:
                print("URL tidak boleh kosong!")
        elif pilih == 2:
            browser.back()
        elif pilih == 3:
            browser.forward()
        elif pilih == 4:
            browser.show_status()
        elif pilih == 5:
            print("Browser ditutup.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()