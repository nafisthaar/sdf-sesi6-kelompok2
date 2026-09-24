BATAS_SANGAT_BAIK = 90
BATAS_BAIK = 75


# 1. Fungsi Hitung Skor
def hitung_skor(daftar_absensi):
    total_skor = 0.0
    for _, status in daftar_absensi:
        if status == "hadir":
            total_skor += 1.0
        elif status == "izin":
            total_skor += 0.5
    return total_skor


# 2. Fungsi Hitung Persentase
def hitung_persentase(total_skor, total_hari):
    if total_hari == 0:
        return 0.0
    return (total_skor / total_hari) * 100


# 3. Fungsi Klasifikasi Kategori
def klasifikasi_kategori(persentase):
    if persentase >= BATAS_SANGAT_BAIK:
        return "Sangat Baik"
    elif persentase >= BATAS_BAIK:
        return "Baik"
    else:
        return "Perlu Perhatian"


# 4. Fungsi Cetak Hasil
def cetak_hasil(nama_karyawan, persentase, kategori):
    print("Nama:", nama_karyawan)
    print("Rekap:", persentase, f"% - {kategori}")


# Fungsi Utama (Orchestrator)
def olah(data):
    if not data:
        return

    nama = data[0][0]
    total_skor = hitung_skor(data)
    persentase = hitung_persentase(total_skor, len(data))
    kategori = klasifikasi_kategori(persentase)

    cetak_hasil(nama, persentase, kategori)


absensi = [
    ("Sari", "hadir"),
    ("Sari", "hadir"),
    ("Sari", "izin"),
    ("Sari", "hadir"),
]

olah(absensi)