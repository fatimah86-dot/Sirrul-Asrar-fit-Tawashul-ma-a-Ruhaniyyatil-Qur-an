# Laporan Ekspor Word — Bab 2 (AR | LAT | ID)

Berkas: `Sirrul-Asrar-Bab2-Hal-239-516.docx`
Sumber: `transkripsi/bab2.md` + `data/LAPORAN-BAB2.md`
Skrip: `tools/make_docx_bab2.py` · Verifikator: `tools/verify_docx.py` · Font: `assets/fonts/Amiri-Regular.ttf` (OFL)

## 1. Cakupan (jujur, tanpa klaim palsu)

| Item | Nilai |
|---|---|
| Rentang di sumber | **hal. 239–516** (278 halaman, tanpa celah) |
| Rentang di sampul/Daftar Isi/footer | **Hal. 239–516** |
| Hal. 1–238 | **tidak ada** di sumber → tidak diekspor, tidak dikarang |
| Bab 1 (`bab1.md`, hal. 7–28) | **dokumen terpisah**, tidak digabung |

Nama berkas lama `Sirrul-Asrar-Bab2-Hal-1-516.docx` **dihapus/diganti** karena klaim rentangnya keliru.

## 2. Struktur

Sampul → **Catatan Cakupan** (halaman 2) → Daftar Isi (278 entri, satu judul satu baris) → Isi per halaman (AR kanan/RTL → LAT miring → ID) → **Daftar Wafak**.

## 3. Hasil verifikasi (`tools/verify_docx.py`)

| Pemeriksaan | Hasil |
|---|---|
| Blok AR / LAT / ID | **2022 / 2022 / 2022** |
| AR identik dengan sumber | **2022 / 2022** |
| LAT identik (setelah normalisasi markdown) | **2022 / 2022** |
| ID identik (setelah normalisasi markdown) | **2022 / 2022** |
| `[TIDAK JELAS]` | doc **220** = sumber **220** |
| `[TEKS ASLI DIJAGA]` | doc **172** = sumber **172** |
| Gambar | **193** media tertanam, **0** relasi `External` (bukan link) |
| Font Arab | **Amiri** (ascii/hAnsi/cs/eastAsia), 8093 rujukan |
| Klaim "Hal. 1–516" | **0** |

## 4. Rajah: crop ketat

**11 gambar** pada 10 halaman dibangun ulang menjadi potongan **ketat area wafaq** (`assets/rajah/sirrul-asrar-tight/`), memakai deteksi komponen terhubung (bingkai + isi menyatu), sehingga judul halaman, garis titik-titik, dan teks di luar bingkai **tidak ikut**:

hal. 286 (2), 342, 346, 376, 378, 381, 386, 393, 434, 490.

**Jumlah gambar tidak bertambah:** 193 di badan isi + 193 di Daftar Wafak = 386 rujukan, tetapi tetap **193 berkas unik**. Sebelumnya juga 193 gambar unik (dari 194 crop; `p428-wafaq-salam-qawlan.png` memang tidak dirujuk).

**Rajah yang isinya memang satu bidang penuh** (mis. hal. 490 = halaman judul berbingkai ornamen, hal. 286 = tabel penuh) tetap disisipkan utuh karena bingkainya sendiri adalah rajahnya — bukan "halaman utuh dengan teks di sekitar".

## 5. Pengulangan `عد٢`

Pola `عد٢` **tidak ditemukan** dalam `transkripsi/bab2.md` (0 kemunculan; `عد` diikuti huruf lain adalah kata biasa). Karena itu tidak ada pengulangan yang ditulis dua kali. Bila naskah sumber Anda memuat `عد٢`, kirimkan halamannya agar bisa diterapkan.

## 6. Yang belum bisa dikerjakan (butuh keputusan Anda)

1. **Pemeriksaan visual render** — sandbox ini tidak memiliki LibreOffice/Word, jadi render PDF/Word belum bisa dilakukan. Berkas dibuka di Word Anda; jika ada lafaz yang terpotong, kirim nomor halamannya.
2. **Amiri di mesin Anda** — font sudah disertakan di `assets/fonts/`; pasang dulu agar tampilan sama.
3. **Halaman 1–6 dan 29–238** — belum pernah ditranskripsi.
