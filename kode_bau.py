"""Modul contoh untuk latihan perbaikan kode sesuai PEP 8."""


def proses_data(a, b, c, e, f):
    """Contoh fungsi sederhana yang menjumlahkan beberapa nilai.

    Args:
        a: Nilai boolean pertama.
        b: Nilai boolean kedua.
        c: Nilai yang mungkin None.
        e: List berisi angka.
        f: Angka tambahan lainnya.

    Returns:
        Hasil penjumlahan, atau None jika syarat tidak terpenuhi.
    """
    if not (a and not b and c is None):
        return None

    hasil = e[0] + f + 1 + 0
    print(hasil)
    return hasil


def main():
    """Fungsi utama program."""
    proses_data(True, False, None, [2], 3)


if __name__ == "__main__":
    main()
